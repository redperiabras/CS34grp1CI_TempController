#*************************************************************************#
# @BeginVerbatim
# Title: Fuzzy Controller for Thermal Control System by implementing FL
# Description: Given the target temperature, we need to control and balance
#              it by determining the degree of error and error dot of a
#              temperature, and to respond by cooling, heating or no change
# Filename: fuzzify_error_dot_Zero.py
# Version: v01.00
# Author/Group: Group 1
# Yr&Sec: BSCS 3-4
# Subject: Computational Intelligence
# @EndVerbatim
#*************************************************************************#

    # @function fuzzify_error_dot_Zero
	# @param fError_dot ---> change of temperature over time
	# @returns fError_dot_Zero ---> fuzzified error_Dot in membership
    #                              function Zero.
	# @Description: Given the set of rules for membership function Zeroative
    #                , it determines the degree of membership of the
    #                error_dot.

def fuzzify_error_dot_Zero(fError_dot):
#@Initialization
    #
    fError_dot_Zero = 0

    #slope of a line between coordinates x1(-2, 0) and x2(0, 1)
    fError_dot_Zero_slope1 = (0.5 * fError_dot) + 1

    #slope of a line between coordinates x1(2, 0) and x2(0, 1)
    fError_dot_Zero_slope2 = (-0.5 * fError_dot) + 1
#***************

#@Code Body
    #rule for membership function Zero of error dot
    if((fError_dot <= -2) or (fError_dot >= 2)):
        fError_dot_Zero = 0 #minimum membership value

    elif((fError_dot > -2) and (fError_dot < 0)):
        fError_dot_Zero = fError_dot_Zero_slope1

    elif((fError_dot > 0) and (fError_dot < 2)):
        fError_dot_Zero = fError_dot_Zero_slope2
        
    else:
        fError_dot_Zero = 1 #maximum membership value

    return fError_dot_Zero
#**********