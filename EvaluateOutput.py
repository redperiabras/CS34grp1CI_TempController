#*******************************************************************#
# Title: Evaluate Output Module for Temperature Controller
# Description: Returns the output evaluation for the temperature
#              controller. 
# Version: 1.0
# Author :  Group 1
# Year and Section: BSCS 3-4 (CSR)
# Course : Computational Intelligence (CS-ELEC 2)
#*******************************************************************#

# au8PCC = [0 for i in range(201)]

def EvaluateOutput():
	au8OutputCooler = fuzzify_outputControl_Cooler()
	au8OutputNoChange = fuzzify_outputControl_noChange()
	au8OutputHotter = fuzzify_outputControl_Hotter()

	return (au8OutputCooler, au8OutputNoChange, au8OutputHotter)

def fuzzify_outputControl_Cooler():
#******************** @Initialization *********************#
	au8PCC_C = [0 for i in range(201)]
	dCoeffA = -0.0153846153846154
	dCoeffB = 1.46153846153846
#**********************************************************#

#*********************** @Code Body ***********************#
	for u8Counter in range(0,30):
		au8PCC_C[u8Counter] = 1

	for u8Counter in range(30, 95):
		au8PCC_C[u8Counter] = dCoeffA * u8Counter + dCoeffB

	for u8Counter in range(95, 201):
		au8PCC_C[u8Counter] = 0

	return au8PCC_C
#**********************************************************#

	
def fuzzify_outputControl_noChange():
		
#******************** @Initialization *********************#
	au8PCC_NC = [0 for i in range(201)]
	fCoeffA1 = 0.1
	fCoeffA0 = -9.0

	fCoeffB1 = -0.1
	fCoeffB0 = 11.0
#**********************************************************#
#*********************** @Code Body ***********************#
	for u8Counter in range(0,90):
		au8PCC_NC[u8Counter] = 0
	for u8Counter in range(90, 100):
		au8PCC_NC[u8Counter] = fCoeffA1 * u8Counter + fCoeffA0
	for u8Counter in range(100, 110):
		au8PCC_NC[u8Counter] = fCoeffB1 * u8Counter + fCoeffB0
	for u8Counter in range(110,201):
		au8PCC_NC[u8Counter] = 0

	return au8PCC_NC
#**********************************************************#


def fuzzify_outputControl_Hotter():
		
#******************** @Initialization *********************#
	au8PCC_H = [0 for i in range(201)]
	dCoeffA =  0.0153846153846154
	dCoeffB = -1.61538461538462
#**********************************************************#

#*********************** @Code Body ***********************#
	for u8Counter in range(0,105):
		au8PCC_H[u8Counter] = 0

	for u8Counter in range(105, 170):
		au8PCC_H[u8Counter] = dCoeffA * u8Counter + dCoeffB

	for u8Counter in range(170, 201):
		au8PCC_H[u8Counter] = 1

	return au8PCC_H
#**********************************************************#