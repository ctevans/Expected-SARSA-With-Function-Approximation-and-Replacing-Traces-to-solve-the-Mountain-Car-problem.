import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy

numRuns = 1
numEpisodes = 200
alpha = 005/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings

runSum = 0.0
for run in xrange(numRuns):
    theta = -0.01*rand(n)
    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        #...
        # your code goes here (20-30 lines, depending on modularity)
        #...
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()


