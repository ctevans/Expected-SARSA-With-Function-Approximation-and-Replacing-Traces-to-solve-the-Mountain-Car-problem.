# -*- coding: utf-8 -*-
import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  #includes numpy
import random

numRuns = 50
numEpisodes = 200
alpha = 0.05/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3 # 4 * 9 * 9 * 3
F = [-1]*numTilings # 4

# for average purpose
aveReturn = zeros((numRuns,numEpisodes))
aveStep = zeros((numRuns,numEpisodes))

def egreedy(Qs,epsilon):
    if rand() < epsilon: return randint(3) # return a random action
    else:                return argmax(Qs) # return argmax θt^T ф(S,A)
    
def expQunderPi(Qs):
    return Epi*average(Qs) + (1-Epi)*max(Qs)

def Qs(F):
    # initialize Q[S, A, F]
    # S = (position, velocity); F = ф
    Q = np.zeros(3)
    
    # numActions
    # for every possible action a in F
    for a in xrange(3):
        # numTilings
        for i in F:
            # update Qa
            Q[a] = Q[a] + theta[i + (a * numTiles)]
    return Q
            
runSum = 0.0
for run in xrange(numRuns):
    theta = -0.01*rand(n)
    returnSum = 0.0
    
    for episodeNum in xrange(numEpisodes):
        G = 0

        step = 0

        # initialize state
        S = mountaincar.init()
        
        # initialize e (eligibility trace vector)
        e = np.zeros(n)
        
        # repeat for each step of episode
        while S is not None:

            # initialize A 
            A = 0
            
            # get a list of four tile indices
            tilecode(S[0], S[1], F)
            
            Q = Qs(F)
            
            # pick the action
            A = egreedy(Q, Emu)
            
            # observe reward, and next state
            R, Sprime = mountaincar.sample(S, A)
            
            delta = R - Q[A]
            
            G = G + R
            
            for i in F:
                # replacing traces
                e[i + (A*numTiles)] = 1
            
            # if S' is terminal, then update theta; go to next episode
            if Sprime == None:
                theta = theta + alpha * delta * e
		break
            
            tilecode(Sprime[0], Sprime[1], F)
            
            Qprime = Qs(F)
            
            delta = delta + expQunderPi(Qprime)
            
            # update theta
            theta = theta + alpha * delta * e
            
            # update e
            e = gamma * lmbda * e
            
            # update current state to next state for next iteration
            S = Sprime
            
            step = step + 1
        
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G

        # average 
        aveReturn[run][episodeNum] = G
        aveStep[run][episodeNum] = step

        returnSum = returnSum + G
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

def writeAve(filename, array):
    fout = open(filename, 'w')
    ave = zeros(numEpisodes)
    for i in range(numEpisodes):
        ave[i] = average(array[:,i])
        fout.write(repr(ave[i]) + ' ')
        fout.write('\n')
    fout.close()

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

writeF()
writeAve("aveReturn", aveReturn)
writeAve("aveStep", aveStep)
