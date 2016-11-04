import math as mt
from formulas import *

from PyQt4.QtCore import QThread, SIGNAL

class Thread(QThread, QtGui.QMainWindow):
    def __init__(self):
        QThread.__init__(self)
        
    def sendSignal(self, top_post):
        #print(top_post)
        print(self.emit(SIGNAL('add_post(QString)'), top_post))
        

def simulate(emi, rec):
    percents = Thread()
    
    emitter = block(emi.width, emi.depth, emi.height, emi.x, emi.y, emi.z, emi.widthEl, emi.depthEl, emi.heightEl)
    receiver = block(rec.width, rec.depth, rec.height, rec.x, rec.y, rec.z, rec.widthEl, rec.depthEl, rec.heightEl)

    #for each small part create object

    emitterDivided = []
    for i in range(emitter.nElements):
        x, y, z = emitter.smallPoz(i)
        dx, dy, dz = emitter.getSmallSize()
        emitterDivided.append(smallBlock(x,y,z, dx, dy, dz))

    receiverDivided = []
    for i in range(receiver.nElements):
        x, y, z = receiver.smallPoz(i)
        dx, dy, dz = receiver.getSmallSize()
        receiverDivided.append(smallBlock(x,y,z, dx, dy, dz))

    avgMatrix = []
    for j in range(receiver.nElements):
        #((j*100)/receiver.nElements, "%")
        #emit(SIGNAL('add_post(QString)'), top_post)
        percents.sendSignal((j*100)/receiver.nElements)
        a11 = 0
        a12 = 0
        a13 = 0
        a22 = 0
        a23 = 0
        a33 = 0
        
        for i in range(emitter.nElements):
            
            delx, dely, delz = (emitterDivided[i]+receiverDivided[j])
            
            dx = emitterDivided[i].width
            dy = emitterDivided[i].depth
            dz = emitterDivided[i].height
            
            a11 += calculateNxx(delx, dely, delz, dx, dy, dz,emitter)
            a12 += calculateNxy(delx, dely, delz, dx, dy, dz,emitter)
            a13 += calculateNxy(delx, delz, dely, dx, dz, dy,emitter)
            #a21 = a12
            a22 += calculateNxx(dely, delx, delz, dy, dx, dz,emitter)
            a23 += calculateNxy(dely, delz, delx, dy, dz, dx,emitter)
            #a31 = a13
            #a32 = a23
            a33 += calculateNxx(delz, dely, delx, dz, dy, dx,emitter)

        a11=a11/emitter.nElements
        a12=a12/emitter.nElements
        a13=a13/emitter.nElements
        a22=a22/emitter.nElements
        a23=a23/emitter.nElements
        a33=a33/emitter.nElements

        avgMatrix.append([a11, a12, a13, a12, a22, a23, a13, a23, a33])
        
    finalMatrix = [0,0,0,0,0,0,0,0,0]
    #create sum of all matrixes to calculate average
    for k in range(len(avgMatrix)):
        for i in range(len(avgMatrix[0])):
            finalMatrix[i] += avgMatrix[k][i]
        
    #divide sum by all elements
    for k in range(len(avgMatrix[0])):
        finalMatrix[k]/=len(avgMatrix)


    print("[",finalMatrix[0], finalMatrix[1], finalMatrix[2], "]")
    print("[",finalMatrix[3], finalMatrix[4], finalMatrix[5], "]")
    print("[",finalMatrix[6], finalMatrix[7], finalMatrix[8], "]")


