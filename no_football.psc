#######################################################
# Simple Model of Football Season
# Author: Eric Lofgren (Eric.Lofgren@wsu.edu)
########################################################

#Descriptive Information for PML File
Modelname: COVID-19 Football
Description: PML Implementation of COVID-19 Football Model

# Set model to run with numbers of individuals
Species_In_Conc: False
Output_In_Conc: False

#Students
R1:
	S > E + Incident
	beta * S * (I/(S+I+E+A+R)) + beta*sigma * S * (A/(S+I+E+A+R))

R2:
	E > I + Symptomatic
	gamma * alpha * E

R3:
	E > A
	gamma * (1-alpha) * E

R4:
	I > R
	delta_I * I

R5:
	A > R
	delta_A * A

# Compartments
S = 19990
E = 0
I = 10
A = 0
R = 0
Incident = 0
Symptomatic = 0

#Parameters:
beta = 0.30
sigma = 0.5 # relative transmissibility of asymptomatic individuals
gamma = 1/5.1
alpha = 0.80 # Percent who end up symptomatic
delta_I = 1/5
delta_A = 1/5
