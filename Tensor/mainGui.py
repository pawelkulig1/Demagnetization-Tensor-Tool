import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
from mainWindow import Ui_mainWindow
from helpWindow import Ui_helpWindow
from result import Ui_result
from simulation import *
from parseGuiData import *
import multiprocessing
import time


class HelpWindow(QtGui.QMainWindow, Ui_helpWindow):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.closePushButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()


class ResultWindow(QtGui.QMainWindow, Ui_result):
    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.closePushButton.clicked.connect(self.closeWindow)
        self.values = 0

    def setResult(self):
        self.a11_lineEdit.setText(str(self.values[0]))
        self.a12_lineEdit.setText(str(self.values[1]))
        self.a13_lineEdit.setText(str(self.values[2]))
        self.a21_lineEdit.setText(str(self.values[3]))
        self.a22_lineEdit.setText(str(self.values[4]))
        self.a23_lineEdit.setText(str(self.values[5]))
        self.a31_lineEdit.setText(str(self.values[6]))
        self.a32_lineEdit.setText(str(self.values[7]))
        self.a33_lineEdit.setText(str(self.values[8]))

        #pass


    def closeWindow(self):
        self.close()

class MainScreen(QtGui.QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.emitterComboBox.hide()
        self.collectorComboBox.hide()
        self.collectorComboBox.hide()
        self.nThreads = multiprocessing.cpu_count()
        self.threadNumberLineEdit.setText(str(self.nThreads))
        self.windowAction()
        self.simulationInProgress = False

    def windowAction(self):
        self.simulateButton.clicked.connect(self.simulateButtonClicked)
        self.exitButton.clicked.connect(self.closeProgram)
        self.helpButton.clicked.connect(self.helpWindow)
        self.emitterRecRadioButton.toggled.connect(self.emitterRadioToggle)
        self.collectorRecRadioButton.toggled.connect(self.collectorRadioToggle)


    def emitterRadioToggle(self):
        if self.emitterRecRadioButton.isChecked():
            self.emitterWidthLabel.setText("width")
            self.emitterDepthLabel.setText("depth")
            self.emitterWidthLineEdit.move(60, 20)
            self.emitterDepthLineEdit.move(60, 40)
            self.emitterWidthMetersLabel.move(150, 22)
            self.emitterDepthMetersLabel.move(150, 42)
            self.emitterComboBox.hide()
        else:
            self.emitterWidthLabel.setText("A Factor")
            self.emitterDepthLabel.setText("B Factor")
            self.emitterWidthLineEdit.move(70, 20)
            self.emitterDepthLineEdit.move(70, 40)
            self.emitterWidthMetersLabel.move(160, 22)
            self.emitterDepthMetersLabel.move(160, 42)
            self.emitterComboBox.show()

    def collectorRadioToggle(self):
        if self.collectorRecRadioButton.isChecked():
            self.collectorWidthLabel.setText("width")
            self.collectorDepthLabel.setText("depth")
            self.collectorWidthLineEdit.move(60, 20)
            self.collectorDepthLineEdit.move(60, 40)
            self.collectorWidthMetersLabel.move(150, 22)
            self.collectorDepthMetersLabel.move(150, 42)
            self.collectorComboBox.hide()
        else:
            self.collectorWidthLabel.setText("A Factor")
            self.collectorDepthLabel.setText("B Factor")
            self.collectorWidthLineEdit.move(70, 20)
            self.collectorDepthLineEdit.move(70, 40)
            self.collectorWidthMetersLabel.move(160, 22)
            self.collectorDepthMetersLabel.move(160, 42)
            self.collectorComboBox.show()

    def alert(self, text, details=""):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(text)
        # msg.setInformativeText(details)
        if details != "":
            msg.setDetailedText(details)
        msg.exec_()

    def areYouSure(self, text, details=""):
        choice = QtGui.QMessageBox.question(self, "This may be mistake!", text,
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            return 1
        else:
            return 0

    def simulateButtonClicked(self):

        self.simulateButton.setText("Simulating...")
        self.setProgressBar(0)

        if self.emitterRecRadioButton.isChecked():
            self.emitterShape = "r"
            self.emitterAxis = "-1"
        else:
            self.emitterShape = "c"
            self.emitterAxis = str(self.emitterComboBox.currentText())

        if self.collectorRecRadioButton.isChecked():
            self.collectorShape = "r"
            self.collectorAxis = "-1"
        else:
            self.collectorShape = "c"
            self.collectorAxis = str(self.collectorComboBox.currentText())

        self.emitterWidth = (self.emitterWidthLineEdit.text())
        self.emitterDepth = (self.emitterDepthLineEdit.text())
        self.emitterHeight = (self.emitterHeightLineEdit.text())

        self.emitterX = (self.emitterXLineEdit.text())
        self.emitterY = (self.emitterYLineEdit.text())
        self.emitterZ = (self.emitterZLineEdit.text())

        self.emitterWidthEl = (self.emitterElementsWidthLineEdit.text())
        self.emitterDepthEl = (self.emitterElementsDepthLineEdit.text())
        self.emitterHeightEl = (self.emitterElementsHeightLineEdit.text())


        emitter = GuiData(self.emitterWidth, self.emitterDepth, self.emitterHeight, self.emitterX, self.emitterY, self.emitterZ, self.emitterWidthEl,
                          self.emitterDepthEl, self.emitterHeightEl, self.emitterAxis)

        self.collectorWidth = (self.collectorWidthLineEdit.text())
        self.collectorDepth = (self.collectorDepthLineEdit.text())
        self.collectorHeight = (self.collectorHeightLineEdit.text())

        self.collectorX = (self.collectorXLineEdit.text())
        self.collectorY = (self.collectorYLineEdit.text())
        self.collectorZ = (self.collectorZLineEdit.text())

        self.collectorWidthEl = (self.collectorElementsWidthLineEdit.text())
        self.collectorDepthEl = (self.collectorElementsDepthLineEdit.text())
        self.collectorHeightEl = (self.collectorElementsHeightLineEdit.text())


        collector = GuiData(self.collectorWidth, self.collectorDepth, self.collectorHeight, self.collectorX, self.collectorY,
                            self.collectorZ, self.collectorWidthEl, self.collectorDepthEl, self.collectorHeightEl, self.collectorAxis)

        self.nThreads = int(self.threadNumberLineEdit.displayText())

        if emitter.error[0] == 'alert':
            self.alert(emitter.error[1], "emitter")
            return 0

        if emitter.error[0] == "yesOrNo":
            if self.areYouSure(emitter.error[1]):
                pass
            else:
                return 0

        if collector.error[0] == 'alert':
            self.alert(collector.error[1], "collector")
            return 0

        if collector.error[0] == "yesOrNo":
            if self.areYouSure(collector.error[1]):
                pass
            else:
                return 0


        self.get_thread = SimulateThread(emitter, collector, self.nThreads)
        self.simulationInProgress = True
        #self.connect(self.get_thread, SIGNAL("add_post(QString)"), self.add_post)


        self.get_thread.start()
        self.connect(self.get_thread, SIGNAL("finished()"), self.done)
        self.connect(self.get_thread, QtCore.SIGNAL('PROGRESS'), self.setProgressBar)
        self.connect(self.get_thread, QtCore.SIGNAL("FINAL_MATRIX"), self.showResult)

    def setProgressBar(self, value):
        self.simulationProgressBar.setValue(int(value))

    def showResult(self, value):
        print("{}".format(value))
        window = ResultWindow(self)
        window.values = value
        window.setResult()
        window.show()



    def done(self):
        self.simulationInProgress = False
        self.setProgressBar(100)
        self.simulateButton.setText("Simulate")

    def helpWindow(self):
        window = HelpWindow(self)
        window.show()

    def closeProgram(self):
        choice = QtGui.QMessageBox.question(self, "Leave Program", "Are You sure you want to leave program?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec_())
