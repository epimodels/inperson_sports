import os
import stochpy
import random
import numpy as numpy
from scipy import stats

workingdir = os.getcwd()

# Simulation parameters
start_time = 0.0
end_time = 109
n_runs = 10000

def Football(beta_draw):
	model = stochpy.SSA()
	model.Model(model_file='football_beta_sweep.psc',dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('betaF',beta_draw)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	return cases
	
def Sensitivity(iterations):
	parameters = numpy.zeros([iterations,3])
	for k in range(0,iterations):
		beta_draw = random.uniform(0,0.50)
		ratio = beta_draw/0.50
		cases = Football(beta_draw)
		parameters[k,0] = beta_draw
		parameters[k,1] = ratio
		parameters[k,2] = cases
		print("*** Iteration %i of %i ***" % (k+1,n_runs))
	return parameters

sweep = Sensitivity(n_runs)
print("Sweep Complete")

numpy.savetxt('football_beta_sweep.csv',sweep,delimiter=',',header="beta,mix_ratio,cases",comments='')
