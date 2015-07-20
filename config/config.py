from config_ui import *
from PyQt4 import QtGui, QtCore

class Config(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.bt_salvar, QtCore.SIGNAL('clicked()'), self.salvar)

    def salvar(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = Config()
    av.show()
    sys.exit(app.exec_())
