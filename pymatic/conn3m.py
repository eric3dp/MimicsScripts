import rpyc
import time
import pymatic

conn_3matic = None
port = None
timeout = 60
autoreconnect = True


def create_connection():
    global conn_3matic
    global port
    should_cycle_ports = False
    start = time.time()
    if port == None:
        port = 15000
        should_cycle_ports = True
    try:
        while True:
            try:
                print("Connecting to 3-matic listener on port {}".format(port))
                conn_3matic = rpyc.connect(host="loopback", port=port, ipv6=True, config={"allow_public_attrs": True, 'sync_request_timeout': 20000}, keepalive=True)
                print("Connected to 3-matic listener on port {} (autoreconnect={}, path={}).".format(port, autoreconnect, pymatic.get_application_path()))
                return
            except ConnectionRefusedError:
                if should_cycle_ports and port < 15100:  # try 100 ports
                    port = port + 1
                elif not should_cycle_ports:
                    if (timeout is not None and time.time() - start > timeout):  # keep trying until timeout reached
                        raise RuntimeError("Could not connect to port within {} seconds".format(timeout))
                else:
                    raise RuntimeError("No more ports available to try.")
    except Exception as e:
        raise RuntimeError("Could Not Connect, first start 3matic external IDE scripting service. Reason: {}".format(str(e)))


def send_command(name, params):
    if conn_3matic == None:
        print("Connection to 3-matic was not initialized, creating connnection.")
        create_connection()
    elif conn_3matic.closed == True and autoreconnect == True:
        print("Connection to 3-matic was closed, trying to reestablish connection.")
        create_connection()
    try:
        return conn_3matic.root.get_answer(name, params)
    except EOFError:  # try to reestablish the connection in case the listener restarted for some reason
        if autoreconnect:
            print("Connection to 3-matic lost, trying to reestablish connection.")
            create_connection()
        else:
            raise RuntimeError("Connection to 3-matic lost.")
    return conn_3matic.root.get_answer(name, params)
