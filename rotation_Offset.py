from datetime import time

import maya.cmds as cmds

import os

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from maya import OpenMayaUI
from shiboken2 import wrapInstance
from PySide2.QtGui import QPixmap
import json

# from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.OpenMayaUI as omui

mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)


class RotationOffsetTool(QWidget):

    def __init__(self, *args, **kwargs):
        super(RotationOffsetTool, self).__init__(*args, **kwargs)
        self.xRotation = 0
        self.yRotation = 0
        self.zRotation = 0
        self.setParent(mayaMainWindow)
        self.setObjectName('RotationOffsetTool')
        self.setWindowTitle('Rotation Offset Tool')
        self.setWindowFlags(Qt.Window)
        self.init_UI()

    def init_UI(self):
        usd = cmds.internalVar(usd=True)
        UI_FILE = os.path.join(usd, 'Rotation_Offset', 'Resources', 'RotationOffset.ui')
        ui_file = QFile(UI_FILE)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()

        self.ui = loader.load(ui_file, parentWidget=self)
        ui_file.close()

        self.xSpinBox = self.ui.xSpinBox
        self.ySpinBox = self.ui.ySpinBox
        self.zSpinBox = self.ui.zSpinBox

        self.ui.errorLabel.setStyleSheet("color:rgb(238, 75, 43)")
        self.ui.errorLabel.setVisible(False)

        self.ui.execButton.clicked.connect(self.offsetRotation)

    def run_UI(self):
        self.ui.show()

    def offsetRotation(self):

        self.ui.errorLabel.setVisible(False)

        sel = cmds.ls(sl=True)
        print(sel)

        if (len(sel) > 0) and (sel[0] == 'BatOffset_1' or sel[0] == 'bat_jnt'):

            keyframes = cmds.keyframe(sel[0], q=True)
            sortedUniqueKeyframes = sorted(set(keyframes))

            self.xRotation = self.xSpinBox.value()
            self.yRotation = self.ySpinBox.value()
            self.zRotation = self.zSpinBox.value()

            print(self.xRotation, self.yRotation, self.zRotation)

            for i in sortedUniqueKeyframes:
                cmds.currentTime(i)
                cmds.rotate(self.xRotation, self.yRotation, self.zRotation, r=True, os=True, fo=True)

        else:
            self.ui.errorLabel.setVisible(True)


try:
    namingValidator.close()
    namingValidator.deleteLater()
except:
    pass
namingValidator = RotationOffsetTool()
namingValidator.run_UI()
