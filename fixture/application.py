from pywinauto.application import Application as WinApplication
from fixture.group import Grouphelper


class Application:
    def __init__(self, target):
        self.application = WinApplication(backend="win32").start(target)
        self.main_window = self.application.window(title='Free Address Book')
        self.main_window.wait('visible')
        self.group = Grouphelper(self)


    def destroy(self):
        self.main_window.close()
