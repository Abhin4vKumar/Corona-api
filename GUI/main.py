# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
from os import path as p
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def initialize(self):
        self.api = "https://api.covid19api.com/summary"    
        self.refresh_data()
        self.session_path = 'data/'
        self.quick_param_settings = 'Qpanel_settings.dll'
        self.load_settings()
        self.display_data_quick()
        self.label_desc.adjustSize()
        self.label_15.adjustSize()
        self.label_5.adjustSize()

    def load_settings(self):
        if p.exists(p.join(self.session_path,self.quick_param_settings)):
                with open(p.join(self.session_path,self.quick_param_settings)) as panel_file:
                        self.quick_param = panel_file.read().strip().strip('\n')
        else:
                self.quick_param = 'Global'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 595)
        MainWindow.setMinimumSize(QtCore.QSize(935, 595))
        MainWindow.setMaximumSize(QtCore.QSize(935, 595))
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_left = QtWidgets.QFrame(self.centralwidget)
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 371, 551))
        self.frame_left.setStyleSheet("#frame_left{\n"
"    background-color:white;\n"
"    font-family:sans-serif;\n"
"}\n"
"#frame_left:hover{\n"
"}")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.frame_left_dash = QtWidgets.QFrame(self.frame_left)
        self.frame_left_dash.setGeometry(QtCore.QRect(0, 0, 61, 551))
        self.frame_left_dash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_dash.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_dash.setObjectName("frame_left_dash")
        self.label_11 = QtWidgets.QLabel(self.frame_left)
        self.label_11.setGeometry(QtCore.QRect(100, 60, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_left)
        self.label_12.setGeometry(QtCore.QRect(80, 190, 121, 16))
        self.label_12.setObjectName("label_12")
        self.Country_name_quick = QtWidgets.QLabel(self.frame_left)
        self.Country_name_quick.setGeometry(QtCore.QRect(230, 170, 57, 15))
        self.Country_name_quick.setObjectName("Country_name_quick")
        self.Country_code_quick = QtWidgets.QLabel(self.frame_left)
        self.Country_code_quick.setGeometry(QtCore.QRect(230, 190, 57, 15))
        self.Country_code_quick.setObjectName("Country_code_quick")
        self.label_15 = QtWidgets.QLabel(self.frame_left)
        self.label_15.setGeometry(QtCore.QRect(80, 250, 121, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_left)
        self.label_16.setGeometry(QtCore.QRect(80, 210, 121, 16))
        self.label_16.setObjectName("label_16")
        self.Date_specific_quick = QtWidgets.QLabel(self.frame_left)
        self.Date_specific_quick.setGeometry(QtCore.QRect(210, 250, 57, 15))
        self.Date_specific_quick.setObjectName("Date_specific_quick")
        self.label_18 = QtWidgets.QLabel(self.frame_left)
        self.label_18.setGeometry(QtCore.QRect(80, 170, 121, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_left)
        self.label_19.setGeometry(QtCore.QRect(80, 230, 121, 16))
        self.label_19.setObjectName("label_19")
        self.Date_quick = QtWidgets.QLabel(self.frame_left)
        self.Date_quick.setGeometry(QtCore.QRect(210, 230, 57, 15))
        self.Date_quick.setObjectName("Date_quick")
        self.Slug_quick = QtWidgets.QLabel(self.frame_left)
        self.Slug_quick.setGeometry(QtCore.QRect(230, 210, 57, 15))
        self.Slug_quick.setObjectName("Slug_quick")
        self.newRecovered_quick = QtWidgets.QLabel(self.frame_left)
        self.newRecovered_quick.setGeometry(QtCore.QRect(230, 350, 57, 15))
        self.newRecovered_quick.setObjectName("newRecovered_quick")
        self.label_37 = QtWidgets.QLabel(self.frame_left)
        self.label_37.setGeometry(QtCore.QRect(80, 390, 131, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_left)
        self.label_38.setGeometry(QtCore.QRect(80, 350, 131, 16))
        self.label_38.setObjectName("label_38")
        self.totalDeaths_quick = QtWidgets.QLabel(self.frame_left)
        self.totalDeaths_quick.setGeometry(QtCore.QRect(230, 390, 57, 15))
        self.totalDeaths_quick.setObjectName("totalDeaths_quick")
        self.label_40 = QtWidgets.QLabel(self.frame_left)
        self.label_40.setGeometry(QtCore.QRect(80, 370, 131, 16))
        self.label_40.setObjectName("label_40")
        self.newConfirmed_quick = QtWidgets.QLabel(self.frame_left)
        self.newConfirmed_quick.setGeometry(QtCore.QRect(230, 310, 57, 15))
        self.newConfirmed_quick.setObjectName("newConfirmed_quick")
        self.totalConfirmed_quick = QtWidgets.QLabel(self.frame_left)
        self.totalConfirmed_quick.setGeometry(QtCore.QRect(230, 330, 57, 15))
        self.totalConfirmed_quick.setObjectName("totalConfirmed_quick")
        self.totalRecovered_quick = QtWidgets.QLabel(self.frame_left)
        self.totalRecovered_quick.setGeometry(QtCore.QRect(230, 370, 57, 15))
        self.totalRecovered_quick.setObjectName("totalRecovered_quick")
        self.label_44 = QtWidgets.QLabel(self.frame_left)
        self.label_44.setGeometry(QtCore.QRect(80, 330, 131, 16))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_left)
        self.label_45.setGeometry(QtCore.QRect(80, 310, 131, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame_left)
        self.label_46.setGeometry(QtCore.QRect(80, 470, 131, 16))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.frame_left)
        self.label_47.setGeometry(QtCore.QRect(80, 450, 131, 16))
        self.label_47.setObjectName("label_47")
        self.Recovery_rate_quick = QtWidgets.QLabel(self.frame_left)
        self.Recovery_rate_quick.setGeometry(QtCore.QRect(230, 470, 57, 15))
        self.Recovery_rate_quick.setObjectName("Recovery_rate_quick")
        self.Recovery_perc_quick = QtWidgets.QLabel(self.frame_left)
        self.Recovery_perc_quick.setGeometry(QtCore.QRect(230, 450, 57, 15))
        self.Recovery_perc_quick.setObjectName("Recovery_perc_quick")
        self.frame_right = QtWidgets.QFrame(self.centralwidget)
        self.frame_right.setGeometry(QtCore.QRect(380, 0, 551, 551))
        self.frame_right.setStyleSheet("#frame_right{\n"
"    background-color:white;\n"
"    font-family:sans-serif;\n"
"}\n"
"#frame_right:hover{\n"
"}")
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.btn_search = QtWidgets.QPushButton(self.frame_right)
        self.btn_search.setGeometry(QtCore.QRect(440, 130, 91, 31))
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_search.setStyleSheet("#btn_search{\n"
"    background-color:white;\n"
"    border:1px solid rgb(207,207,207);\n"
"    border-radius: 10px;\n"
"    color : rgb(77,77,77);\n"
"}\n"
"#btn_search:hover{\n"
"    color : white;\n"
"    background-color: royalblue;\n"
"}")
        self.btn_search.setObjectName("btn_search")
        self.Search_box = QtWidgets.QLineEdit(self.frame_right)
        self.Search_box.setGeometry(QtCore.QRect(20, 130, 411, 31))
        self.Search_box.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Search_box.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Search_box.setStyleSheet("#Search_box{\n"
"    color:rgb(77,77,77);\n"
"}")
        self.Search_box.setObjectName("Search_box")
        self.head_title = QtWidgets.QLabel(self.frame_right)
        self.head_title.setGeometry(QtCore.QRect(150, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.head_title.setFont(font)
        self.head_title.setStyleSheet("color:#101010;")
        self.head_title.setObjectName("head_title")
        self.label_desc = QtWidgets.QLabel(self.frame_right)
        self.label_desc.setGeometry(QtCore.QRect(90, 70, 381, 16))
        self.label_desc.setStyleSheet("color : rgb(101,101,101);")
        self.label_desc.setObjectName("label_desc")
        self.logs_area = QtWidgets.QPlainTextEdit(self.frame_right)
        self.logs_area.setGeometry(QtCore.QRect(10, 430, 531, 111))
        self.logs_area.setObjectName("logs_area")
        self.results_tab = QtWidgets.QTabWidget(self.frame_right)
        self.results_tab.setGeometry(QtCore.QRect(20, 170, 511, 251))
        self.results_tab.setStyleSheet("")
        self.results_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.results_tab.setTabBarAutoHide(False)
        self.results_tab.setObjectName("results_tab")
        self.data_disp_tab = QtWidgets.QWidget()
        self.data_disp_tab.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.data_disp_tab.setObjectName("data_disp_tab")
        self.data_tabs = QtWidgets.QTabWidget(self.data_disp_tab)
        self.data_tabs.setGeometry(QtCore.QRect(10, 10, 491, 201))
        self.data_tabs.setObjectName("data_tabs")
        self.country_dets_tab = QtWidgets.QWidget()
        self.country_dets_tab.setObjectName("country_dets_tab")
        self.Country_name_search = QtWidgets.QLabel(self.country_dets_tab)
        self.Country_name_search.setGeometry(QtCore.QRect(180, 20, 57, 15))
        self.Country_name_search.setObjectName("Country_name_search")
        self.label_2 = QtWidgets.QLabel(self.country_dets_tab)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 121, 16))
        self.label_2.setObjectName("label_2")
        self.Country_code_search = QtWidgets.QLabel(self.country_dets_tab)
        self.Country_code_search.setGeometry(QtCore.QRect(180, 40, 57, 15))
        self.Country_code_search.setObjectName("Country_code_search")
        self.label_3 = QtWidgets.QLabel(self.country_dets_tab)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.country_dets_tab)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.label_5.setObjectName("label_5")
        self.Date_specific_search = QtWidgets.QLabel(self.country_dets_tab)
        self.Date_specific_search.setGeometry(QtCore.QRect(180, 100, 57, 15))
        self.Date_specific_search.setObjectName("Date_specific_search")
        self.label = QtWidgets.QLabel(self.country_dets_tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.country_dets_tab)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_4.setObjectName("label_4")
        self.Date_search = QtWidgets.QLabel(self.country_dets_tab)
        self.Date_search.setGeometry(QtCore.QRect(180, 80, 57, 15))
        self.Date_search.setObjectName("Date_search")
        self.Slug_search = QtWidgets.QLabel(self.country_dets_tab)
        self.Slug_search.setGeometry(QtCore.QRect(180, 60, 57, 15))
        self.Slug_search.setObjectName("Slug_search")
        self.data_tabs.addTab(self.country_dets_tab, "")
        self.corona_stats_tab = QtWidgets.QWidget()
        self.corona_stats_tab.setObjectName("corona_stats_tab")
        self.label_22 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_22.setGeometry(QtCore.QRect(20, 40, 131, 16))
        self.label_22.setObjectName("label_22")
        self.newConfirmed_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.newConfirmed_search.setGeometry(QtCore.QRect(170, 20, 57, 15))
        self.newConfirmed_search.setObjectName("newConfirmed_search")
        self.totalConfirmed_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.totalConfirmed_search.setGeometry(QtCore.QRect(170, 40, 57, 15))
        self.totalConfirmed_search.setObjectName("totalConfirmed_search")
        self.label_25 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_25.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_26.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_26.setObjectName("label_26")
        self.Recovery_perc_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.Recovery_perc_search.setGeometry(QtCore.QRect(170, 120, 57, 15))
        self.Recovery_perc_search.setObjectName("Recovery_perc_search")
        self.label_28 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_28.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_29.setGeometry(QtCore.QRect(20, 80, 131, 16))
        self.label_29.setObjectName("label_29")
        self.totalRecovered_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.totalRecovered_search.setGeometry(QtCore.QRect(170, 80, 57, 15))
        self.totalRecovered_search.setObjectName("totalRecovered_search")
        self.newRecovered_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.newRecovered_search.setGeometry(QtCore.QRect(170, 60, 57, 15))
        self.newRecovered_search.setObjectName("newRecovered_search")
        self.label_32 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_32.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.label_32.setObjectName("label_32")
        self.Recovery_rate_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.Recovery_rate_search.setGeometry(QtCore.QRect(170, 140, 57, 15))
        self.Recovery_rate_search.setObjectName("Recovery_rate_search")
        self.label_34 = QtWidgets.QLabel(self.corona_stats_tab)
        self.label_34.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.label_34.setObjectName("label_34")
        self.totalDeaths_search = QtWidgets.QLabel(self.corona_stats_tab)
        self.totalDeaths_search.setGeometry(QtCore.QRect(170, 100, 57, 15))
        self.totalDeaths_search.setObjectName("totalDeaths_search")
        self.data_tabs.addTab(self.corona_stats_tab, "")
        self.results_tab.addTab(self.data_disp_tab, "")
        self.search_res_tab = QtWidgets.QWidget()
        self.search_res_tab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_res_tab.setObjectName("search_res_tab")
        self.search_res_list = QtWidgets.QListView(self.search_res_tab)
        self.search_res_list.setGeometry(QtCore.QRect(10, 10, 481, 201))
        self.search_res_list.setObjectName("search_res_list")
        self.results_tab.addTab(self.search_res_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHide_Menu = QtWidgets.QAction(MainWindow)
        self.actionHide_Menu.setObjectName("actionHide_Menu")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOther.addAction(self.actionHide_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())

        self.retranslateUi(MainWindow)
        self.results_tab.setCurrentIndex(0)
        self.data_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame_left.setStatusTip(_translate("MainWindow", "Dashboard"))
        self.frame_left_dash.setStatusTip(_translate("MainWindow", "Navigation Menu"))
        self.label_11.setStatusTip(_translate("MainWindow", "Quick Stats Head"))
        self.label_11.setText(_translate("MainWindow", "Global Stats"))
        self.label_12.setStatusTip(_translate("MainWindow", "Country Code"))
        self.label_12.setText(_translate("MainWindow", "Country Code"))
        self.Country_name_quick.setText(_translate("MainWindow", "--"))
        self.Country_code_quick.setText(_translate("MainWindow", "--"))
        self.label_15.setStatusTip(_translate("MainWindow", "Date (Specific Zone)"))
        self.label_15.setText(_translate("MainWindow", "Date (GMT + 5:30)"))
        self.label_16.setStatusTip(_translate("MainWindow", "Slug"))
        self.label_16.setText(_translate("MainWindow", "Slug"))
        self.Date_specific_quick.setText(_translate("MainWindow", "--"))
        self.label_18.setStatusTip(_translate("MainWindow", "Country Name"))
        self.label_18.setText(_translate("MainWindow", "Country"))
        self.label_19.setStatusTip(_translate("MainWindow", "Date"))
        self.label_19.setText(_translate("MainWindow", "Date"))
        self.Date_quick.setText(_translate("MainWindow", "--"))
        self.Slug_quick.setText(_translate("MainWindow", "--"))
        self.newRecovered_quick.setText(_translate("MainWindow", "--"))
        self.label_37.setStatusTip(_translate("MainWindow", "Total Deaths "))
        self.label_37.setText(_translate("MainWindow", "Total Deaths"))
        self.label_38.setStatusTip(_translate("MainWindow", "New Recovered Cases "))
        self.label_38.setText(_translate("MainWindow", "New Recovered"))
        self.totalDeaths_quick.setText(_translate("MainWindow", "--"))
        self.label_40.setStatusTip(_translate("MainWindow", "Total Recovered Cases"))
        self.label_40.setText(_translate("MainWindow", "Total Recovered"))
        self.newConfirmed_quick.setText(_translate("MainWindow", "--"))
        self.totalConfirmed_quick.setText(_translate("MainWindow", "--"))
        self.totalRecovered_quick.setText(_translate("MainWindow", "--"))
        self.label_44.setStatusTip(_translate("MainWindow", "Total Confirmed Cases"))
        self.label_44.setText(_translate("MainWindow", "Total Confirmed"))
        self.label_45.setStatusTip(_translate("MainWindow", "New Confirmed cases"))
        self.label_45.setText(_translate("MainWindow", "New Confirmed"))
        self.label_46.setStatusTip(_translate("MainWindow", "Recovery Rate in Percentage"))
        self.label_46.setText(_translate("MainWindow", "Recovery Rate (in %)"))
        self.label_47.setStatusTip(_translate("MainWindow", "Recovery Percentage"))
        self.label_47.setText(_translate("MainWindow", "Recovery (in %)"))
        self.Recovery_rate_quick.setText(_translate("MainWindow", "--"))
        self.Recovery_perc_quick.setText(_translate("MainWindow", "--"))
        self.btn_search.setStatusTip(_translate("MainWindow", "Search Button"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.Search_box.setStatusTip(_translate("MainWindow", "Search Box"))
        self.Search_box.setText(_translate("MainWindow", "Search Here"))
        self.head_title.setStatusTip(_translate("MainWindow", "Application Name"))
        self.head_title.setText(_translate("MainWindow", "Corona - API"))
        self.label_desc.setStatusTip(_translate("MainWindow", "Application Description"))
        self.label_desc.setText(_translate("MainWindow", "Get Real-Time Corona Status of any Country around the Globe"))
        self.logs_area.setStatusTip(_translate("MainWindow", "logs"))
        self.results_tab.setStatusTip(_translate("MainWindow", "Results Tab"))
        self.data_tabs.setStatusTip(_translate("MainWindow", "Data tab"))
        self.Country_name_search.setText(_translate("MainWindow", "--"))
        self.label_2.setStatusTip(_translate("MainWindow", "Country Code"))
        self.label_2.setText(_translate("MainWindow", "Country Code"))
        self.Country_code_search.setText(_translate("MainWindow", "--"))
        self.label_3.setStatusTip(_translate("MainWindow", "Slug"))
        self.label_3.setText(_translate("MainWindow", "Slug"))
        self.label_5.setStatusTip(_translate("MainWindow", "Date (Specific Zone)"))
        self.label_5.setText(_translate("MainWindow", "Date (GMT + 5:30)"))
        self.Date_specific_search.setText(_translate("MainWindow", "--"))
        self.label.setStatusTip(_translate("MainWindow", "Country Name"))
        self.label.setText(_translate("MainWindow", "Country"))
        self.label_4.setStatusTip(_translate("MainWindow", "Date"))
        self.label_4.setText(_translate("MainWindow", "Date"))
        self.Date_search.setText(_translate("MainWindow", "--"))
        self.Slug_search.setText(_translate("MainWindow", "--"))
        self.data_tabs.setTabText(self.data_tabs.indexOf(self.country_dets_tab), _translate("MainWindow", "Country Details"))
        self.label_22.setStatusTip(_translate("MainWindow", "Total Confirmed Cases"))
        self.label_22.setText(_translate("MainWindow", "Total Confirmed"))
        self.newConfirmed_search.setText(_translate("MainWindow", "--"))
        self.totalConfirmed_search.setText(_translate("MainWindow", "--"))
        self.label_25.setStatusTip(_translate("MainWindow", "Recovery Percentage"))
        self.label_25.setText(_translate("MainWindow", "Recovery (in %)"))
        self.label_26.setStatusTip(_translate("MainWindow", "New Recovered Cases "))
        self.label_26.setText(_translate("MainWindow", "New Recovered"))
        self.Recovery_perc_search.setText(_translate("MainWindow", "--"))
        self.label_28.setStatusTip(_translate("MainWindow", "New Confirmed cases"))
        self.label_28.setText(_translate("MainWindow", "New Confirmed"))
        self.label_29.setStatusTip(_translate("MainWindow", "Total Recovered Cases"))
        self.label_29.setText(_translate("MainWindow", "Total Recovered"))
        self.totalRecovered_search.setText(_translate("MainWindow", "--"))
        self.newRecovered_search.setText(_translate("MainWindow", "--"))
        self.label_32.setStatusTip(_translate("MainWindow", "Recovery Rate in Percentage"))
        self.label_32.setText(_translate("MainWindow", "Recovery Rate (in %)"))
        self.Recovery_rate_search.setText(_translate("MainWindow", "--"))
        self.label_34.setStatusTip(_translate("MainWindow", "Total Deaths "))
        self.label_34.setText(_translate("MainWindow", "Total Deaths"))
        self.totalDeaths_search.setText(_translate("MainWindow", "--"))
        self.data_tabs.setTabText(self.data_tabs.indexOf(self.corona_stats_tab), _translate("MainWindow", "Corona Stats"))
        self.results_tab.setTabText(self.results_tab.indexOf(self.data_disp_tab), _translate("MainWindow", "Data"))
        self.search_res_list.setStatusTip(_translate("MainWindow", "Search Results"))
        self.results_tab.setTabText(self.results_tab.indexOf(self.search_res_tab), _translate("MainWindow", "Search Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOther.setTitle(_translate("MainWindow", "Other"))
        self.actionSave.setText(_translate("MainWindow", "Save "))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionHide_Menu.setText(_translate("MainWindow", "Hide Menu"))
        self.actionHide_Menu.setShortcut(_translate("MainWindow", "Ctrl+Shift+H"))
        self.initialize()
    def refresh_data(self):
        z = requests.request('GET',self.api)
        self.data = eval(z.text)

    def display_data_quick(self):
        
        #quick setup
        self.updateLabel(label_name=self.newConfirmed_quick,param=[self.quick_param,'NewConfirmed'])
        self.Date_specific_quick.setText(self.time_specific_cal(self.data[self.quick_param]['Date']))
        self.Date_specific_quick.adjustSize()
        self.Date_quick.setText(self.time_specific_cal(self.data[self.quick_param]['Date'],gmt_val=[0,0,0]))
        self.Date_quick.adjustSize()
        self.updateLabel(label_name=self.totalConfirmed_quick,param=[self.quick_param,'TotalConfirmed'])
        self.updateLabel(label_name=self.newRecovered_quick,param=[self.quick_param,'NewRecovered'])
        self.updateLabel(label_name=self.totalDeaths_quick,param=[self.quick_param,'TotalDeaths'])
        self.updateLabel(label_name=self.totalRecovered_quick,param=[self.quick_param,'TotalRecovered'])
        if 'CountryCode' in self.data[self.quick_param]:
                self.updateLabel(label_name=self.Country_name_quick,param=[self.quick_param,'Country'])
                self.updateLabel(label_name=self.Country_code_quick,param=[self.quick_param,'CountryCode'])
                self.updateLabel(label_name=self.Slug_quick,param=[self.quick_param,'Slug'])

    def time_specific_cal(self,abs_time,gmt_val=[5,30,0],add=True):
            date = abs_time[:abs_time.find('T')]
            time = abs_time[abs_time.find('T') + 1:]
            #time == 11:11:11 ex:- ,  gmt_val == [hrs , min , sec]
            time_hrs = int(time[:2])
            time_min = int(time[2 + 1 : 5])
            time_sec = int(float(time[5 + 1:-1]))
            time_hrs += gmt_val[0]
            time_min += gmt_val[1]
            time_sec += gmt_val[2]
            while time_hrs >= 24:
                    time_hrs -= 24
            while time_min >= 60:
                    time_min -= 60
            while time_sec >= 60:
                    time_sec -= 60
            time = date + ' ' + str(time_hrs) + ':' + str(time_min) + ':' + str(time_sec)
            return time

    def updateLabel(self,label_name,param):
            label_name.setText(str(self.data[param[0]][param[1]]))
            label_name.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
    	QLabel{
    		color:#101010;
    	}
    	QWidget{
    		color:#101010;
    	}
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
