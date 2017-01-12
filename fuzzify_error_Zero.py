#*************************************************************************#
# @BeginVerbatim
# Title: zero_error function module
# Description: Compute given error in zero error in fuzzification
# Filename: fuzzify_error_Zero.py
# Version: v01.00
# Author/Group: Group 1
# Yr&Sec: BSCS 3-4
# Subject: Computational Intelligence
# @EndVerbatim
#*************************************************************************#

def fuzzify_error_Zero(fError):
#@Initialization
    #return value
    fError_Zero = 0
    #checks if fError is less than or equal to -5
    mult = 0.2
#***************

#@Code Body
    if ((fError <= -5) or (fError >= 5)):
        fError_Zero = 0

    elif ((fError >= -5) and (fError <= 0)):
        fError_Zero = (mult * fError) + 1

    elif ((fError >= 0) and (fError <= 5)):
        fError_Zero = ((-1 * (mult)) * fError) + 1

    return fError_Zero
#**********