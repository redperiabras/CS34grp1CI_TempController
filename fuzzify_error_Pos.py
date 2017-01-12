#*************************************************************************#
# @BeginVerbatim
# Title: positive_error function module
# Description: Compute given error in positive error in fuzzification
# Filename: fuzzify_error_Pos.py
# Version: v01.00
# Author/Group: Group 1
# Yr&Sec: BSCS 3-4
# Subject: Computational Intelligence
# @EndVerbatim
#*************************************************************************#

def fuzzify_error_Pos(fError):
#@Initialization
    #return value
    fError_Pos = 0

    #checks if fError is less than or equal to -5
    mult = 0.2
#***************

#@Code Body
    if (fError >= 5):
        fError_Pos = 1

    elif ((fError >= 0) and (fError <= 5)):
        fError_Pos = mult * fError

    elif (fError <= 0):
        fError_Pos = 0

    return fError_Pos
#**********