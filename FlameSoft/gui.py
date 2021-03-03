# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(750, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.length = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QtCore.QSize(400, 0))
        self.length.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.length.setObjectName("length")
        self.gridLayout_2.addWidget(self.length, 6, 1, 1, 1)
        self.direction = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.direction.sizePolicy().hasHeightForWidth())
        self.direction.setSizePolicy(sizePolicy)
        self.direction.setMinimumSize(QtCore.QSize(400, 0))
        self.direction.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.direction.setObjectName("direction")
        self.direction.addItem("")
        self.direction.addItem("")
        self.gridLayout_2.addWidget(self.direction, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 3, 1, 1)
        self.videopath = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videopath.sizePolicy().hasHeightForWidth())
        self.videopath.setSizePolicy(sizePolicy)
        self.videopath.setMinimumSize(QtCore.QSize(400, 0))
        self.videopath.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.videopath.setObjectName("videopath")
        self.gridLayout_2.addWidget(self.videopath, 1, 1, 1, 1)
        self.speed = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy)
        self.speed.setMinimumSize(QtCore.QSize(400, 0))
        self.speed.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.speed.setObjectName("speed")
        self.gridLayout_2.addWidget(self.speed, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 8, 2, 1, 2)
        self.b_video = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_video.sizePolicy().hasHeightForWidth())
        self.b_video.setSizePolicy(sizePolicy)
        self.b_video.setMinimumSize(QtCore.QSize(0, 0))
        self.b_video.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_video.setObjectName("b_video")
        self.gridLayout_2.addWidget(self.b_video, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 7, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 5, 2, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 6, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.useprevious = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useprevious.sizePolicy().hasHeightForWidth())
        self.useprevious.setSizePolicy(sizePolicy)
        self.useprevious.setMinimumSize(QtCore.QSize(400, 0))
        self.useprevious.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.useprevious.setObjectName("useprevious")
        self.useprevious.addItem("")
        self.useprevious.addItem("")
        self.gridLayout_2.addWidget(self.useprevious, 8, 1, 1, 1)
        self.subframe = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subframe.sizePolicy().hasHeightForWidth())
        self.subframe.setSizePolicy(sizePolicy)
        self.subframe.setMinimumSize(QtCore.QSize(400, 0))
        self.subframe.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.subframe.setObjectName("subframe")
        self.subframe.addItem("")
        self.subframe.addItem("")
        self.gridLayout_2.addWidget(self.subframe, 12, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 12, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 12, 2, 1, 2)
        self.slices = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slices.sizePolicy().hasHeightForWidth())
        self.slices.setSizePolicy(sizePolicy)
        self.slices.setMinimumSize(QtCore.QSize(400, 0))
        self.slices.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.slices.setObjectName("slices")
        self.gridLayout_2.addWidget(self.slices, 2, 1, 1, 1)
        self.outpath = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outpath.sizePolicy().hasHeightForWidth())
        self.outpath.setSizePolicy(sizePolicy)
        self.outpath.setMinimumSize(QtCore.QSize(400, 0))
        self.outpath.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.outpath.setObjectName("outpath")
        self.gridLayout_2.addWidget(self.outpath, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.filter = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter.sizePolicy().hasHeightForWidth())
        self.filter.setSizePolicy(sizePolicy)
        self.filter.setMinimumSize(QtCore.QSize(400, 0))
        self.filter.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.filter.setObjectName("filter")
        self.gridLayout_2.addWidget(self.filter, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 11, 0, 1, 1)
        self.ratio = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ratio.sizePolicy().hasHeightForWidth())
        self.ratio.setSizePolicy(sizePolicy)
        self.ratio.setMinimumSize(QtCore.QSize(400, 0))
        self.ratio.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.ratio.setObjectName("ratio")
        self.gridLayout_2.addWidget(self.ratio, 11, 1, 1, 1)
        self.b_out = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_out.sizePolicy().hasHeightForWidth())
        self.b_out.setSizePolicy(sizePolicy)
        self.b_out.setMinimumSize(QtCore.QSize(0, 0))
        self.b_out.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_out.setObjectName("b_out")
        self.gridLayout_2.addWidget(self.b_out, 0, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 11, 2, 1, 2)
        self.thresh_data = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresh_data.sizePolicy().hasHeightForWidth())
        self.thresh_data.setSizePolicy(sizePolicy)
        self.thresh_data.setMinimumSize(QtCore.QSize(400, 0))
        self.thresh_data.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.thresh_data.setObjectName("thresh_data")
        self.gridLayout_2.addWidget(self.thresh_data, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.b_process = QtWidgets.QPushButton(self.centralwidget)
        self.b_process.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_process.setObjectName("b_process")
        self.gridLayout.addWidget(self.b_process, 0, 0, 1, 1)
        self.b_whiten = QtWidgets.QPushButton(self.centralwidget)
        self.b_whiten.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_whiten.setObjectName("b_whiten")
        self.gridLayout.addWidget(self.b_whiten, 0, 1, 1, 1)
        self.b_blacken = QtWidgets.QPushButton(self.centralwidget)
        self.b_blacken.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_blacken.setObjectName("b_blacken")
        self.gridLayout.addWidget(self.b_blacken, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 0, 3, 1, 1)
        self.b_detect = QtWidgets.QPushButton(self.centralwidget)
        self.b_detect.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_detect.setObjectName("b_detect")
        self.gridLayout.addWidget(self.b_detect, 1, 0, 1, 1)
        self.b_data = QtWidgets.QPushButton(self.centralwidget)
        self.b_data.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_data.setObjectName("b_data")
        self.gridLayout.addWidget(self.b_data, 1, 1, 1, 1)
        self.b_thresh = QtWidgets.QPushButton(self.centralwidget)
        self.b_thresh.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.b_thresh.setObjectName("b_thresh")
        self.gridLayout.addWidget(self.b_thresh, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlameSoft"))
        self.direction.setItemText(0, _translate("MainWindow", "Left"))
        self.direction.setItemText(1, _translate("MainWindow", "Right"))
        self.label_6.setText(_translate("MainWindow", "Flame Direction"))
        self.label_8.setText(_translate("MainWindow", "Video Speed (FPS)"))
        self.videopath.setText(_translate("MainWindow", "E:/Github/Flame-Speed-Tool/bin/video1.wmv"))
        self.label_9.setText(_translate("MainWindow", "Use Previous Crop"))
        self.b_video.setText(_translate("MainWindow", "Browse"))
        self.label_7.setText(_translate("MainWindow", "Croped Area Length (ft)"))
        self.label_2.setText(_translate("MainWindow", "Video Path"))
        self.useprevious.setItemText(0, _translate("MainWindow", "True"))
        self.useprevious.setItemText(1, _translate("MainWindow", "False"))
        self.subframe.setItemText(0, _translate("MainWindow", "False"))
        self.subframe.setItemText(1, _translate("MainWindow", "True"))
        self.label_10.setText(_translate("MainWindow", "Substract Frame 1"))
        self.outpath.setText(_translate("MainWindow", "E:/Github/Flame-Speed-Tool/bin/"))
        self.label_4.setText(_translate("MainWindow", "Fliter Data"))
        self.label_3.setText(_translate("MainWindow", "Video Slices"))
        self.label.setText(_translate("MainWindow", "Out Path"))
        self.label_5.setText(_translate("MainWindow", "Thresh Data"))
        self.label_12.setText(_translate("MainWindow", "Height / Flame Ratio"))
        self.b_out.setText(_translate("MainWindow", "Browse"))
        self.b_process.setText(_translate("MainWindow", "Process Video"))
        self.b_whiten.setText(_translate("MainWindow", "Whiten Image"))
        self.b_blacken.setText(_translate("MainWindow", "Blacken Image"))
        self.b_detect.setText(_translate("MainWindow", "Run Detection"))
        self.b_data.setText(_translate("MainWindow", "Get Data"))
        self.b_thresh.setText(_translate("MainWindow", "View Thresh"))
