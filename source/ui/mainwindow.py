from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QSizePolicy, QLabel


class MainWindowUI:

    """Класс, описывающий UI главного окна приложения."""

    def setupUi(self, MainWindow):
        """Метод, создающий объекты виджета в соответствующих контейнерах окна MainWindow.

        Args:
            MainWindow:
                окно, тип QMainWindow.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1248, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTasks = QtWidgets.QMenu(self.menubar)
        self.menuTasks.setObjectName("menuTasks")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMouseTracking(False)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.ToolBarArea.AllToolBarAreas)
        self.toolBar.setObjectName("toolBar")
        self.spacer = QtWidgets.QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.toolBar.addWidget(self.spacer)
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        start_icon = QtGui.QIcon()
        start_disabled_icon = QtGui.QIcon()
        start_icon.addPixmap(QtGui.QPixmap('icons/start.png'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        start_disabled_icon.addPixmap(QtGui.QPixmap('icons/start_disabled.png'), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.actionStartParsing = QtGui.QAction(MainWindow)
        self.actionStartParsing.setIcon(start_icon)
        self.actionStartParsing.setObjectName("actionStartParsing")
        stop_icon = QtGui.QIcon()
        stop_disabled_icon = QtGui.QIcon()
        stop_icon.addPixmap(QtGui.QPixmap('icons/stop.png'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        stop_disabled_icon.addPixmap(QtGui.QPixmap('icons/stop_disabled.png'), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.actionStopParsing = QtGui.QAction(MainWindow)
        self.actionStopParsing.setIcon(stop_icon)
        self.actionStopParsing.setEnabled(False)
        self.actionStopParsing.setObjectName("actionStopParsing")
        self.actionOpenSettings = QtGui.QAction(MainWindow)
        settings_icon = QtGui.QIcon()
        settings_icon.addPixmap(QtGui.QPixmap('icons/settings.png'), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actionOpenSettings.setIcon(settings_icon)
        self.actionOpenSettings.setObjectName("actionOpenSettings")
        self.toolBar.addAction(self.actionStartParsing)
        self.toolBar.addAction(self.actionStopParsing)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOpenSettings)
        self.actionOpenFile = QtGui.QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionOpenParsingWizard = QtGui.QAction(MainWindow)
        self.actionOpenParsingWizard.setObjectName("actionOpenParsingWizard")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionShowTasks = QtGui.QAction(MainWindow)
        self.actionShowTasks.setObjectName("actionShowTasks")
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())
        self.menuTasks.addAction(self.actionShowTasks)
        self.movie = QtGui.QMovie('icons/loading_logo.gif')
        self.label = QLabel()
        self.label.setMovie(self.movie)
        self.verticalLayout.addWidget(self.label)
        self.label.setEnabled(False)
        self.tableWidget.setVisible(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Метод, устанавливающий текст и заголовки виджетов."""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parser"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTasks.setTitle(_translate("MainWindow", "Tasks"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionStartParsing.setText(_translate("MainWindow", "Start Parsing"))
        self.actionStopParsing.setText(_translate("MainWindow", "Stop Parsing"))
        self.actionOpenSettings.setText(_translate("MainWindow", "Open Settings"))
        self.actionOpenSettings.setToolTip(_translate("MainWindow", "Open Settings"))
        self.actionOpenSettings.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.actionOpenFile.setText(_translate("MainWindow", "Open"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionShowTasks.setText(_translate("MainWindow", "Manage parsing tasks"))
        self.actionShowTasks.setToolTip(_translate("MainWindow", "Manage parsing tasks"))
