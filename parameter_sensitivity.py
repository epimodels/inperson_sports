import os
import stochpy
import random
import numpy as numpy
from scipy import stats

workingdir = os.getcwd()

# Simulation parameters
start_time = 0.0
end_time = 109
n_runs = 1000
batch_num = 25


# Run is a single run of the model that returns the number of incident cases
def Control(pdict):
	model = stochpy.SSA()
	model.Model(model_file='no_football.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.ChangeParameter('sigma',pdict['sigma']*0.5)
	model.ChangeParameter('gamma',pdict['gamma']*0.1960784)
	model.ChangeParameter('alpha',pdict['alpha']*0.80)
	model.ChangeParameter('delta_I',pdict['delta_I']*0.2)
	model.ChangeParameter('delta_A',pdict['delta_A']*0.2)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	return cases

def Football(pdict):
	model = stochpy.SSA()
	model.Model(model_file='football_highmix_highprev.psc',dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.ChangeParameter('sigma',pdict['sigma']*0.5)
	model.ChangeParameter('gamma',pdict['gamma']*0.1960784)
	model.ChangeParameter('alpha',pdict['alpha']*0.80)
	model.ChangeParameter('delta_I',pdict['delta_I']*0.20)
	model.ChangeParameter('delta_A',pdict['delta_A']*0.20)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	return cases
	
def Batch(iterations,pdict,type):
	results_holder = numpy.zeros([iterations,1])
	for i in range(0,iterations):
		if type=="fb":
			single_run = Football(pdict=pdict)
		elif type=="nfb":
			single_run = Control(pdict=pdict)
		results_holder[i,0] = single_run
	return numpy.median(results_holder)
		
	
def Sensitivity(iterations):
    parameters = numpy.zeros([iterations,8])
    for k in range(0,iterations):
    
        pdict = {
        'sigma':random.uniform(0.5,1.5),
        'gamma':random.uniform(0.5,1.5),
        'alpha':random.uniform(0.5,1.25), #To keep probabilities bounded by 0 and 1
        'delta_I':random.uniform(0.5,1.5),
        'delta_A':random.uniform(0.5,1.5),
            } 
        nfb = Batch(batch_num,pdict=pdict,type="nfb")
        fb = Batch(batch_num,pdict=pdict,type="fb")
        ratio = fb/nfb
        parameters[k,0] = nfb
        parameters[k,1] = fb
        parameters[k,2] = ratio 
        parameters[k,3] = pdict['sigma']
        parameters[k,4] = pdict['gamma']
        parameters[k,5] = pdict['alpha']
        parameters[k,6] = pdict['delta_I']
        parameters[k,7] = pdict['delta_A']
        print("*** Iteration %i of %i ***" % (k+1,n_runs))
    return parameters

sweep = Sensitivity(n_runs)
print("Sweep Complete")
numpy.savetxt('football_sweep.csv',sweep,delimiter=',',header="NFB,FB,Ratio,Sigma,Gamma,Alpha,Delta_I,Delta_A",comments='')
