# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/workspace/git/gns3-gui/gns3/modules/dynamips/ui/frame_relay_switch_configuration_page.ui'
#
# Created: Tue Jan 21 21:27:47 2014
#      by: PyQt4 UI code generator 4.10
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

class Ui_frameRelaySwitchConfigPageWidget(object):
    def setupUi(self, frameRelaySwitchConfigPageWidget):
        frameRelaySwitchConfigPageWidget.setObjectName(_fromUtf8("frameRelaySwitchConfigPageWidget"))
        frameRelaySwitchConfigPageWidget.resize(397, 314)
        self.gridlayout = QtGui.QGridLayout(frameRelaySwitchConfigPageWidget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.uiFrameRelaySourceGroupBox = QtGui.QGroupBox(frameRelaySwitchConfigPageWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiFrameRelaySourceGroupBox.sizePolicy().hasHeightForWidth())
        self.uiFrameRelaySourceGroupBox.setSizePolicy(sizePolicy)
        self.uiFrameRelaySourceGroupBox.setObjectName(_fromUtf8("uiFrameRelaySourceGroupBox"))
        self.gridlayout1 = QtGui.QGridLayout(self.uiFrameRelaySourceGroupBox)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.uiSourcePortLabel = QtGui.QLabel(self.uiFrameRelaySourceGroupBox)
        self.uiSourcePortLabel.setObjectName(_fromUtf8("uiSourcePortLabel"))
        self.gridlayout1.addWidget(self.uiSourcePortLabel, 0, 0, 1, 1)
        self.uiSourcePortSpinBox = QtGui.QSpinBox(self.uiFrameRelaySourceGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSourcePortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiSourcePortSpinBox.setSizePolicy(sizePolicy)
        self.uiSourcePortSpinBox.setMinimum(0)
        self.uiSourcePortSpinBox.setMaximum(65535)
        self.uiSourcePortSpinBox.setProperty("value", 1)
        self.uiSourcePortSpinBox.setObjectName(_fromUtf8("uiSourcePortSpinBox"))
        self.gridlayout1.addWidget(self.uiSourcePortSpinBox, 0, 1, 1, 1)
        self.uiSourceDLCILabel = QtGui.QLabel(self.uiFrameRelaySourceGroupBox)
        self.uiSourceDLCILabel.setObjectName(_fromUtf8("uiSourceDLCILabel"))
        self.gridlayout1.addWidget(self.uiSourceDLCILabel, 1, 0, 1, 1)
        self.uiSourceDLCISpinBox = QtGui.QSpinBox(self.uiFrameRelaySourceGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSourceDLCISpinBox.sizePolicy().hasHeightForWidth())
        self.uiSourceDLCISpinBox.setSizePolicy(sizePolicy)
        self.uiSourceDLCISpinBox.setMaximum(65535)
        self.uiSourceDLCISpinBox.setProperty("value", 101)
        self.uiSourceDLCISpinBox.setObjectName(_fromUtf8("uiSourceDLCISpinBox"))
        self.gridlayout1.addWidget(self.uiSourceDLCISpinBox, 1, 1, 1, 1)
        self.gridlayout.addWidget(self.uiFrameRelaySourceGroupBox, 0, 0, 1, 2)
        self.uiFrameRelayMappingGroupBox = QtGui.QGroupBox(frameRelaySwitchConfigPageWidget)
        self.uiFrameRelayMappingGroupBox.setObjectName(_fromUtf8("uiFrameRelayMappingGroupBox"))
        self.vboxlayout = QtGui.QVBoxLayout(self.uiFrameRelayMappingGroupBox)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.uiMappingTreeWidget = QtGui.QTreeWidget(self.uiFrameRelayMappingGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiMappingTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiMappingTreeWidget.setSizePolicy(sizePolicy)
        self.uiMappingTreeWidget.setRootIsDecorated(False)
        self.uiMappingTreeWidget.setObjectName(_fromUtf8("uiMappingTreeWidget"))
        self.vboxlayout.addWidget(self.uiMappingTreeWidget)
        self.gridlayout.addWidget(self.uiFrameRelayMappingGroupBox, 0, 2, 3, 1)
        self.uiFrameRelayDestinationGroupBox = QtGui.QGroupBox(frameRelaySwitchConfigPageWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiFrameRelayDestinationGroupBox.sizePolicy().hasHeightForWidth())
        self.uiFrameRelayDestinationGroupBox.setSizePolicy(sizePolicy)
        self.uiFrameRelayDestinationGroupBox.setObjectName(_fromUtf8("uiFrameRelayDestinationGroupBox"))
        self.gridlayout2 = QtGui.QGridLayout(self.uiFrameRelayDestinationGroupBox)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.uiDestinationPortLabel = QtGui.QLabel(self.uiFrameRelayDestinationGroupBox)
        self.uiDestinationPortLabel.setObjectName(_fromUtf8("uiDestinationPortLabel"))
        self.gridlayout2.addWidget(self.uiDestinationPortLabel, 0, 0, 1, 1)
        self.uiDestinationPortSpinBox = QtGui.QSpinBox(self.uiFrameRelayDestinationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDestinationPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiDestinationPortSpinBox.setSizePolicy(sizePolicy)
        self.uiDestinationPortSpinBox.setMinimum(0)
        self.uiDestinationPortSpinBox.setMaximum(65535)
        self.uiDestinationPortSpinBox.setProperty("value", 10)
        self.uiDestinationPortSpinBox.setObjectName(_fromUtf8("uiDestinationPortSpinBox"))
        self.gridlayout2.addWidget(self.uiDestinationPortSpinBox, 0, 1, 1, 1)
        self.uiDestinationDLCILabel = QtGui.QLabel(self.uiFrameRelayDestinationGroupBox)
        self.uiDestinationDLCILabel.setObjectName(_fromUtf8("uiDestinationDLCILabel"))
        self.gridlayout2.addWidget(self.uiDestinationDLCILabel, 1, 0, 1, 1)
        self.uiDestinationDLCISpinBox = QtGui.QSpinBox(self.uiFrameRelayDestinationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDestinationDLCISpinBox.sizePolicy().hasHeightForWidth())
        self.uiDestinationDLCISpinBox.setSizePolicy(sizePolicy)
        self.uiDestinationDLCISpinBox.setMaximum(65535)
        self.uiDestinationDLCISpinBox.setProperty("value", 202)
        self.uiDestinationDLCISpinBox.setObjectName(_fromUtf8("uiDestinationDLCISpinBox"))
        self.gridlayout2.addWidget(self.uiDestinationDLCISpinBox, 1, 1, 1, 1)
        self.gridlayout.addWidget(self.uiFrameRelayDestinationGroupBox, 1, 0, 1, 2)
        self.uiAddPushButton = QtGui.QPushButton(frameRelaySwitchConfigPageWidget)
        self.uiAddPushButton.setObjectName(_fromUtf8("uiAddPushButton"))
        self.gridlayout.addWidget(self.uiAddPushButton, 2, 0, 1, 1)
        self.uiDeletePushButton = QtGui.QPushButton(frameRelaySwitchConfigPageWidget)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName(_fromUtf8("uiDeletePushButton"))
        self.gridlayout.addWidget(self.uiDeletePushButton, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 3, 1, 1, 2)

        self.retranslateUi(frameRelaySwitchConfigPageWidget)
        QtCore.QMetaObject.connectSlotsByName(frameRelaySwitchConfigPageWidget)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiSourcePortSpinBox, self.uiSourceDLCISpinBox)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiSourceDLCISpinBox, self.uiDestinationPortSpinBox)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiDestinationPortSpinBox, self.uiDestinationDLCISpinBox)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiDestinationDLCISpinBox, self.uiAddPushButton)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiAddPushButton, self.uiDeletePushButton)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiDeletePushButton, self.uiMappingTreeWidget)

    def retranslateUi(self, frameRelaySwitchConfigPageWidget):
        frameRelaySwitchConfigPageWidget.setWindowTitle(_translate("frameRelaySwitchConfigPageWidget", "Frame Relay Switch", None))
        self.uiFrameRelaySourceGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "Source", None))
        self.uiSourcePortLabel.setText(_translate("frameRelaySwitchConfigPageWidget", "Port:", None))
        self.uiSourceDLCILabel.setText(_translate("frameRelaySwitchConfigPageWidget", "DLCI:", None))
        self.uiFrameRelayMappingGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "Mapping", None))
        self.uiMappingTreeWidget.headerItem().setText(0, _translate("frameRelaySwitchConfigPageWidget", "Port:DLCI", None))
        self.uiMappingTreeWidget.headerItem().setText(1, _translate("frameRelaySwitchConfigPageWidget", "Port:DLCI", None))
        self.uiFrameRelayDestinationGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "Destination", None))
        self.uiDestinationPortLabel.setText(_translate("frameRelaySwitchConfigPageWidget", "Port:", None))
        self.uiDestinationDLCILabel.setText(_translate("frameRelaySwitchConfigPageWidget", "DLCI:", None))
        self.uiAddPushButton.setText(_translate("frameRelaySwitchConfigPageWidget", "&Add", None))
        self.uiDeletePushButton.setText(_translate("frameRelaySwitchConfigPageWidget", "&Delete", None))

