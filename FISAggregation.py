def FISAggregation(Rule, PCC, PCNC, PCH):
#*@Initialization
    fisAggregation = [0 for i in range(201)]
    fuzzy = [[0 for i in range(201)] for j in range(9)]
#****************

#*@Code Body
    for rule_no in range(9):

        # print("\nRule ",rule_no,": ",Rule[rule_no][0], Rule[rule_no][1],Rule[rule_no][2])
        
        for index in range(201):
            fuzzy[rule_no][index] = 0
            
        for index in range(201):

            # print("Controller: ",PCC[index],PCNC[index],PCH[index])

            if(Rule[rule_no][0] > 0):

                #index 0-95
                if((index >= 0) and (index <= 95)):
                    if(Rule[rule_no][0] < PCC[index]):
                        fuzzy[rule_no][index] = Rule[rule_no][0]
                    else:
                        fuzzy[rule_no][index] = PCC[index]
                else:
                    fuzzy[rule_no][index] = 0

            if((Rule[rule_no][1]) > 0):

                #index 90-110
                if((index >= 90) and (index <= 110)):
                    if(Rule[rule_no][1] < PCNC[index]):
                        fuzzy[rule_no][index] = Rule[rule_no][1]
                    else:
                        fuzzy[rule_no][index] = PCNC[index]
                else:
                    fuzzy[rule_no][index] = 0

            if(Rule[rule_no][2] > 0):

                #index 105-200
                if((index >= 105) and (index <= 200)):
                    if(Rule[rule_no][2] < PCH[index]):
                        fuzzy[rule_no][index] = Rule[rule_no][2]
                    else:
                        fuzzy[rule_no][index] = PCH[index]
                else:
                    fuzzy[rule_no][index] = 0

            # print("X-Axis: ",index," : ",fuzzy[rule_no][index])

    #resetting to zero not needed. @fisAggregation already initialized in line 3

    #assign
    for index in range(201):
        for rule_no in range(9):
            if(fisAggregation[index] < fuzzy[rule_no][index]):
                fisAggregation[index] =  fuzzy[rule_no][index]

    return fisAggregation
#***********