__author__ = 'Serge'

#from Smatrix import *
from Draw import *
from Files import *
from BinImage import *

class Execution():
    def __init__(self):
        self.binFull = BinImage('../../Diploma/Image/image.bin')
        self.planes = list()
        self.random = list()

    def getPlanes(self):
        return self.planes

    def getRandom(self):
        return self.random

    def cutPlanesFiles(self):
        self.binFull.intCut(2689, 3403, 70)
        self.binFull.intCut(2655, 3540, 70)
        self.binFull.intCut(2645, 3355, 70)

        #self.binFull.intCut(3403, 2689, 70)
        #self.binFull.intCut(3540, 2655, 70)
        #self.binFull.intCut(3355, 2645, 70)

    def readPlanes(self):
        self.planes.append(readSmatFile('./files/pic_3403_2689_70.txt', 70))
        self.planes.append(readSmatFile('./files/pic_3540_2655_70.txt', 70))
        self.planes.append(readSmatFile('./files/pic_3355_2645_70.txt', 70))

    def readRandom(self):
        self.random.append(self.binFull.intRead(1111, 1111, 70))
        self.random.append(self.binFull.intRead(2222, 2222, 70))
        self.random.append(self.binFull.intRead(3333, 3333, 70))

    def printPlanes(self):
        for i in xrange(len(self.planes)):
            self.planes[i].printSmat()
            print '\n'

    def printRandom(self):
        for i in xrange(len(self.random)):
            self.random[i].printSmat()
            print '\n'

    def printPirsonExample(self):
        print '\n'
        for i in xrange(3):
            print Pirson(self.planes[1], self.planes[i])
        print '\n'
        for i in xrange(3):
            print Pirson(self.planes[1], self.random[i])
        print '\n'


        # plot 'heat_map_data.txt' matrix with image

    def printScanLine(self):
        #self.binFull.scanLine(3540, 2655, 150, self.planes[1])
        #self.binFull.scanLine(3540, 2655, 150, self.planes[2])

        self.binFull.scanLine(2650, 3540, 76, self.planes[1])


    def printScanPartPirs(self):
        #self.binFull.scanPartPirs(2555, 3440, 270, 270, self.planes[1])
        self.binFull.scanPartPirs(2640, 3530, 90, 90, self.planes[1])

    def printScanPartInv(self):
        self.binFull.scanPartInv(2555, 3440, 270, 270, self.planes[1])
        #self.binFull.scanPartInv(2640, 3530, 90, 90, self.planes[1])

    def printScanPartOrig(self):
        self.binFull.getOriginal(2555, 3440, 270, 270)
        #self.binFull.getOriginal(2640, 3530, 90, 90)
        #self.binFull.testBin()