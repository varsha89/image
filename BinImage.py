__author__ = 'Serge'

from Files import *
from struct import *

class BinImage:
    def __init__(self, name, width=11232, height=6142):
        self.name = name
        self.width = width
        self.height = height
        self.file = open(name, 'rb')

    def binRead(self, col, row, size):
        smat = Smatrix(size)
        smat.fillSmat()
        self.file.seek(2 * (row * self.width + col))
        for j in range(size):
            for i in xrange(size):
                smat.cont[i][j] = (self.file.read(2))
            self.file.seek(2 * (self.width - size), 1)
        return smat

    def intCut(self, col, row, size):
        strName = 'pic_{}_{}_{}.txt'.format(str(row), str(col), str(size))
        wFile = open("./"+strName, 'w')
        self.file.seek(2 * (row * self.width + col))
        for j in range(size):
            for i in xrange(size):
                wFile.write(str(unpack('H', (self.file.read(2)))[0])+' ')
            self.file.seek(2 * (self.width - size), 1)

    def intRead(self, col, row, size):
        smat = Smatrix(size)
        smat.fillSmat()
        self.file.seek(2 * (row * self.width + col))
        for j in range(size):
            for i in xrange(size):
                smat.cont[i][j] = int(unpack('H', (self.file.read(2)))[0])
            self.file.seek(2 * (self.width - size), 1)
        return smat

    def normRead(self, col, row, size):
        smat = Smatrix(size)
        smat.fillSmat()
        smatMax = 1
        self.file.seek(2 * (row * self.width + col))
        for j in range(size):
            for i in range(size):
                smat.cont[i][j] = int(unpack('H', (self.file.read(2)))[0])
                if (smatMax < smat.getCont()[i][j]):
                    smatMax = smat.getCont()[i][j]
            self.file.seek(2 * (self.width - size), 1)
        for j in xrange(size):
            for i in xrange(size):
                smat.getCont()[i][j] = (smat.getCont()[i][j] * 255) / smatMax
        return smat

    def scanLine(self, col, row, length, pattern):
        strNameInt = './files/intFilePirsonLine123.txt'
        #strNameBin = './binFilePirsonLine123.bin'
        wFileInt = open("./"+strNameInt, 'w')
        #wFileBin = open("./"+strNameBin, 'w')
        #line = list() # length - pattern.size + 1
        for i in xrange(length - pattern.size + 1):
            trial = self.intRead(col+i, row, pattern.size)
            data = pack('H', int(fabs(Pirson(trial, pattern))*100))
            #wFileBin.write(data)
            wFileInt.write(str(Pirson(trial, pattern)))
            print Pirson(trial, pattern)
            #print PirsonOld(trial, pattern)
        #return line

    def scanPartPirs(self, col, row, width, height, pattern):
        strNameInt = './files/intFilePirson_' + str(FindNumber('./files/intFilePirson_', 'txt')) + '.txt'
        strNameBin = './files/binFilePirson_' + str(FindNumber('./files/binFilePirson_', 'bin')) + '.bin'
        wFileInt = open(strNameInt, 'w')
        wFileBin = open(strNameBin, 'wb')
        for j in xrange(height - pattern.size + 1):
            for i in xrange(width - pattern.size + 1):
                trial = self.intRead(col+i, row+j, pattern.size)
                a = fabs(Pirson(trial, pattern))
                print a
                wFileInt.write(str(a)+' ')
                wFileBin.write(str(pack('f', a)))
            wFileInt.write('\n')

    def scanPartInv(self, col, row, width, height, pattern):
        strNameInt = './files/intFileInvariants_' + str(FindNumber('./files/intFileInvariants_', 'txt')) + '.txt'
        strNameProb = './files/intFileInvariantsProb_' + str(FindNumber('./files/intFileInvariantsProb_', 'txt')) + '.txt'
        strNameBinProb = './files/binFileInvariantsProb_' + str(FindNumber('./files/binFileInvariantsProb_', 'bin')) + '.bin'
        strNameBin = './files/binFileInvariants_' + str(FindNumber('./files/binFileInvariants_', 'bin')) + '.bin'
        wFileInt = open(strNameInt, 'w')
        wFileProb = open(strNameProb, 'w')
        wFileBinProb = open(strNameBinProb, 'wb')
        wFileBin = open(strNameBin, 'wb')
        invPattern = Invariants(Moments(pattern))
        for j in xrange(height - pattern.size + 1):
            for i in xrange(width - pattern.size + 1):
                trial = self.intRead(col+i, row+j, pattern.size)
                invTrial = Invariants(Moments(trial))
                euc = Euclid(invPattern, invTrial)
                #euc = JustSum(invPattern, invTrial) # This is called "euc" just not to change other lines
                euc2 = euc/1e+42
                print euc2
                prob = ProbInv(euc2)
                wFileProb.write(str(prob)+' ')
                wFileInt.write(str(euc2)+' ')
                wFileBinProb.write(str(pack('f', prob)))
                wFileBin.write(str(pack('f', euc2)))
            wFileProb.write('\n')
            wFileInt.write('\n')


    def getOriginal(self, col, row, width, height):
        #strNameOrig = './files/intFileOrig.txt'
        strNameBinOrig = './files/binFileOrig.bin'
        #wFileOrig = open(strNameOrig, 'w')
        wFileBinOrig = open(strNameBinOrig, 'wb')
        for j in xrange(height):
            for i in xrange(width):
                orig = self.intRead(col+i, row+j, 1)
                intOrig = orig.getCont()[0][0]
                binOrig = pack('H', orig.getCont()[0][0])
                #wFileOrig.write(str(intOrig)+' ')
                wFileBinOrig.write(str(binOrig))
            #wFileOrig.write('\n')

    def testBin(self):
        strName1 = './files/testBin_1.bin'
        wFile = open(strName1, 'wb')
        for i in xrange(100):
            for j in xrange(100):
                b = pack('f', (i + j)/13.0)
                wFile.write(str(b))

    def scanFull(self, pattern):
        strNameBin = './files/binFilePirsonFull.bin'
        wFileBin = open("./"+strNameBin, 'w')
        for j in xrange(self.height - pattern.size + 1):
            for i in xrange(self.width - pattern.size + 1):
                trial = self.intRead(i, j, pattern.size)
                data = pack('H', int(fabs(Pirson(trial, pattern))*100))
                wFileBin.write(data)
                #line.append(Pirson(trial, pattern))
                #print Pirson(trial, pattern)


def ProbInv(number, a1=1.5, a2=2.5, a3=3.5):
    if number <= a1:
        return 3
    else:
        if number <= a2:
            return 2
        else:
            if number <= a3:
                return 1
            else:
                return 0


def ProbCor(number, a1=0.4, a2=0.3, a3=0.2):
    if number >= a1:
        return 3
    else:
        if number >= a2:
            return 2
        else:
            if number >= a3:
                return 1
            else:
                return 0
