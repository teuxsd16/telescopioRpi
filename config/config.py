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
        dialog.resize(322, 289)
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 191, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(dialog)
        self.spinBox.setGeometry(QtCore.QRect(110, 80, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 80, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(210, 80, 42, 22))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(dialog)
        self.spinBox_4.setGeometry(QtCore.QRect(260, 80, 42, 22))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_5 = QtGui.QSpinBox(dialog)
        self.spinBox_5.setGeometry(QtCore.QRect(110, 140, 42, 22))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.spinBox_6 = QtGui.QSpinBox(dialog)
        self.spinBox_6.setGeometry(QtCore.QRect(160, 140, 42, 22))
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.spinBox_7 = QtGui.QSpinBox(dialog)
        self.spinBox_7.setGeometry(QtCore.QRect(210, 140, 42, 22))
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.spinBox_8 = QtGui.QSpinBox(dialog)
        self.spinBox_8.setGeometry(QtCore.QRect(260, 140, 42, 22))
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
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

        self.retranslateUi(dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.buttonBox, self.lineEdit)
        dialog.setTabOrder(self.lineEdit, self.spinBox)
        dialog.setTabOrder(self.spinBox, self.spinBox_2)
        dialog.setTabOrder(self.spinBox_2, self.spinBox_3)
        dialog.setTabOrder(self.spinBox_3, self.spinBox_4)
        dialog.setTabOrder(self.spinBox_4, self.spinBox_5)
        dialog.setTabOrder(self.spinBox_5, self.spinBox_6)
        dialog.setTabOrder(self.spinBox_6, self.spinBox_7)
        dialog.setTabOrder(self.spinBox_7, self.spinBox_8)

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

