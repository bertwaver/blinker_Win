from PySide6.QtCore import *
from PySide6.QtWidgets import *
from mainwindow import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.webEngineView.load(QUrl("https://pwa.blinker.app/"))

        self.ui.webEngineView.loadFinished.connect(self.onLoadFinished)

    def onLoadFinished(self, ok):
        if ok:
            #自动登录实现
            if(self.ui.webEngineView.url().toString()=="https://pwa.blinker.app/login"):
                self.ui.webEngineView.page().runJavaScript('var usernameInput = document.querySelector("input[name=\'username\']");'
                                                           'var passwordInput = document.querySelector("input[name=\'password\']");'
                                                           'var usernameValue = "usename";'
                                                           'var passwordValue = "password";'
                                                           'var usernameEvent = new Event("input", { bubbles: true });'
                                                           'var passwordEvent = new Event("input", { bubbles: true });'
                                                           'usernameInput.value = usernameValue;'
                                                           'usernameInput.dispatchEvent(usernameEvent);'
                                                           'passwordInput.value = passwordValue;'
                                                           'passwordInput.dispatchEvent(passwordEvent);')

    def links_update(self):
        links = self.ui.webEngineView.url().toString()
        self.setWindowTitle("管理台 - " + links)

app = QApplication([])
mainw = MainWindow()
mainw.show()

timer_udpatelinks = QTimer()
timer_udpatelinks.setInterval(2000)
timer_udpatelinks.timeout.connect(mainw.links_update)
timer_udpatelinks.start()

app.exec_()
