# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/ui/appliance_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ApplianceWizard(object):
    def setupUi(self, ApplianceWizard):
        ApplianceWizard.setObjectName("ApplianceWizard")
        ApplianceWizard.resize(688, 469)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ApplianceWizard.sizePolicy().hasHeightForWidth())
        ApplianceWizard.setSizePolicy(sizePolicy)
        ApplianceWizard.setMaximumSize(QtCore.QSize(688, 469))
        ApplianceWizard.setModal(True)
        ApplianceWizard.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        ApplianceWizard.setOptions(QtWidgets.QWizard.NoBackButtonOnStartPage)
        self.uiInfoWizardPage = QtWidgets.QWizardPage()
        self.uiInfoWizardPage.setSubTitle("")
        self.uiInfoWizardPage.setObjectName("uiInfoWizardPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiInfoWizardPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiInfoTreeWidget = QtWidgets.QTreeWidget(self.uiInfoWizardPage)
        self.uiInfoTreeWidget.setAlternatingRowColors(False)
        self.uiInfoTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.uiInfoTreeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.uiInfoTreeWidget.setRootIsDecorated(False)
        self.uiInfoTreeWidget.setWordWrap(False)
        self.uiInfoTreeWidget.setHeaderHidden(True)
        self.uiInfoTreeWidget.setObjectName("uiInfoTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiInfoTreeWidget)
        self.uiInfoTreeWidget.header().setVisible(False)
        self.gridLayout_4.addWidget(self.uiInfoTreeWidget, 1, 0, 1, 1)
        self.uiDescriptionLabel = QtWidgets.QLabel(self.uiInfoWizardPage)
        self.uiDescriptionLabel.setWordWrap(True)
        self.uiDescriptionLabel.setObjectName("uiDescriptionLabel")
        self.gridLayout_4.addWidget(self.uiDescriptionLabel, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiInfoWizardPage)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiServerWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.uiServerWizardPage)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiServerTypeGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.horizontalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiVMRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiVMRadioButton.setObjectName("uiVMRadioButton")
        self.horizontalLayout.addWidget(self.uiVMRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.horizontalLayout.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.uiServerTypeGroupBox)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiLoadBalanceCheckBox = QtWidgets.QCheckBox(self.uiRemoteServersGroupBox)
        self.uiLoadBalanceCheckBox.setChecked(True)
        self.uiLoadBalanceCheckBox.setObjectName("uiLoadBalanceCheckBox")
        self.gridLayout_7.addWidget(self.uiLoadBalanceCheckBox, 0, 0, 1, 2)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 1, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiRemoteServersGroupBox)
        ApplianceWizard.addPage(self.uiServerWizardPage)
        self.uiFilesWizardPage = QtWidgets.QWizardPage()
        self.uiFilesWizardPage.setObjectName("uiFilesWizardPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiFilesWizardPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiApplianceVersionTreeWidget = QtWidgets.QTreeWidget(self.uiFilesWizardPage)
        self.uiApplianceVersionTreeWidget.setIndentation(20)
        self.uiApplianceVersionTreeWidget.setObjectName("uiApplianceVersionTreeWidget")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.uiApplianceVersionTreeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiApplianceVersionTreeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiApplianceVersionTreeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiApplianceVersionTreeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.uiApplianceVersionTreeWidget.header().setDefaultSectionSize(120)
        self.uiApplianceVersionTreeWidget.header().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.uiApplianceVersionTreeWidget)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.uiImportPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiImportPushButton.setObjectName("uiImportPushButton")
        self.horizontalLayout1.addWidget(self.uiImportPushButton)
        self.uiDownloadPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiDownloadPushButton.setObjectName("uiDownloadPushButton")
        self.horizontalLayout1.addWidget(self.uiDownloadPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(spacerItem1)
        self.uiRefreshPushButton = QtWidgets.QPushButton(self.uiFilesWizardPage)
        self.uiRefreshPushButton.setObjectName("uiRefreshPushButton")
        self.horizontalLayout1.addWidget(self.uiRefreshPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        ApplianceWizard.addPage(self.uiFilesWizardPage)
        self.uiSummaryWizardPage = QtWidgets.QWizardPage()
        self.uiSummaryWizardPage.setObjectName("uiSummaryWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiSummaryWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiSummaryTreeWidget = QtWidgets.QTreeWidget(self.uiSummaryWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSummaryTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiSummaryTreeWidget.setSizePolicy(sizePolicy)
        self.uiSummaryTreeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.uiSummaryTreeWidget.setAlternatingRowColors(False)
        self.uiSummaryTreeWidget.setRootIsDecorated(False)
        self.uiSummaryTreeWidget.setUniformRowHeights(False)
        self.uiSummaryTreeWidget.setItemsExpandable(False)
        self.uiSummaryTreeWidget.setAnimated(False)
        self.uiSummaryTreeWidget.setAllColumnsShowFocus(False)
        self.uiSummaryTreeWidget.setWordWrap(False)
        self.uiSummaryTreeWidget.setHeaderHidden(True)
        self.uiSummaryTreeWidget.setColumnCount(2)
        self.uiSummaryTreeWidget.setObjectName("uiSummaryTreeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiSummaryTreeWidget)
        self.uiSummaryTreeWidget.header().setDefaultSectionSize(150)
        self.uiSummaryTreeWidget.header().setMinimumSectionSize(20)
        self.uiSummaryTreeWidget.header().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.uiSummaryTreeWidget, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiSummaryWizardPage)
        self.uiUsageWizardPage = QtWidgets.QWizardPage()
        self.uiUsageWizardPage.setObjectName("uiUsageWizardPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiUsageWizardPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiUsageTextEdit = QtWidgets.QTextEdit(self.uiUsageWizardPage)
        self.uiUsageTextEdit.setObjectName("uiUsageTextEdit")
        self.gridLayout_3.addWidget(self.uiUsageTextEdit, 0, 0, 1, 1)
        ApplianceWizard.addPage(self.uiUsageWizardPage)

        self.retranslateUi(ApplianceWizard)
        QtCore.QMetaObject.connectSlotsByName(ApplianceWizard)

    def retranslateUi(self, ApplianceWizard):
        _translate = QtCore.QCoreApplication.translate
        ApplianceWizard.setWindowTitle(_translate("ApplianceWizard", "Add appliance"))
        self.uiInfoWizardPage.setTitle(_translate("ApplianceWizard", "Cisco NX-OSv"))
        self.uiInfoTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "1"))
        self.uiInfoTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "2"))
        __sortingEnabled = self.uiInfoTreeWidget.isSortingEnabled()
        self.uiInfoTreeWidget.setSortingEnabled(False)
        self.uiInfoTreeWidget.topLevelItem(0).setText(0, _translate("ApplianceWizard", "Category:"))
        self.uiInfoTreeWidget.topLevelItem(0).setText(1, _translate("ApplianceWizard", "router"))
        self.uiInfoTreeWidget.topLevelItem(1).setText(0, _translate("ApplianceWizard", "Product:"))
        self.uiInfoTreeWidget.topLevelItem(1).setText(1, _translate("ApplianceWizard", "NX-OSv"))
        self.uiInfoTreeWidget.topLevelItem(2).setText(0, _translate("ApplianceWizard", "Vendor:"))
        self.uiInfoTreeWidget.topLevelItem(2).setText(1, _translate("ApplianceWizard", "Cisco"))
        self.uiInfoTreeWidget.topLevelItem(3).setText(0, _translate("ApplianceWizard", "Status:"))
        self.uiInfoTreeWidget.topLevelItem(3).setText(1, _translate("ApplianceWizard", "stable"))
        self.uiInfoTreeWidget.topLevelItem(4).setText(0, _translate("ApplianceWizard", "Maintainer:"))
        self.uiInfoTreeWidget.topLevelItem(4).setText(1, _translate("ApplianceWizard", "The GNS3 team"))
        self.uiInfoTreeWidget.setSortingEnabled(__sortingEnabled)
        self.uiDescriptionLabel.setText(_translate("ApplianceWizard", "NX-OSv is a reference platform for an implementation of the Cisco Nexus operating system, based on the Nexus 7000-series platforms, running as a full virtual machine on a hypervisor."))
        self.uiServerWizardPage.setTitle(_translate("ApplianceWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("ApplianceWizard", "Please choose a server type to run your new Appliance."))
        self.label.setText(_translate("ApplianceWizard", "On Windows and OSX the local server is not supported. Please use the GNS3 VM."))
        self.uiServerTypeGroupBox.setTitle(_translate("ApplianceWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("ApplianceWizard", "Remote"))
        self.uiVMRadioButton.setText(_translate("ApplianceWizard", "GNS3 VM"))
        self.uiLocalRadioButton.setText(_translate("ApplianceWizard", "Local"))
        self.uiRemoteServersGroupBox.setTitle(_translate("ApplianceWizard", "Remote servers"))
        self.uiLoadBalanceCheckBox.setText(_translate("ApplianceWizard", "Load balance across all available remote servers"))
        self.uiRemoteServersLabel.setText(_translate("ApplianceWizard", "Run on server:"))
        self.uiFilesWizardPage.setTitle(_translate("ApplianceWizard", "Required files"))
        self.uiFilesWizardPage.setSubTitle(_translate("ApplianceWizard", "The following files are required to install NX-OS"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "Appliance version"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "Filename"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(2, _translate("ApplianceWizard", "Size"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(3, _translate("ApplianceWizard", "Status"))
        self.uiApplianceVersionTreeWidget.headerItem().setText(4, _translate("ApplianceWizard", "Version"))
        __sortingEnabled = self.uiApplianceVersionTreeWidget.isSortingEnabled()
        self.uiApplianceVersionTreeWidget.setSortingEnabled(False)
        self.uiApplianceVersionTreeWidget.topLevelItem(0).setText(0, _translate("ApplianceWizard", "7.2.0.121"))
        self.uiApplianceVersionTreeWidget.topLevelItem(0).setText(3, _translate("ApplianceWizard", "Missing"))
        self.uiApplianceVersionTreeWidget.topLevelItem(0).child(0).setText(1, _translate("ApplianceWizard", "NXOS-V7.2.0.121.bin"))
        self.uiApplianceVersionTreeWidget.topLevelItem(0).child(0).setText(2, _translate("ApplianceWizard", "345MB"))
        self.uiApplianceVersionTreeWidget.topLevelItem(0).child(0).setText(3, _translate("ApplianceWizard", "Missing"))
        self.uiApplianceVersionTreeWidget.topLevelItem(0).child(0).setText(4, _translate("ApplianceWizard", "7.2.0.121"))
        self.uiApplianceVersionTreeWidget.topLevelItem(1).setText(0, _translate("ApplianceWizard", "7.3.0.42"))
        self.uiApplianceVersionTreeWidget.topLevelItem(1).setText(3, _translate("ApplianceWizard", "Missing"))
        self.uiApplianceVersionTreeWidget.topLevelItem(1).child(0).setText(1, _translate("ApplianceWizard", "NXOS-V7.3.0.121.bin"))
        self.uiApplianceVersionTreeWidget.topLevelItem(1).child(0).setText(2, _translate("ApplianceWizard", "356MB"))
        self.uiApplianceVersionTreeWidget.topLevelItem(1).child(0).setText(3, _translate("ApplianceWizard", "Missing"))
        self.uiApplianceVersionTreeWidget.topLevelItem(1).child(0).setText(4, _translate("ApplianceWizard", "7.3.0.42"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).setText(0, _translate("ApplianceWizard", "8.0"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).setText(3, _translate("ApplianceWizard", "Available"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(0).setText(1, _translate("ApplianceWizard", "NX-diskA"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(0).setText(2, _translate("ApplianceWizard", "12MB"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(0).setText(3, _translate("ApplianceWizard", "Available"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(0).setText(4, _translate("ApplianceWizard", "8.0"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(1).setText(1, _translate("ApplianceWizard", "NX-diskB"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(1).setText(2, _translate("ApplianceWizard", "400MB"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(1).setText(3, _translate("ApplianceWizard", "Available"))
        self.uiApplianceVersionTreeWidget.topLevelItem(2).child(1).setText(4, _translate("ApplianceWizard", "8.0"))
        self.uiApplianceVersionTreeWidget.setSortingEnabled(__sortingEnabled)
        self.uiImportPushButton.setText(_translate("ApplianceWizard", "&Import"))
        self.uiDownloadPushButton.setText(_translate("ApplianceWizard", "&Download"))
        self.uiRefreshPushButton.setText(_translate("ApplianceWizard", "Refresh"))
        self.uiSummaryWizardPage.setTitle(_translate("ApplianceWizard", "Summary"))
        self.uiSummaryWizardPage.setSubTitle(_translate("ApplianceWizard", "The following settings are going to be used."))
        self.uiSummaryTreeWidget.headerItem().setText(0, _translate("ApplianceWizard", "1"))
        self.uiSummaryTreeWidget.headerItem().setText(1, _translate("ApplianceWizard", "2"))
        __sortingEnabled = self.uiSummaryTreeWidget.isSortingEnabled()
        self.uiSummaryTreeWidget.setSortingEnabled(False)
        self.uiSummaryTreeWidget.topLevelItem(0).setText(0, _translate("ApplianceWizard", "adapter_type"))
        self.uiSummaryTreeWidget.topLevelItem(0).setText(1, _translate("ApplianceWizard", "e1000"))
        self.uiSummaryTreeWidget.topLevelItem(1).setText(0, _translate("ApplianceWizard", "console_type"))
        self.uiSummaryTreeWidget.topLevelItem(1).setText(1, _translate("ApplianceWizard", "telnet"))
        self.uiSummaryTreeWidget.topLevelItem(2).setText(0, _translate("ApplianceWizard", "ram"))
        self.uiSummaryTreeWidget.topLevelItem(2).setText(1, _translate("ApplianceWizard", "3072"))
        self.uiSummaryTreeWidget.topLevelItem(3).setText(0, _translate("ApplianceWizard", "arch"))
        self.uiSummaryTreeWidget.topLevelItem(3).setText(1, _translate("ApplianceWizard", "x68_64"))
        self.uiSummaryTreeWidget.topLevelItem(4).setText(0, _translate("ApplianceWizard", "adapters"))
        self.uiSummaryTreeWidget.topLevelItem(4).setText(1, _translate("ApplianceWizard", "16"))
        self.uiSummaryTreeWidget.topLevelItem(5).setText(0, _translate("ApplianceWizard", "kernel command line"))
        self.uiSummaryTreeWidget.topLevelItem(5).setText(1, _translate("ApplianceWizard", "user=gns3"))
        self.uiSummaryTreeWidget.setSortingEnabled(__sortingEnabled)
        self.uiUsageWizardPage.setTitle(_translate("ApplianceWizard", "Usage"))
        self.uiUsageWizardPage.setSubTitle(_translate("ApplianceWizard", "Please read the following instructions in order to use your new appliance."))
        self.uiUsageTextEdit.setHtml(_translate("ApplianceWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">The default username/password is admin/admin. A default configuration is present.</span></p></body></html>"))

from . import resources_rc
