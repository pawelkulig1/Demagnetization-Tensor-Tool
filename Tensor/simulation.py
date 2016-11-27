from formulas import *
import multiprocessing
from PyQt4 import QtCore
from PyQt4.QtCore import QThread, SIGNAL
import time

class SimulateThread(QThread):
    def __init__(self, emitter, collector, nThreads):
        QThread.__init__(self)
        self.emitter = emitter
        self.collector = collector
        self.nThreads = nThreads

    def __del__(self):
        self.wait()

    def run(self):
        self.simulate(self.emitter, self.collector)

    def simulate(self, emi, rec):
        if emi.axis == -1:
            emitter = Rectangle(emi.width, emi.depth, emi.height, emi.x, emi.y, emi.z, emi.widthEl, emi.depthEl,
                                emi.heightEl)
        else:
            emitter = Ellipse(emi.width, emi.depth, emi.height, emi.axis, emi.x, emi.y, emi.z, emi.widthEl, emi.depthEl,
                              emi.heightEl)
        if rec.axis == -1:
            receiver = Rectangle(rec.width, rec.depth, rec.height, rec.x, rec.y, rec.z, rec.widthEl, rec.depthEl,
                                 rec.heightEl)
        else:
            receiver = Ellipse(rec.width, rec.depth, rec.height, rec.axis, rec.x, rec.y, rec.z, rec.widthEl,
                               rec.depthEl, rec.heightEl)

        receiver.createStructure()
        emitter.createStructure()

        thread = []

        #nThreads = multiprocessing.cpu_count()
        print(receiver.nElements)
        manager = multiprocessing.Manager()
        avgMatrix = manager.list()

        for i in range(self.nThreads):

            onThread = mt.floor(receiver.nElements / self.nThreads)
            thisThreadStart = onThread * (i + 1)

            if i == self.nThreads - 1:
                thisThreadEnd = receiver.nElements
            else:
                thisThreadEnd = onThread * (i + 2)

            process = multiprocessing.Process(target=self.calculateAllAverages, args=(
            thisThreadStart, thisThreadEnd, self.nThreads, receiver, emitter, avgMatrix))

            thread.append(process)
            thread[i].start()

        #starting calculations in main thread to send signals to GUI
        self.calculateAllAverages(0, mt.floor(receiver.nElements / self.nThreads), self.nThreads, receiver, emitter, avgMatrix)


        for i in range(self.nThreads):
            thread[i].join()

        #print(avgMatrix)

        finalMatrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # create sum of all matrixes to calculate average
        for k, e in enumerate(avgMatrix):
            for i, e in enumerate(avgMatrix[0]):
                finalMatrix[i] += avgMatrix[k][i]

        # divide sum by all elements
        for k, e in enumerate(avgMatrix[0]):
            finalMatrix[k] /= len(avgMatrix)
            finalMatrix[k] *= (
            emitter.nElements / (4 * mt.pi * emitter.widthSmall * emitter.depthSmall * emitter.heightSmall))

        avgMatrix = []
        #print("[", finalMatrix[0], finalMatrix[1], finalMatrix[2], "]")
        #print("[", finalMatrix[3], finalMatrix[4], finalMatrix[5], "]")
        #print("[", finalMatrix[6], finalMatrix[7], finalMatrix[8], "]")
        self.emit(QtCore.SIGNAL('FINAL_MATRIX'), finalMatrix)

        #return finalMatrix

    def calculateAllAverages(self, start, stop, nThreads, receiver, emitter, avgMatrix):
        for j in range(start, stop):
            if (start == 0):
                val = int(((j * 100) / receiver.nElements) * nThreads)
                self.emit(QtCore.SIGNAL('PROGRESS'), val)
            a11 = 0
            a12 = 0
            a13 = 0
            a22 = 0
            a23 = 0
            a33 = 0

            for i in range(emitter.nElements):
                delx, dely, delz = calculateDistance(emitter.smallBlocksStructure[i], receiver.smallBlocksStructure[j])
                dx = emitter.widthSmall
                dy = emitter.depthSmall
                dz = emitter.heightSmall

                a11 += calculateNxx(delx, dely, delz, dx, dy, dz, emitter)
                a12 += calculateNxy(delx, dely, delz, dx, dy, dz, emitter)
                a13 += calculateNxy(delx, delz, dely, dx, dz, dy, emitter)
                # a21 = a12
                a22 += calculateNxx(dely, delx, delz, dy, dx, dz, emitter)
                a23 += calculateNxy(dely, delz, delx, dy, dz, dx, emitter)
                # a31 = a13
                # a32 = a23
                a33 += calculateNxx(delz, dely, delx, dz, dy, dx, emitter)

            a11 = a11 / emitter.nElements
            a12 = a12 / emitter.nElements
            a13 = a13 / emitter.nElements
            a22 = a22 / emitter.nElements
            a23 = a23 / emitter.nElements
            a33 = a33 / emitter.nElements

            avgMatrix.append([a11, a12, a13, a12, a22, a23, a13, a23, a33])
        return avgMatrix

