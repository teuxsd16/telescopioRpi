# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(322, 257)
        self.tx_ip = QtGui.QLineEdit(dialog)
        self.tx_ip.setGeometry(QtCore.QRect(110, 20, 191, 21))
        self.tx_ip.setObjectName(_fromUtf8("tx_ip"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.motor_alt_1 = QtGui.QSpinBox(dialog)
        self.motor_alt_1.setGeometry(QtCore.QRect(110, 80, 42, 22))
        self.motor_alt_1.setObjectName(_fromUtf8("motor_alt_1"))
        self.motor_alt_2 = QtGui.QSpinBox(dialog)
        self.motor_alt_2.setGeometry(QtCore.QRect(160, 80, 42, 22))
        self.motor_alt_2.setObjectName(_fromUtf8("motor_alt_2"))
        self.motor_alt_3 = QtGui.QSpinBox(dialog)
        self.motor_alt_3.setGeometry(QtCore.QRect(210, 80, 42, 22))
        self.motor_alt_3.setObjectName(_fromUtf8("motor_alt_3"))
        self.motor_alt_4 = QtGui.QSpinBox(dialog)
        self.motor_alt_4.setGeometry(QtCore.QRect(260, 80, 42, 22))
        self.motor_alt_4.setObjectName(_fromUtf8("motor_alt_4"))
        self.motor_az_1 = QtGui.QSpinBox(dialog)
        self.motor_az_1.setGeometry(QtCore.QRect(110, 140, 42, 22))
        self.motor_az_1.setObjectName(_fromUtf8("motor_az_1"))
        self.motor_az_2 = QtGui.QSpinBox(dialog)
        self.motor_az_2.setGeometry(QtCore.QRect(160, 140, 42, 22))
        self.motor_az_2.setObjectName(_fromUtf8("motor_az_2"))
        self.motor_az_3 = QtGui.QSpinBox(dialog)
        self.motor_az_3.setGeometry(QtCore.QRect(210, 140, 42, 22))
        self.motor_az_3.setObjectName(_fromUtf8("motor_az_3"))
        self.motor_az_4 = QtGui.QSpinBox(dialog)
        self.motor_az_4.setGeometry(QtCore.QRect(260, 140, 42, 22))
        self.motor_az_4.setObjectName(_fromUtf8("motor_az_4"))
        self.label_3 = QtGui.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 60, 21, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(170, 60, 21, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 60, 21, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(270, 60, 21, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(dialog)
        self.label_8.setGeometry(QtCore.QRect(270, 120, 21, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(dialog)
        self.label_9.setGeometry(QtCore.QRect(170, 120, 21, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(dialog)
        self.label_10.setGeometry(QtCore.QRect(120, 120, 21, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(dialog)
        self.label_11.setGeometry(QtCore.QRect(220, 120, 21, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.bt_salvar = QtGui.QPushButton(dialog)
        self.bt_salvar.setGeometry(QtCore.QRect(230, 220, 75, 23))
        self.bt_salvar.setObjectName(_fromUtf8("bt_salvar"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.tx_ip, self.motor_alt_1)
        dialog.setTabOrder(self.motor_alt_1, self.motor_alt_2)
        dialog.setTabOrder(self.motor_alt_2, self.motor_alt_3)
        dialog.setTabOrder(self.motor_alt_3, self.motor_alt_4)
        dialog.setTabOrder(self.motor_alt_4, self.motor_az_1)
        dialog.setTabOrder(self.motor_az_1, self.motor_az_2)
        dialog.setTabOrder(self.motor_az_2, self.motor_az_3)
        dialog.setTabOrder(self.motor_az_3, self.motor_az_4)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "telescopioRpi - Configurações", None))
        self.label.setText(_translate("dialog", "IP do Servidor (RPi):", None))
        self.label_2.setText(_translate("dialog", "Motor de Altitude:", None))
        self.label_3.setText(_translate("dialog", "Motor de Azimute:", None))
        self.label_4.setText(_translate("dialog", "In 1", None))
        self.label_5.setText(_translate("dialog", "In 2", None))
        self.label_6.setText(_translate("dialog", "In 3", None))
        self.label_7.setText(_translate("dialog", "In 4", None))
        self.label_8.setText(_translate("dialog", "In 4", None))
        self.label_9.setText(_translate("dialog", "In 2", None))
        self.label_10.setText(_translate("dialog", "In 1", None))
        self.label_11.setText(_translate("dialog", "In 3", None))
        self.bt_salvar.setText(_translate("dialog", "Salvar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

