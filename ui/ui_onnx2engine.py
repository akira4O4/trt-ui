# Form implementation generated from reading ui file 'D:\llf\code\export-ui\ui\ui_onnx2engine.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets, QtWidgets


class Ui_ONNX2Engine(object):
    def setupUi(self, ONNX2Engine):
        ONNX2Engine.setObjectName("ONNX2Engine")
        ONNX2Engine.resize(800, 400)
        self.centralwidget = QtWidgets.QWidget(parent=ONNX2Engine)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_config = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_config.setObjectName("groupBox_config")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_config)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_onnx_input = QtWidgets.QPushButton(parent=self.groupBox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_onnx_input.sizePolicy().hasHeightForWidth())
        self.pushButton_onnx_input.setSizePolicy(sizePolicy)
        self.pushButton_onnx_input.setObjectName("pushButton_onnx_input")
        self.gridLayout.addWidget(self.pushButton_onnx_input, 0, 1, 1, 1)
        self.lineEdit_output = QtWidgets.QLineEdit(parent=self.groupBox_config)
        self.lineEdit_output.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_output.sizePolicy().hasHeightForWidth())
        self.lineEdit_output.setSizePolicy(sizePolicy)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.gridLayout.addWidget(self.lineEdit_output, 1, 0, 1, 1)
        self.pushButton_input_config = QtWidgets.QPushButton(parent=self.groupBox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_input_config.sizePolicy().hasHeightForWidth())
        self.pushButton_input_config.setSizePolicy(sizePolicy)
        self.pushButton_input_config.setObjectName("pushButton_input_config")
        self.gridLayout.addWidget(self.pushButton_input_config, 2, 1, 1, 1)
        self.lineEdit_input_config = QtWidgets.QLineEdit(parent=self.groupBox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_input_config.sizePolicy().hasHeightForWidth())
        self.lineEdit_input_config.setSizePolicy(sizePolicy)
        self.lineEdit_input_config.setObjectName("lineEdit_input_config")
        self.gridLayout.addWidget(self.lineEdit_input_config, 2, 0, 1, 1)
        self.pushButton_output = QtWidgets.QPushButton(parent=self.groupBox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_output.sizePolicy().hasHeightForWidth())
        self.pushButton_output.setSizePolicy(sizePolicy)
        self.pushButton_output.setObjectName("pushButton_output")
        self.gridLayout.addWidget(self.pushButton_output, 1, 1, 1, 1)
        self.lineEdit_onnx_input = QtWidgets.QLineEdit(parent=self.groupBox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_onnx_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_onnx_input.setSizePolicy(sizePolicy)
        self.lineEdit_onnx_input.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_onnx_input.setObjectName("lineEdit_onnx_input")
        self.gridLayout.addWidget(self.lineEdit_onnx_input, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.verticalLayout_5.addWidget(self.groupBox_config)
        self.groupBox_workspace = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_workspace.setObjectName("groupBox_workspace")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_workspace)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSlider_workspace = QtWidgets.QSlider(parent=self.groupBox_workspace)
        self.horizontalSlider_workspace.setMinimum(1)
        self.horizontalSlider_workspace.setMaximum(12)
        self.horizontalSlider_workspace.setSingleStep(1)
        self.horizontalSlider_workspace.setProperty("value", 2)
        self.horizontalSlider_workspace.setTracking(True)
        self.horizontalSlider_workspace.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_workspace.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.horizontalSlider_workspace.setTickInterval(1)
        self.horizontalSlider_workspace.setObjectName("horizontalSlider_workspace")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_workspace)
        self.label_workspace_number = QtWidgets.QLabel(parent=self.groupBox_workspace)
        self.label_workspace_number.setObjectName("label_workspace_number")
        self.horizontalLayout_2.addWidget(self.label_workspace_number)
        self.label_workspace_gb = QtWidgets.QLabel(parent=self.groupBox_workspace)
        self.label_workspace_gb.setObjectName("label_workspace_gb")
        self.horizontalLayout_2.addWidget(self.label_workspace_gb)
        self.verticalLayout_5.addWidget(self.groupBox_workspace)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_datatype = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_datatype.setObjectName("groupBox_datatype")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_datatype)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_fp32 = QtWidgets.QRadioButton(parent=self.groupBox_datatype)
        self.radioButton_fp32.setChecked(True)
        self.radioButton_fp32.setObjectName("radioButton_fp32")
        self.verticalLayout.addWidget(self.radioButton_fp32)
        self.radioButton_fp16 = QtWidgets.QRadioButton(parent=self.groupBox_datatype)
        self.radioButton_fp16.setObjectName("radioButton_fp16")
        self.verticalLayout.addWidget(self.radioButton_fp16)
        self.horizontalLayout_3.addWidget(self.groupBox_datatype)
        self.groupBox_model_info = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_model_info.setObjectName("groupBox_model_info")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_model_info)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_model_type = QtWidgets.QLabel(parent=self.groupBox_model_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_model_type.sizePolicy().hasHeightForWidth())
        self.label_model_type.setSizePolicy(sizePolicy)
        self.label_model_type.setObjectName("label_model_type")
        self.verticalLayout_3.addWidget(self.label_model_type)
        self.label_min_shape = QtWidgets.QLabel(parent=self.groupBox_model_info)
        self.label_min_shape.setObjectName("label_min_shape")
        self.verticalLayout_3.addWidget(self.label_min_shape)
        self.label_max_shape = QtWidgets.QLabel(parent=self.groupBox_model_info)
        self.label_max_shape.setObjectName("label_max_shape")
        self.verticalLayout_3.addWidget(self.label_max_shape)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_model_type = QtWidgets.QLineEdit(parent=self.groupBox_model_info)
        self.lineEdit_model_type.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_model_type.sizePolicy().hasHeightForWidth())
        self.lineEdit_model_type.setSizePolicy(sizePolicy)
        self.lineEdit_model_type.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_model_type.setReadOnly(True)
        self.lineEdit_model_type.setPlaceholderText("")
        self.lineEdit_model_type.setObjectName("lineEdit_model_type")
        self.verticalLayout_4.addWidget(self.lineEdit_model_type)
        self.lineEdit_min_shape = QtWidgets.QLineEdit(parent=self.groupBox_model_info)
        self.lineEdit_min_shape.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_min_shape.sizePolicy().hasHeightForWidth())
        self.lineEdit_min_shape.setSizePolicy(sizePolicy)
        self.lineEdit_min_shape.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_min_shape.setReadOnly(True)
        self.lineEdit_min_shape.setPlaceholderText("")
        self.lineEdit_min_shape.setObjectName("lineEdit_min_shape")
        self.verticalLayout_4.addWidget(self.lineEdit_min_shape)
        self.lineEdit_max_shape = QtWidgets.QLineEdit(parent=self.groupBox_model_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_max_shape.sizePolicy().hasHeightForWidth())
        self.lineEdit_max_shape.setSizePolicy(sizePolicy)
        self.lineEdit_max_shape.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_max_shape.setPlaceholderText("")
        self.lineEdit_max_shape.setObjectName("lineEdit_max_shape")
        self.verticalLayout_4.addWidget(self.lineEdit_max_shape)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addWidget(self.groupBox_model_info)
        self.groupBox_btn = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_btn.setObjectName("groupBox_btn")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_btn)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_analysis_onnx = QtWidgets.QPushButton(parent=self.groupBox_btn)
        self.pushButton_analysis_onnx.setObjectName("pushButton_analysis_onnx")
        self.verticalLayout_2.addWidget(self.pushButton_analysis_onnx)
        self.pushButton_export_config = QtWidgets.QPushButton(parent=self.groupBox_btn)
        self.pushButton_export_config.setObjectName("pushButton_export_config")
        self.verticalLayout_2.addWidget(self.pushButton_export_config)
        self.pushButton_run = QtWidgets.QPushButton(parent=self.groupBox_btn)
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout_2.addWidget(self.pushButton_run)
        self.horizontalLayout_3.addWidget(self.groupBox_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textEdit_onnx_info = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEdit_onnx_info.setEnabled(True)
        self.textEdit_onnx_info.setReadOnly(True)
        self.textEdit_onnx_info.setObjectName("textEdit_onnx_info")
        self.verticalLayout_8.addWidget(self.textEdit_onnx_info)
        self.horizontalLayout_4.addWidget(self.groupBox)
        ONNX2Engine.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ONNX2Engine)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(parent=self.menubar)
        self.menu_help.setObjectName("menu_help")
        ONNX2Engine.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ONNX2Engine)
        self.statusbar.setObjectName("statusbar")
        ONNX2Engine.setStatusBar(self.statusbar)
        self.action_chinese = QtWidgets.QAction(parent=ONNX2Engine)
        self.action_chinese.setObjectName("action_chinese")
        self.action_english = QtWidgets.QAction(parent=ONNX2Engine)
        self.action_english.setObjectName("action_english")
        self.action_github = QtWidgets.QAction(parent=ONNX2Engine)
        self.action_github.setObjectName("action_github")
        self.action_gitee = QtWidgets.QAction(parent=ONNX2Engine)
        self.action_gitee.setObjectName("action_gitee")
        self.menu_help.addAction(self.action_github)
        self.menu_help.addAction(self.action_gitee)
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(ONNX2Engine)
        QtCore.QMetaObject.connectSlotsByName(ONNX2Engine)

    def retranslateUi(self, ONNX2Engine):
        _translate = QtCore.QCoreApplication.translate
        ONNX2Engine.setWindowTitle(_translate("ONNX2Engine", "TRT Export"))
        self.groupBox_config.setTitle(_translate("ONNX2Engine", "Config"))
        self.pushButton_onnx_input.setText(_translate("ONNX2Engine", "Select ONNX"))
        self.lineEdit_output.setPlaceholderText(_translate("ONNX2Engine", "/home/data/model.engine"))
        self.pushButton_input_config.setText(_translate("ONNX2Engine", "Import Config"))
        self.lineEdit_input_config.setPlaceholderText(_translate("ONNX2Engine", "/home/data/config.json [Option]"))
        self.pushButton_output.setText(_translate("ONNX2Engine", "Select Output"))
        self.lineEdit_onnx_input.setPlaceholderText(_translate("ONNX2Engine", "/home/data/model.onnx"))
        self.groupBox_workspace.setTitle(_translate("ONNX2Engine", "Workspace"))
        self.label_workspace_number.setText(_translate("ONNX2Engine", "0"))
        self.label_workspace_gb.setText(_translate("ONNX2Engine", "GB"))
        self.groupBox_datatype.setTitle(_translate("ONNX2Engine", "DataType"))
        self.radioButton_fp32.setText(_translate("ONNX2Engine", "FP32"))
        self.radioButton_fp16.setText(_translate("ONNX2Engine", "FP16"))
        self.groupBox_model_info.setTitle(_translate("ONNX2Engine", "Engine Export Setting"))
        self.label_model_type.setText(_translate("ONNX2Engine", "Model Type:"))
        self.label_min_shape.setText(_translate("ONNX2Engine", "Min Input Shape:"))
        self.label_max_shape.setText(_translate("ONNX2Engine", "Max Input Shape:"))
        self.lineEdit_model_type.setText(_translate("ONNX2Engine", "Static"))
        self.groupBox_btn.setTitle(_translate("ONNX2Engine", "Start"))
        self.pushButton_analysis_onnx.setText(_translate("ONNX2Engine", "Analysis ONNX"))
        self.pushButton_export_config.setText(_translate("ONNX2Engine", "Export Config"))
        self.pushButton_run.setText(_translate("ONNX2Engine", "Run"))
        self.groupBox.setTitle(_translate("ONNX2Engine", "ONNX Info"))
        self.textEdit_onnx_info.setHtml(_translate("ONNX2Engine", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">Inputs:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">    name:    image</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">    type:    FP32</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">    shape:    [N,C,H,W]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#8d8d8d;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#8d8d8d;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">Output:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">    name:    output</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">    type:    FP32</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#8d8d8d;\">    shape:    [N,C,H,W]</span></p></body></html>"))
        self.menu_help.setTitle(_translate("ONNX2Engine", "Help"))
        self.action_chinese.setText(_translate("ONNX2Engine", "Chinese"))
        self.action_english.setText(_translate("ONNX2Engine", "English"))
        self.action_github.setText(_translate("ONNX2Engine", "Github"))
        self.action_gitee.setText(_translate("ONNX2Engine", "Gitee"))
