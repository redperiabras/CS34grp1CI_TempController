from fuzzify_error_dot_Neg import fuzzify_error_dot_Neg
from fuzzify_error_dot_Pos import fuzzify_error_dot_Pos
from fuzzify_error_dot_Zero import fuzzify_error_dot_Zero
from fuzzify_error_Neg import fuzzify_error_Neg
from fuzzify_error_Pos import fuzzify_error_Pos
from fuzzify_error_Zero import fuzzify_error_Zero

def EvaluateRules(e, ediv):

    #column, row
    rules = [[0 for i in range(3)] for j in range(9)] #3x9 matrix of 0's
    i8_arrVal1 = 0
    i8_arrVal2 = 0
    u16_value = 0

    #RULE 1
    i8_arrVal1 = fuzzify_error_Neg(e)
    i8_arrVal2 = fuzzify_error_dot_Neg(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    #column 1, row 1
    rules[0][0] = u16_value #for C
    rules[0][1] = 0         #for NC
    rules[0][2] = 0         #for H

    #RULE 2
    i8_arrVal1 = fuzzify_error_Zero(e)
    i8_arrVal2 = fuzzify_error_dot_Neg(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[1][0] = 0         # for C
    rules[1][1] = 0         # for NC
    rules[1][2]= u16_value # for H

    #RULE 3
    i8_arrVal1 = fuzzify_error_Pos(e)
    i8_arrVal2 = fuzzify_error_dot_Neg(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[2][0] = 0  # for C
    rules[2][1] = 0  # for NC
    rules[2][2] = u16_value  # for H

    #RULE 4
    i8_arrVal1 = fuzzify_error_Neg(e)
    i8_arrVal2 = fuzzify_error_dot_Zero(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[3][0] = u16_value # for C
    rules[3][1] = 0  # for NC
    rules[3][2] = 0  # for H

    #RULE 5
    i8_arrVal1 = fuzzify_error_Zero(e)
    i8_arrVal2 = fuzzify_error_dot_Zero(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[4][0] = 0  # for C
    rules[4][1] = u16_value  # for NC
    rules[4][2] = 0  # for H

    # RULE 6
    i8_arrVal1 = fuzzify_error_Pos(e)
    i8_arrVal2 = fuzzify_error_dot_Zero(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[5][0] = 0  # for C
    rules[5][1] = 0  # for NC
    rules[5][2] = u16_value  # for H

    # RULE 7
    i8_arrVal1 = fuzzify_error_Neg(e)
    i8_arrVal2 = fuzzify_error_dot_Pos(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[6][0] = u16_value # for C
    rules[6][1] = 0  # for NC
    rules[6][2] = 0  # for H

    # RULE 8
    i8_arrVal1 = fuzzify_error_Zero(e)
    i8_arrVal2 = fuzzify_error_dot_Pos(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[7][0] = u16_value  # for C
    rules[7][1] = 0  # for NC
    rules[7][2] = 0  # for H

    # RULE 9
    i8_arrVal1 = fuzzify_error_Pos(e)
    i8_arrVal2 = fuzzify_error_dot_Pos(ediv)
    if(i8_arrVal1 >= i8_arrVal2):
        u16_value = i8_arrVal2
    else:
        u16_value = i8_arrVal1
    rules[8][0] = 0  # for C
    rules[8][1] = 0  # for NC
    rules[8][2] = u16_value  # for H

    return rules