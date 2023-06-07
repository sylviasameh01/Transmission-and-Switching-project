#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:47:11 2023

@author: sylviasameh
"""

from scipy.stats import erlang


Area=250
noofuserskm=4000
avgnocallsday=10/(60*24)
avgcallduration=1
maxchannels_cell=25
blockingprob=0.02

i=0

sectoringarr=[10,120,180,360]

totalnoofusers=Area*noofuserskm



full_duplex=8/2

aofuser=avgnocallsday*avgcallduration
    


from scipy.optimize import brentq
import math

def erlang_b_formula(load, trunks):
    return (load ** trunks / math.factorial(trunks)) / sum([(load ** i) / math.factorial(i) for i in range(trunks + 1)])

def find_offered_load(pdrop, trunks, initial_load, tolerance, max_iterations):
    load = initial_load
    difference = erlang_b_formula(load, trunks) - pdrop
    iteration = 0

    while abs(difference) > tolerance and iteration < max_iterations:
        load =load-( difference )  
        #print(load)
        difference = erlang_b_formula(load, trunks) - pdrop
        iteration += 1
    #print(iteration)
    if iteration == max_iterations:
        print("Maximum iterations reached and the offered load wasn't calculated")

    return load
length=len(sectoringarr)

for i in range (length):
    noofsectors=360/sectoringarr[i]
    print(noofsectors)
    nooftrunks=(int) ((maxchannels_cell*full_duplex)/noofsectors)
    OfferedLoad = find_offered_load(blockingprob,nooftrunks,0,1e-6,10000000)
    noofusers=(OfferedLoad*noofsectors)/aofuser
    noofcells=totalnoofusers/noofusers
    print("Number of Cells:")
    print(noofcells)
    




