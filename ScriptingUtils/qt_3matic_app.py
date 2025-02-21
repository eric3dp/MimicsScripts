import sys
import threading

from PyQt5.QtWidgets import QApplication


class Qt3MaticApp:
     started = False
     def  __init__(self,ui_class,*args, **kwargs):
          self.ui_class = ui_class
          self.args = args
          self.kwargs = kwargs

     def  __qt_thread_func(self):
            app = QApplication.instance()
            if app is None or not Qt3MaticApp.started:
                app = QApplication(sys.argv)
                print("Qt application started")
            ui = self.ui_class(*self.args,**self.kwargs)
            ui.show()
            Qt3MaticApp.started =True
            app.exec()
            print("Qt application Quit")
            Qt3MaticApp.started =False

     def  __init_qt_thread(self):
          if  Qt3MaticApp.started:
              raise Exception("Attempt to create more than one instance of QtApplication while one is active")

          if  sys.executable.endswith('3-matic.exe'):
              qt_thread = threading.Thread(target=self.__qt_thread_func)
              qt_thread.daemon = True
              qt_thread.start()
          else:
              self.__qt_thread_func()

     def run(self):
         self.__init_qt_thread()
