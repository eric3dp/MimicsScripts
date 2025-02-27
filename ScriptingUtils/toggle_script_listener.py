import threading
import trimatic

import sys
import time
import pymatic
import queue

has_required_packages = True

try:
    import rpyc
    from rpyc.utils.server import ThreadedServer
except:
    has_required_packages = False
    pass

# Evaluated every ms to retrieve python commands send to server


def execute_command(send_queue, receive_queue, exception_queue=None):
    try:
        # first get is without waiting. If empty here, wait for next check before starting to process the send queue.
        command_dict = send_queue.get_nowait()
    except queue.Empty:
        return

    while True:
        try:
            func = command_dict['func']
            args = command_dict['args']
            member = command_dict['member']
            if member:
                returnvalue = func(*args, **{})
            else:
                returnvalue = getattr(pymatic, func)(*args)
            receive_queue.put(returnvalue)
            # wait for a external python command for at most 1s.
            # this will allow the external python to keep filling the queue without yielding control back to 3-matic
            command_dict = send_queue.get(block=True, timeout=1)
        except queue.Empty:
            return
        except (AttributeError, RuntimeError, ValueError) as e:
            receive_queue.put(e)
            return


script_listener_send_queue = queue.Queue()
script_listener_receive_queue = queue.Queue()
trimatic.listener_server_thread = None


def command_fetch_timer_callback():
    execute_command(script_listener_send_queue,
                    script_listener_receive_queue)


if has_required_packages:
    # create_trimatic_listener_service is a wrapper enabling to pass two queues
    # to the Service class of rpyc.
    def create_trimatic_listener_service(send_queue, receive_queue):
        class TrimaticListenerService(rpyc.Service):
            # code that runs when a connection is created
            # Notify the user that the server connected
            def on_connect(self, conn):
                print("Connected to Server")

            # The exposed method that is called from the pymatic client module
            # The "Exposed" part is left out when calling the method
            def exposed_get_answer(self, func, args):
                command_dict = {'func': func, 'args': args, 'member': False}

                send_queue.put(command_dict)  # Put the command on the queue
                answer = receive_queue.get()  # Blocking wait for for answer
                if type(answer) == RuntimeError:  # Catch Exceptions, neccesary to do it seperately
                    raise answer
                elif type(answer) == AttributeError:
                    raise answer
                elif type(answer) == ValueError:
                    raise answer
                # happens when the connection to the listener is lost
                elif type(answer) == EOFError:
                    raise answer
                else:
                    return answer

        return TrimaticListenerService

    # Threading class setting put the server
    class TrimaticServerThread(threading.Thread):
        def __init__(self, send_queue, receive_queue, port):
            threading.Thread.__init__(self)
            trimatic_listener_service = create_trimatic_listener_service(
                send_queue, receive_queue)
            # Set arguments of server, allow to retrieve attributes for debugging.
            args = {'protocol_config': {"allow_public_attrs": True, "allow_setattr": True}}
            self.processing_server = ThreadedServer(
                trimatic_listener_service, port=port, hostname="loopback", ipv6=True, **args)

        # Initialisation method
        def run(self):
            self.processing_server.start()

    def reset_listener_thread():
        trimatic.listener_server_thread.processing_server.close()
        # closing the processing server will cause the server to stop
        # and the thread to end
        trimatic.listener_server_thread.join()
        trimatic.listener_server_thread = None

    port = None

    def toggle_listener():
        global port
        should_cycle_ports = False
        if port == None:
            port = 15000
            should_cycle_ports = True
        while True:
            try:
                if trimatic.listener_server_thread is None:
                    # There can be exception when socket is not bound, which will make to fail the initailization of ThreadedServer
                    trimatic.listener_server_thread = TrimaticServerThread(
                        script_listener_send_queue, script_listener_receive_queue, port)
                break  # get out of the while loop
            except OSError as e:
                if e.errno == 10048 and should_cycle_ports and port < 15100:
                    print("Port " + str(port) +
                          " already in use, trying next port")
                    port = port + 1
                else:
                    raise RuntimeError()
            except:
                print(
                    "Failed to start 3-matic script listener: Already in use in another instance")
                return False

        if not trimatic.listener_server_thread.is_alive():
            try:
                trimatic.listener_server_thread.start()
                print("3-matic script listener is active on port " + str(port))
                return True
            except:
                # The threaded servers can't be intialized, because port
                # is not available.
                # in this case release all the resources which are aquired.
                print("Failed to start 3-matic script listener")
                if trimatic.listener_server_thread.processing_server.active:
                    reset_listener_thread()
                return False
        else:
            try:
                reset_listener_thread()
                print("3-matic script listener is deactivated")
                return False
            except:
                print("Failed to deactivate 3-matic script listener")
                return True
