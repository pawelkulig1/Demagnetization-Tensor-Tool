import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
from mainWindow import Ui_mainWindow
from helpWindow import Ui_helpWindow
from simulation import simulate
from parseGuiData import *


class SimulateThread(QThread):

    def __init__(self, emitter, collector):
        QThread.__init__(self)
        self.emitter = emitter
        self.collector = collector

    def __del__(self):
        self.wait()
        
    def run(self):
        simulate(self.emitter, self.collector)

class HelpWindow(QtGui.QMainWindow, Ui_helpWindow):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.closePushButton.clicked.connect(self.closeWindow)      
        
    def closeWindow(self):
        self.close()

class MainScreen(QtGui.QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        #self.helpButton.clicked.connect(self.helpWindowClick)
        self.window()
        
    def alert(self, text, details=""):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(text)
        #msg.setInformativeText(details)
        if details!="":
            msg.setDetailedText(details)
        msg.exec_()
    
    def areYouSure(self, text, details=""):
        choice = QtGui.QMessageBox.question(self, "This may be mistake!", text, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            return 1
        else:
            return 0
    
    def window(self):
        self.simulateButton.clicked.connect(self.simulateButtonClicked)
        self.exitButton.clicked.connect(self.closeProgram)
        self.helpButton.clicked.connect(self.helpWindow)
        
    def simulateButtonClicked(self):
        print("simulation started")        
        
        self.setProgressBar(0)
        
        self.emitterWidth = (self.emitterWidthLineEdit.text())
        self.emitterDepth = (self.emitterDepthLineEdit.text())
        self.emitterHeight = (self.emitterHeightLineEdit.text())
        
        self.emitterX = (self.emitterXLineEdit.text())
        self.emitterY = (self.emitterYLineEdit.text())
        self.emitterZ = (self.emitterZLineEdit.text())
        
        self.emitterWidthEl = (self.emitterElementsWidthLineEdit.text())
        self.emitterDepthEl = (self.emitterElementsDepthLineEdit.text())
        self.emitterHeightEl = (self.emitterElementsHeightLineEdit.text())
        
        emitter = GuiData(self.emitterWidth, self.emitterDepth, self.emitterHeight,  self.emitterWidthEl, self.emitterDepthEl, self.emitterHeightEl, self.emitterX, self.emitterY, self.emitterZ,)
       
        
        self.collectorWidth = (self.collectorWidthLineEdit.text())
        self.collectorDepth = (self.collectorDepthLineEdit.text())
        self.collectorHeight = (self.collectorHeightLineEdit.text())
        
        self.collectorX = (self.collectorXLineEdit.text())
        self.collectorY = (self.collectorYLineEdit.text())
        self.collectorZ = (self.collectorZLineEdit.text())
        
        self.collectorWidthEl = (self.collectorElementsWidthLineEdit.text())
        self.collectorDepthEl = (self.collectorElementsDepthLineEdit.text())
        self.collectorHeightEl = (self.collectorElementsHeightLineEdit.text())        

        collector = GuiData(self.collectorWidth, self.collectorDepth, self.collectorHeight, self.collectorWidthEl, self.collectorDepthEl, self.collectorHeightEl, self.collectorX, self.collectorY, self.collectorZ)
    
        
        
        self.get_thread = SimulateThread(emitter, collector)
        #print(self.connect(self.get_thread, SIGNAL("setProgressBar(QString)"), self.setProgressBar))
        self.connect(self.get_thread, SIGNAL("add_post(QString)"), self.add_post)
        self.connect(self.get_thread, SIGNAL("finished()"), self.done)
        self.get_thread.start()
        

        #print("simulation finished succesfully")
        return 1
    
    def setProgressBar(self, value):
        #print(value)
        self.simulationProgressBar.setValue(value)
        
    def add_post(self, post_text):
        print(post_text)
    
    def done(self):
        pass
    
    def helpWindow(self):
        window = HelpWindow(self)
        window.show()

    def closeProgram(self):
        choice = QtGui.QMessageBox.question(self, "Leave Program", "Are You sure you want to leave program?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
	


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec_())
