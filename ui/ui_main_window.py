# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#Main{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"#Container{\n"
"	background-color: rgb(20, 20, 21);\n"
"}\n"
"\n"
"#header{\n"
"	background-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"#frame_search {\n"
"	border: 1px solid #747474;\n"
"	border-radius: 3px;\n"
"	background-color: rgb(49, 49, 49);\n"
"	margin-left: 10px;\n"
"}\n"
"\n"
"#frame_search:hover,\n"
"#frame_date:hover {\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"#frame_search:pressed {\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"#search_input {\n"
"    color: #fff;\n"
"	background-color: rgb(49, 49, 49);\n"
"	border: none;\n"
"	padding: 5px 10px;\n"
"}\n"
"\n"
"#btn_search{\n"
"	border:none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"#lbl_logo,\n"
"#lbl_description,\n"
"#lbl_excel_disponibles,\n"
"#lbl_file_sql{\n"
"	color: white;\n"
"}\n"
"\n"
"#btn_icon_logo{\n"
"	background-color: none;\n"
"	border: none;\n"
"}\n"
"\n"
"#card_file_sql,\n"
"#card_file_xls,\n"
"#content_right,\n"
"#footer{\n"
"	backgrou"
                        "nd-color: rgb(32, 32, 32);\n"
"}\n"
"\n"
"#btn_convert_sql{\n"
"	background-color: #0C7238;\n"
"	color: white;\n"
"	border: none;\n"
"}\n"
"#btn_convert_sql:hover{\n"
"	background-color: #129652;\n"
"	color: white;\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Container = QFrame(self.centralwidget)
        self.Container.setObjectName(u"Container")
        self.Container.setFrameShape(QFrame.Shape.StyledPanel)
        self.Container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Container)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.Container)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 40))
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.lbl_description = QLabel(self.header)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        self.lbl_description.setFont(font)

        self.horizontalLayout_9.addWidget(self.lbl_description)

        self.btn_sidebar = QPushButton(self.header)
        self.btn_sidebar.setObjectName(u"btn_sidebar")
        self.btn_sidebar.setMinimumSize(QSize(30, 30))
        self.btn_sidebar.setMaximumSize(QSize(30, 30))
        self.btn_sidebar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sidebar.setStyleSheet(u"#btn_sidebar{\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"\n"
"#btn_sidebar:hover{\n"
"	background-color: rgb(62, 62, 62);\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/assets/icons/white/side_navigation_left_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sidebar.setIcon(icon)
        self.btn_sidebar.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.btn_sidebar)

        self.horizontalSpacer_ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_)

        self.btn_icon_logo = QPushButton(self.header)
        self.btn_icon_logo.setObjectName(u"btn_icon_logo")
        self.btn_icon_logo.setMinimumSize(QSize(36, 36))
        self.btn_icon_logo.setMaximumSize(QSize(36, 36))
        icon1 = QIcon()
        icon1.addFile(u":/icon/assets/icons/black/icon-excel.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_icon_logo.setIcon(icon1)
        self.btn_icon_logo.setIconSize(QSize(36, 36))

        self.horizontalLayout_9.addWidget(self.btn_icon_logo)

        self.lbl_logo = QLabel(self.header)
        self.lbl_logo.setObjectName(u"lbl_logo")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_logo.setFont(font1)

        self.horizontalLayout_9.addWidget(self.lbl_logo)


        self.verticalLayout_11.addWidget(self.header)

        self.body = QFrame(self.Container)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.Shape.StyledPanel)
        self.body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.body)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.content_light = QFrame(self.body)
        self.content_light.setObjectName(u"content_light")
        self.content_light.setMinimumSize(QSize(450, 0))
        self.content_light.setMaximumSize(QSize(450, 16777215))
        self.content_light.setFrameShape(QFrame.Shape.StyledPanel)
        self.content_light.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.content_light)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.card_file_xls = QFrame(self.content_light)
        self.card_file_xls.setObjectName(u"card_file_xls")
        self.card_file_xls.setMinimumSize(QSize(0, 0))
        self.card_file_xls.setMaximumSize(QSize(16777215, 300))
        self.card_file_xls.setFrameShape(QFrame.Shape.StyledPanel)
        self.card_file_xls.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.card_file_xls)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.file_xls_header = QFrame(self.card_file_xls)
        self.file_xls_header.setObjectName(u"file_xls_header")
        self.file_xls_header.setMinimumSize(QSize(0, 30))
        self.file_xls_header.setMaximumSize(QSize(16777215, 30))
        self.file_xls_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_xls_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.file_xls_header)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.lbl_excel_disponibles = QLabel(self.file_xls_header)
        self.lbl_excel_disponibles.setObjectName(u"lbl_excel_disponibles")
        self.lbl_excel_disponibles.setFont(font)

        self.horizontalLayout_11.addWidget(self.lbl_excel_disponibles)


        self.verticalLayout_13.addWidget(self.file_xls_header)

        self.file_xls_body = QFrame(self.card_file_xls)
        self.file_xls_body.setObjectName(u"file_xls_body")
        self.file_xls_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_xls_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.file_xls_body)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.listWidget_file_xls = QListWidget(self.file_xls_body)
        self.listWidget_file_xls.setObjectName(u"listWidget_file_xls")
        self.listWidget_file_xls.setMinimumSize(QSize(0, 0))
        self.listWidget_file_xls.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_14.addWidget(self.listWidget_file_xls)


        self.verticalLayout_13.addWidget(self.file_xls_body)

        self.file_xls_footer = QFrame(self.card_file_xls)
        self.file_xls_footer.setObjectName(u"file_xls_footer")
        self.file_xls_footer.setMinimumSize(QSize(0, 40))
        self.file_xls_footer.setMaximumSize(QSize(16777215, 40))
        self.file_xls_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_xls_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.file_xls_footer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.btn_delete_file = QPushButton(self.file_xls_footer)
        self.btn_delete_file.setObjectName(u"btn_delete_file")
        self.btn_delete_file.setMinimumSize(QSize(33, 33))
        self.btn_delete_file.setMaximumSize(QSize(33, 33))
        self.btn_delete_file.setStyleSheet(u"#btn_delete_file{\n"
"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"#btn_delete_file:hover{\n"
"background-color: rgb(238, 40, 5);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/assets/icons/white/scan_delete_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete_file.setIcon(icon2)
        self.btn_delete_file.setIconSize(QSize(30, 30))

        self.horizontalLayout_12.addWidget(self.btn_delete_file)

        self.btn_upload = QPushButton(self.file_xls_footer)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setMinimumSize(QSize(130, 33))
        self.btn_upload.setMaximumSize(QSize(130, 33))
        self.btn_upload.setStyleSheet(u"#btn_upload{\n"
"background-color: #0273fd;\n"
"color: white;\n"
"border: none;\n"
"}\n"
"\n"
"#btn_upload:hover{\n"
"background-color: #318af8;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/assets/icons/white/upload_file_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_upload.setIcon(icon3)
        self.btn_upload.setIconSize(QSize(30, 30))

        self.horizontalLayout_12.addWidget(self.btn_upload)

        self.btn_convert_sql = QPushButton(self.file_xls_footer)
        self.btn_convert_sql.setObjectName(u"btn_convert_sql")
        self.btn_convert_sql.setMinimumSize(QSize(130, 33))
        self.btn_convert_sql.setMaximumSize(QSize(130, 33))

        self.horizontalLayout_12.addWidget(self.btn_convert_sql)


        self.verticalLayout_13.addWidget(self.file_xls_footer)


        self.verticalLayout_12.addWidget(self.card_file_xls)

        self.card_file_sql = QFrame(self.content_light)
        self.card_file_sql.setObjectName(u"card_file_sql")
        self.card_file_sql.setMinimumSize(QSize(0, 0))
        self.card_file_sql.setMaximumSize(QSize(16777215, 300))
        self.card_file_sql.setFrameShape(QFrame.Shape.StyledPanel)
        self.card_file_sql.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.card_file_sql)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 9)
        self.file_sql_header = QFrame(self.card_file_sql)
        self.file_sql_header.setObjectName(u"file_sql_header")
        self.file_sql_header.setMinimumSize(QSize(0, 30))
        self.file_sql_header.setMaximumSize(QSize(16777215, 30))
        self.file_sql_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_sql_header.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.file_sql_header)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.lbl_file_sql = QLabel(self.file_sql_header)
        self.lbl_file_sql.setObjectName(u"lbl_file_sql")
        self.lbl_file_sql.setFont(font)

        self.verticalLayout_16.addWidget(self.lbl_file_sql)


        self.verticalLayout_15.addWidget(self.file_sql_header)

        self.file_sql_body = QFrame(self.card_file_sql)
        self.file_sql_body.setObjectName(u"file_sql_body")
        self.file_sql_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_sql_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.file_sql_body)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.listWidget_sql = QListWidget(self.file_sql_body)
        self.listWidget_sql.setObjectName(u"listWidget_sql")

        self.verticalLayout_17.addWidget(self.listWidget_sql)


        self.verticalLayout_15.addWidget(self.file_sql_body)

        self.file_sql_footer = QFrame(self.card_file_sql)
        self.file_sql_footer.setObjectName(u"file_sql_footer")
        self.file_sql_footer.setMinimumSize(QSize(0, 40))
        self.file_sql_footer.setMaximumSize(QSize(16777215, 40))
        self.file_sql_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.file_sql_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.file_sql_footer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.btn_load_sql = QPushButton(self.file_sql_footer)
        self.btn_load_sql.setObjectName(u"btn_load_sql")
        self.btn_load_sql.setMinimumSize(QSize(130, 33))
        self.btn_load_sql.setMaximumSize(QSize(130, 33))
        font2 = QFont()
        font2.setBold(True)
        self.btn_load_sql.setFont(font2)
        self.btn_load_sql.setStyleSheet(u"#btn_load_sql{\n"
"background-color: #0273fd;\n"
"color: white;\n"
"border: none;\n"
"}\n"
"\n"
"#btn_load_sql:hover{\n"
"background-color: #318af8;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.btn_load_sql)


        self.verticalLayout_15.addWidget(self.file_sql_footer)


        self.verticalLayout_12.addWidget(self.card_file_sql)


        self.horizontalLayout_10.addWidget(self.content_light)

        self.content_right = QFrame(self.body)
        self.content_right.setObjectName(u"content_right")
        self.content_right.setMinimumSize(QSize(0, 0))
        self.content_right.setMaximumSize(QSize(800, 16777215))
        self.content_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.content_right.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.content_right)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_search = QFrame(self.content_right)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 33))
        self.frame_search.setMaximumSize(QSize(600, 33))
        self.frame_search.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.search_input = QLineEdit(self.frame_search)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(0, 23))
        self.search_input.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout_14.addWidget(self.search_input)

        self.btn_search = QPushButton(self.frame_search)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(33, 33))
        self.btn_search.setMaximumSize(QSize(33, 33))
        icon4 = QIcon()
        icon4.addFile(u":/icon/assets/icons/white/search-white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.btn_search)


        self.verticalLayout_18.addWidget(self.frame_search)

        self.view_data_body = QFrame(self.content_right)
        self.view_data_body.setObjectName(u"view_data_body")
        self.view_data_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_data_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.view_data_body)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tableView_data = QTableView(self.view_data_body)
        self.tableView_data.setObjectName(u"tableView_data")

        self.verticalLayout_19.addWidget(self.tableView_data)


        self.verticalLayout_18.addWidget(self.view_data_body)

        self.view_data_footer = QFrame(self.content_right)
        self.view_data_footer.setObjectName(u"view_data_footer")
        self.view_data_footer.setMinimumSize(QSize(0, 40))
        self.view_data_footer.setMaximumSize(QSize(16777215, 40))
        self.view_data_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.view_data_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.view_data_footer)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.btn_edit = QPushButton(self.view_data_footer)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMinimumSize(QSize(130, 33))
        self.btn_edit.setMaximumSize(QSize(130, 33))
        self.btn_edit.setFont(font2)
        self.btn_edit.setStyleSheet(u"#btn_edit{\n"
"background-color: #0273fd;\n"
"color: white;\n"
"border: none;\n"
"}\n"
"\n"
"#btn_edit:hover{\n"
"background-color: #318af8;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.btn_edit)


        self.verticalLayout_18.addWidget(self.view_data_footer)


        self.horizontalLayout_10.addWidget(self.content_right)


        self.verticalLayout_11.addWidget(self.body)

        self.footer = QFrame(self.Container)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 31))
        self.footer.setMaximumSize(QSize(16777215, 30))
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.footer)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_2)


        self.verticalLayout_11.addWidget(self.footer)


        self.verticalLayout.addWidget(self.Container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_description.setText(QCoreApplication.translate("MainWindow", u"Migrexel - Gestiona tus archivos Excel y trabajalos en Sqlite", None))
        self.btn_sidebar.setText("")
        self.btn_icon_logo.setText("")
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"DASH", None))
        self.lbl_excel_disponibles.setText(QCoreApplication.translate("MainWindow", u"Listar archivos Excel disponibles", None))
#if QT_CONFIG(tooltip)
        self.btn_delete_file.setToolTip(QCoreApplication.translate("MainWindow", u"Eliminar archivo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_delete_file.setText("")
#if QT_CONFIG(tooltip)
        self.btn_upload.setToolTip(QCoreApplication.translate("MainWindow", u"Cargar archivo Excel", None))
#endif // QT_CONFIG(tooltip)
        self.btn_upload.setText(QCoreApplication.translate("MainWindow", u"Cargar archivo", None))
        self.btn_convert_sql.setText(QCoreApplication.translate("MainWindow", u"Convertir en SQL", None))
        self.lbl_file_sql.setText(QCoreApplication.translate("MainWindow", u"Listar tablas en la base de datos", None))
        self.btn_load_sql.setText(QCoreApplication.translate("MainWindow", u"Cargar SQL", None))
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"buscar...", None))
        self.btn_search.setText("")
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Modificar ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Copyright (c) 2025 Adolfo Agust\u00edn Fern\u00e1ndez ", None))
    # retranslateUi

