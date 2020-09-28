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
	S > E + Incident
	betaF * S * (VI/(S+I+E+A+R+VI+VS))

R3:
	E > I + Symptomatic
	gamma * alpha * E

R4:
	E > A
	gamma * (1-alpha) * E

R5:
	I > R
	delta_I * I

R6:
	A > R
	delta_A * A

# Events
Event: Game1, _TIME_ > 18, 0
{
	betaF = 0.125
}

Event: Game1Off, _TIME_ > 20, 0
{
	betaF = 0
}

Event: Game2, _TIME_ > 25, 0
{
	betaF = 0.125
}

Event: Game2Off, _TIME_ > 27, 0
{
	betaF = 0
}

Event: Game3, _TIME_ > 39, 0
{
	betaF = 0.125
}

Event: Game3Off, _TIME_ > 41, 0
{
	betaF = 0
}

Event: Game4, _TIME_ > 46, 0
{
	betaF = 0.125
}

Event: Game4Off, _TIME_ > 48, 0
{
	betaF = 0
}

Event: Game5, _TIME_ > 67, 0
{
	betaF = 0.125
}

Event: Game5Off, _TIME_ > 69, 0
{
	betaF = 0
}

Event: Game6, _TIME_ > 88, 0
{
	betaF = 0.125
}

Event: Game6Off, _TIME_ > 90, 0
{
	betaF = 0
}

# Compartments
VS = 9990
VI = 10
S = 19990
E = 0
I = 10
A = 0
R = 0
Incident = 0
Symptomatic = 0

#Parameters:
beta = 0.30
betaF = 0.0
sigma = 0.5 # relative transmissibility of asymptomatic individuals
gamma = 1/5.1
alpha = 0.80 # Percent who end up symptomatic
delta_I = 1/5
delta_A = 1/5

FIX: betaF
