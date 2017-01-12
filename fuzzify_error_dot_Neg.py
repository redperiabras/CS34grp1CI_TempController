#*************************************************************************#
# @BeginVerbatim
# Title: Fuzzy Controller for Thermal Control System by implementing FL
# Description: Given the target temperature, we need to control and balance
#              it by determining the degree of error and error dot of a
#              temperature, and to respond by cooling, heating or no change
# Filename: fuzzify_error_dot_Neg.py
# Version: v01.00
# Author/Group: Group 1
# Yr&Sec: BSCS 3-4
# Subject: Computational Intelligence
# @EndVerbatim
#*************************************************************************#

    # @function fuzzify_error_dot_Neg
	# @param fError_dot ---> change of temperature over time
	# @returns fError_dot_Neg ---> fuzzified error_Dot in membership
    #                              function Negative.
	# @Description: Given the set of rules for membership function Negative
    #                , it determines the degree of membership of the
    #                error_dot.

def fuzzify_error_dot_Neg(fError_dot):
#@Initialization
    #
    fError_dot_Neg = 0
    #slope of a line between coordinates x1(-1, 0) and x2(-1.5, 1)
    fError_dot_Neg_slope = (-2 * fError_dot) - 2
#***************

#@Code Body
    #rule for membership function Negatie of error dot
    if((fError_dot >= -5) and (fError_dot <= -1.5)):
        fError_dot_Neg = 1 #maximum membership value

    elif((fError_dot > -1.5) and (fError_dot < -1)):
        fError_dot_Neg = fError_dot_Neg_slope

    elif((fError_dot > -1) and (fError_dot <= 5)):
        fError_dot_Neg = 0 #minimum membership value

    return fError_dot_Neg
#**********