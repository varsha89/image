__author__ = 'Serge'

from math import *

class Smatrix:
    def __init__(self, size):
        self.size = size
        self.cont = list()
        #self.fillSmat()

    def getCont(self):
        return self.cont

    def getSize(self):
        return self.size

    def fillSmat(self):
        for i in xrange(self.size):
            self.cont.append(list())
            for j in xrange(self.size):
                self.cont[i].append(42)

    def printSmat(self):
        for i in xrange(self.size):
            print self.cont[i]

    def average(self):
        res = 0
        for i in xrange(self.size):
            for j in xrange(self.size):
                res += self.getCont()[i][j]
        return res/self.size/self.size

    def devSmat(self):
        smat = self
        aver = self.average()
        for i in xrange(self.size):
            for j in xrange(self.size):
                smat.getCont()[i][j] -= aver
        return smat

    def stDev(self):
        res = 0
        aver = self.average()
        for i in xrange(self.size):
            for j in xrange(self.size):
                res += pow((self.getCont()[i][j] - aver), 2)
        return sqrt(res/self.size/self.size)

    def norm(self):
        smat = self
        smatMax = 1
        for i in xrange(self.size):
            for j in xrange(self.size):
                if (smatMax < self.getCont()[i][j]):
                    smatMax = self.getCont()[i][j]
        for i in xrange(self.size):
            for j in xrange(self.size):
                smat.getCont()[i][j] = (smat.getCont()[i][j] * 255) / smatMax
        print smatMax
        return smat


def SmatSum(smat1, smat2): # REWRITE '+' SYMBOL
    if (smat1.size == smat2.size):
        res = Smatrix(smat1.size)
        res.fillSmat()
        for i in xrange(smat1.size):
            for j in xrange(smat1.size):
                res.getCont()[i][j] = smat1.getCont()[i][j] + smat2.getCont()[i][j]
        return res
    else:
        print "Different sizes!"
        return 0


def Covariation(smatX, smatY):
    if (smatX.size == smatY.size):
        res = 0
        averX = smatX.average()
        averY = smatY.average()
        for i in xrange(smatX.size):
            for j in xrange(smatX.size):
                res += (smatX.getCont()[i][j] - averX) * (smatY.getCont()[i][j] - averY)
        return 1. * res/smatX.size/smatX.size
    else:
        print "Different sizes!"
        return 0


def Covariation2(smatX, smatY, averX=None):
    if (smatX.size == smatY.size):
        res = 0
        if averX == None:
            averX = smatX.average()
        averY = smatY.average()
        for i in xrange(smatX.size):
            for j in xrange(smatX.size):
                res += (smatX.getCont()[i][j] - averX) * (smatY.getCont()[i][j] - averY)
        return 1. * res/smatX.size/smatX.size
    else:
        print "Different sizes!"
        return 0


def PirsonOld(smatX, smatY):
    if (smatX.size == smatY.size):
        top = 0
        botX = 0
        botY = 0
        averX = smatX.average()
        averY = smatY.average()
        for i in xrange(smatX.size):
            for j in xrange(smatX.size):
                top += (smatX.getCont()[i][j] - averX) * (smatY.getCont()[i][j] - averY)
                botX += pow((smatX.getCont()[i][j] - averX), 2)
                botY += pow((smatY.getCont()[i][j] - averY), 2)
        return 1. * top/sqrt(botX*botY)
    else:
        print "Different sizes!"
        return 0


def Pirson(smatX, smatY, stDevX=None):
    if (smatX.size == smatY.size):
        top = Covariation(smatX, smatY)
        if stDevX == None:
            stDevX = smatX.stDev()
        stDevY = smatY.stDev()
        return top/stDevX/stDevY
    else:
        print "Different sizes!"
        return 0

def Moments(smat): # Just get moments of a full matrix. Temp thing.
    moments = Smatrix(4)
    for k in xrange(4):
        moments.cont.append(list())
        for s in xrange(4):
            sum = 0
            for i in xrange(smat.size):
                for j in xrange(smat.size):
                    sum += pow(i, k) * pow(j, s) * smat.getCont()[i][j]
            moments.cont[k].append(sum)
    return moments

def Invariants(mom):
    invariants = list()
    invariants.append(mom.getCont()[2][0] + mom.getCont()[0][2])
    invariants.append(pow((mom.getCont()[2][0] - mom.getCont()[0][2]),2) - 4*pow(mom.getCont()[1][1], 2))
    invariants.append(pow((mom.getCont()[3][0] - 3*mom.getCont()[1][2]),2) + pow((3*mom.getCont()[2][1] - mom.getCont()[0][3]),2))
    invariants.append(pow((mom.getCont()[3][0] + mom.getCont()[1][2]),2) + pow((mom.getCont()[2][1] + mom.getCont()[0][3]),2))
    invariants.append((mom.getCont()[3][0] - 3*mom.getCont()[1][2])*(mom.getCont()[3][0] + mom.getCont()[1][2])*(pow((mom.getCont()[3][0] + mom.getCont()[1][2]),2) - 3*pow((mom.getCont()[2][1] + mom.getCont()[0][3]),2)) +
                      (3*mom.getCont()[2][1] - mom.getCont()[0][3])*(mom.getCont()[2][1] + mom.getCont()[0][3])*(3*pow((mom.getCont()[3][0] + mom.getCont()[1][2]),2) - pow((mom.getCont()[2][1] + mom.getCont()[0][3]),2)))
    invariants.append(((mom.getCont()[2][0] - mom.getCont()[0][2]))*((pow((mom.getCont()[3][0] + mom.getCont()[1][2]),2) - pow((mom.getCont()[2][1] + mom.getCont()[0][3]),2))) +
                      4 * mom.getCont()[1][1] * (mom.getCont()[3][0] + mom.getCont()[1][2]) * (mom.getCont()[2][1] + mom.getCont()[0][3]))
    invariants.append((3*mom.getCont()[2][1] - mom.getCont()[0][3])*(mom.getCont()[3][0] + mom.getCont()[1][2])*(pow((mom.getCont()[3][0] + mom.getCont()[1][2]),2) - 3*pow((mom.getCont()[2][1] + mom.getCont()[0][3]),2)) -
                      (mom.getCont()[3][0] - 3*mom.getCont()[1][2])*(mom.getCont()[2][1] + mom.getCont()[0][3])*(3*pow((mom.getCont()[3][0] + mom.getCont()[1][2]),2) - pow((mom.getCont()[2][1] + mom.getCont()[0][3]),2)))
    return invariants

def Euclid(vect1, vect2):
    if len(vect1) == len(vect2):
        sum = 0
        for i in xrange(len(vect1)):
            sum = sum + abs(pow(vect1[i], 2) - pow(vect2[i], 2))
        return sqrt(sum)
    else:
        print 'Different sizes!'
        return 0

def JustSum(vect1, vect2):
    if len(vect1) == len(vect2):
        sum = 0
        for i in xrange(len(vect1)):
            sum = sum + abs(vect1[i] - vect2[i])
        return sum
    else:
        print 'Different sizes!'
        return 0