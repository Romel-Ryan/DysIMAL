# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppliedProblemSubtest6to10.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class AppliedProblemSubtest6To10:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 20, 800, 480))
        self.frame.setStyleSheet("background-color: rgb(180, 203, 253);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 120, 761, 291))
        self.frame_2.setStyleSheet("background-color: rgb(218, 229, 255);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 741, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 741, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 741, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 741, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 741, 51))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(180, 203, 253);\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(180, 203, 253);\n"
"border-radius: 10px;")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(410, 10, 331, 20))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid #000000\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 60, 331, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid #000000\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 100, 301, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid #000000\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 150, 301, 20))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid #000000\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 190, 281, 20))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid #000000\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 0, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(270, 90, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Directions:"))
        self.label_5.setText(_translate("MainWindow", " 6.Mr. De Guzman and the boys spent Php 567.75 for food and Php 175.50 for \n"
"transportation during the Science Fair Camp. If they had Php 800.00 to spend,\n"
" how much money was left?"))
        self.label_6.setText(_translate("MainWindow", "7.10% of our class of 40 was unable to join the field trip.\n"
" How many in our class joined the field trip?"))
        self.label_7.setText(_translate("MainWindow", "8.A company donates 935 pencils to a school. The pencils are divided evenly among 9 \n"
"classrooms. The rest of the pencils are given to the library. How many pencils were \n"
"donated to each classroom and to the library?"))
        self.label_8.setText(_translate("MainWindow", "9. The city park is 9 1/2 miles from Roland Elementary School. The city library is 3 3/10 \n"
" from the same school. 9.How much farther from the school is the park than the library? "))
        self.label_9.setText(_translate("MainWindow", "10. There are 12 people in Mrs. Hilt’s living room. 6 people are wearing socks and 4 people \n"
"are wearing shoes. 3 people are wearing both. How many people are in bare feet? "))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.label.setText(_translate("MainWindow", "Dyscalculia Immediate Mode of Assesment in Learning System"))
        self.label_4.setText(_translate("MainWindow", "Applied Problem Subtest"))
