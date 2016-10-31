import sys
from PyQt4 import QtCore, QtGui
from mainWindow import Ui_mainWindow
from helpWindow import Ui_helpWindow

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
        
        #EmitterData
        self.emitterWidth = (self.emitterWidthLineEdit.text())
        self.emitterDepth = (self.emitterDepthLineEdit.text())
        self.emitterHeight = (self.emitterHeightLineEdit.text())
        
        self.emitterX = (self.emitterXLineEdit.text())
        self.emitterY = (self.emitterYLineEdit.text())
        self.emitterZ = (self.emitterZLineEdit.text())
        
        self.emitterWidthEl = (self.emitterElementsWidthLineEdit.text())
        self.emitterDepthEl = (self.emitterElementsDepthLineEdit.text())
        self.emitterHeightEl = (self.emitterElementsHeightLineEdit.text())
        #print(emitterWidthEl)
        
        if not self.emitterFormValidation():
            return 0
        
        #CollectorData
        
        self.collectorWidth = (self.collectorWidthLineEdit.text())
        self.collectorDepth = (self.collectorDepthLineEdit.text())
        self.collectorHeight = (self.collectorHeightLineEdit.text())
        
        self.collectorX = (self.collectorXLineEdit.text())
        self.collectorY = (self.collectorYLineEdit.text())
        self.collectorZ = (self.collectorZLineEdit.text())
        
        self.collectorWidthEl = (self.collectorElementsWidthLineEdit.text())
        self.collectorDepthEl = (self.collectorElementsDepthLineEdit.text())
        self.collectorHeightEl = (self.collectorElementsHeightLineEdit.text())
        
        if not self.collectorFormValidation():
            return 0
        
        print("simulation finished succesfully")
        return 1
        
    def emitterFormValidation(self):
        try:
            self.emitterWidth = float(self.emitterWidth)
            self.emitterDepth = float(self.emitterDepth)
            self.emitterHeight = float(self.emitterHeight)
            self.emitterX = float(self.emitterX)
            self.emitterY = float(self.emitterY)
            self.emitterZ = float(self.emitterZ)
            self.emitterWidthEl = float(self.emitterWidthEl)
            self.emitterDepthEl = float(self.emitterDepthEl)
            self.emitterHeightEl = float(self.emitterHeightEl)
        except:
            self.alert("Some emitter data are not numbers!")
            return 0
            
        if self.emitterWidth>1e-5:
            if self.areYouSure("Emitter width seems very big, are you sure you want to leave it?","Check if you really want to make structure of that size, exception is always raised when size exceeds 1e-5"):
                pass
            else:
                return 0
            
        if self.emitterDepth>1e-5:
            if self.areYouSure("Emitter depth seems very big, are you sure you want to leave it?","Check if you really want to make structure of that size, exception is always raised when size exceeds 1e-5"):
                pass
            else:
                return 0
            
        if self.emitterHeight>1e-5:
            if self.areYouSure("Emitter height seems very big, are you sure you want to leave it?", "Check if you really want to make structure of that size, exception is always raised when size exceeds 1e-5"):
                pass
            else:
                return 0
        
        if self.emitterWidthEl<0:
            self.alert("Emitter cannot be cut in less than 1 element (width axis)")
            return 0
        
        if self.emitterDepthEl<0:
            self.alert("Emitter cannot be cut in less than 1 element (depth axis)")
            return 0
        
        if self.emitterHeightEl<0:
            self.alert("Emitter cannot be cut in less than 1 element (height axis)")
            return 0
        
        
        if self.emitterWidthEl*self.emitterDepthEl*self.emitterHeightEl>1000:
            if self.areYouSure("Calculation time may be huge for a lot of elements! Are you sure? ("+str(self.emitterWidthEl*self.emitterDepthEl*self.emitterHeightEl)+" only in emitter)"):
                pass
            else:
                return 0
        return 1

    def collectorFormValidation(self):
        try:
            self.collectorWidth = float(self.collectorWidth)
            self.collectorDepth = float(self.collectorDepth)
            self.collectorHeight = float(self.collectorHeight)
            self.collectorX = float(self.collectorX)
            self.collectorY = float(self.collectorY)
            self.collectorZ = float(self.collectorZ)
            self.collectorWidthEl = float(self.collectorWidthEl)
            self.collectorDepthEl = float(self.collectorDepthEl)
            self.collectorHeightEl = float(self.collectorHeightEl)
        except:
            self.alert("Some collector data are not numbers!")
            return 0
            
        if self.collectorWidth>1e-5:
            if self.areYouSure("collector width seems very big, are you sure you want to leave it?","Check if you really want to make structure of that size, exception is always raised when size exceeds 1e-5"):
                pass
            else:
                return 0
            
        if self.collectorDepth>1e-5:
            if self.areYouSure("collector depth seems very big, are you sure you want to leave it?","Check if you really want to make structure of that size, exception is always raised when size exceeds 1e-5"):
                pass
            else:
                return 0
            
        if self.collectorHeight>1e-5:
            if self.areYouSure("collector height seems very big, are you sure you want to leave it?", "Check if you really want to make structure of that size, exception is always raised when size exceeds 1e-5"):
                pass
            else:
                return 0
        
        if self.collectorWidthEl<0:
            self.alert("collector cannot be cut in less than 1 element (width axis)")
            return 0
        
        if self.collectorDepthEl<0:
            self.alert("collector cannot be cut in less than 1 element (depth axis)")
            return 0
        
        if self.collectorHeightEl<0:
            self.alert("collector cannot be cut in less than 1 element (height axis)")
            return 0
        
        
        if self.collectorWidthEl*self.collectorDepthEl*self.collectorHeightEl>1000:
            if self.areYouSure("Calculation time may be huge for a lot of elements! Are you sure? ("+str(self.collectorWidthEl*self.collectorDepthEl*self.collectorHeightEl)+" only in collector)"):
                pass
            else:
                return 0
        return 1

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
