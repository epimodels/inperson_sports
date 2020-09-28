import os
import stochpy
import numpy as numpy

workingdir = os.getcwd()

# Simulation parameters
start_time = 0.0
end_time = 109
n_runs = 1000
scenarios = 10

# Model output storage arrays

results = numpy.empty([n_runs*scenarios,3], dtype = object)

def LowControl(iteration, scen):
	model = stochpy.SSA()
	model.Model(model_file='no_football.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 0
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom

def HighControl(iteration, scen):
	model = stochpy.SSA()
	model.Model(model_file='no_football.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.30)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 1
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom

def LowBetaLowPrevLowMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_lowmix_lowprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 2
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom

def LowBetaLowPrevHighMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_highmix_lowprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 3
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom
	
def LowBetaHighPrevLowMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_lowmix_highprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 4
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom

def LowBetaHighPrevHighMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_highmix_highprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.25)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 5
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom
	
def HighBetaHighPrevLowMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_lowmix_highprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.30)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 6
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom

def HighBetaHighPrevHighMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_highmix_highprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.30)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 7
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom	

def HighBetaLowPrevLowMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_lowmix_lowprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.30)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 8
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom

def HighBetaLowPrevHighMix(iteration,scen):
	model = stochpy.SSA()
	model.Model(model_file='football_highmix_lowprev.psc', dir=workingdir)
	model.Endtime(end_time)
	model.ChangeParameter('beta',0.30)
	model.DoStochSim()
	model.GetRegularGrid(n_samples=end_time)
	outcomes = model.data_stochsim_grid.species
	cases = outcomes[2][0][-1]
	symptom = outcomes[4][0][-1]
	results[iteration+(n_runs*scen),0] = 9
	results[iteration+(n_runs*scen),1] = cases
	results[iteration+(n_runs*scen),2] = symptom	
	
for i in range(0,n_runs):
	print("*** Iteration %i of %i ***" % (i+1,n_runs))
	LowControl(i,0)
	HighControl(i,1)
	LowBetaLowPrevLowMix(i,2)
	LowBetaLowPrevHighMix(i,3)
	LowBetaHighPrevLowMix(i,4)
	LowBetaHighPrevHighMix(i,5)
	HighBetaHighPrevLowMix(i,6)
	HighBetaHighPrevHighMix(i,7)
	HighBetaLowPrevLowMix(i,8)
	HighBetaLowPrevHighMix(i,9)

numpy.savetxt('wsu_football.csv',results,delimiter=',',header="Scenario,Cases,Symptomatic",comments='')
	