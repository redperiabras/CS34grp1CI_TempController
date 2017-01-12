#*************************************************************************#
# @BeginVerbatim
# Title: negative_error function module
# Description: Compute given error in negative error in fuzzification
# Filename: fuzzify_error_Neg.py
# Version: v01.00
# Author/Group: Group 1
# Yr&Sec: BSCS 3-4
# Subject: Computational Intelligence
# @EndVerbatim
#*************************************************************************#

def fuzzify_error_Neg(fError):
#@Initialization
    #return value
    fError_Neg = 0
    mult = -0.2
#***************

#@Code Body
    if (fError <= -5):
        fError_Neg = 1

    elif ((fError <= 0) and (fError > -5)):
        fError_Neg = mult * fError

    elif (fError > 0):
        fError_Neg = 0

    return fError_Neg
#**********