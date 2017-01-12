#*************************************************************************#
# Title: Running Temperature Control Fuzzy
# Description: Room Temperature Controller based on Fuzzy Logic which tries
#              to reach a given target temperature by measuring the
#              difference between the current and previous temperature
#              along with the target temperature.
# Filename: RunTempConFuzzy.py
# Version: v00.01
# Author: Group 1
# Yr&Sec: BSCS 3-4 (CSR)
# Subject: Computational Intelligence (CS-ELEC 2)
#*************************************************************************#

# Last Review by: Redentor Periabras, January 12, 2016

import sys
import os
from EvaluateRules import EvaluateRules
from EvaluateOutput import EvaluateOutput
from FISAggregation import FISAggregation


def main(argv):
    error, errordiv = setParams()
    print("Error: " + str(error))
    print("Error Derivative: " + str(errordiv))

    rules = EvaluateRules(error, errordiv)
    print("\n Rules: ")
    print(rules)
    print("\n")
    h1, h2, h3 = EvaluateOutput()
    ArrAgg = FISAggregation(rules, h1, h2, h3)
    print("Aggregation: ")
    for i in range (len(ArrAgg)):
        print(i," : ",ArrAgg[i])
    Centroid = getCentroid(ArrAgg)

    print("Centroid: " + str(Centroid))

def setParams():

    try:
        # temp_target = float(input("Enter Target Temperature: "))
        # temp_curr = float(input("Enter Current Temperature: "))
        # temp_prev = float(input("Enter Previous Temperature: "))
        temp_target = 39
        temp_curr = 40
        temp_prev = 35
    except ValueError:
        print("Invalid Input")
        os.system("cls")
        sys.exit(1)

    errorPrev = temp_target - temp_prev
    error = temp_target - temp_curr
    errordiv = error - errorPrev
    return (error, errordiv)

def getCentroid(ArrAgg):
    n = len(ArrAgg)
    xAxis = [i+1 for i in range(n)] #list with values of 1, 2, ... , n

    centroidDenum = 0
    centroidNum = 0

    for i in range(n):
        print("x: ",i+1," - ", ArrAgg[i]," ")

        centroidNum += (xAxis[i] * ArrAgg[i])
        centroidDenum += ArrAgg[i]


    print(centroidNum)
    print(centroidDenum)

    return centroidNum/centroidDenum

if __name__ == "__main__":
    main(sys.argv)