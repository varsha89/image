
from Smatrix import *


def readSmatFile(name, size):
    res = Smatrix(size)
    res.fillSmat()
    rFile = open(name, 'r')
    arr = rFile.read().split()
    for i in xrange(size):
        for j in xrange(size):
            res.getCont()[i][j] = int(arr[j*size + i])
    return res


def FileCheck(name, number, type):
    try:
        open(name + str(number) + '.' + type, 'r')
        print 'file exists'
        return 0
    except IOError:
        print 'file ok'
        return -1
    pass


def FindNumber(name, type='txt'):
    fileExists = 0
    number = 1
    while fileExists != -1:
        number += 1
        fileExists = FileCheck(name, number, type)
    print 'number found'
    return number
