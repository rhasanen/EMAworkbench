'''
Created on 20 May, 2011

This module shows how you can use vensim models directly
instead of coding the model in Python. The underlying case
is the same as used in fluExample

.. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
                epruyt <e.pruyt (at) tudelft (dot) nl>
'''
import time

from expWorkbench import SimpleModelEnsemble, ParameterUncertainty,\
                         Outcome, save_results
from expWorkbench.vensim import VensimModelStructureInterface 
import expWorkbench.EMAlogging as logging

class FluModel(VensimModelStructureInterface):
    #base case model
    modelFile = r'\FLUvensimV1basecase.vpm'
        
    #outcomes
    outcomes = [Outcome('deceased population region 1', time=True),
                Outcome('infected fraction R1', time=True)]
 
    #Plain Parametric Uncertainties 
    uncertainties = [
        ParameterUncertainty((0, 0.5), 
                             "additional seasonal immune population fraction R1"),
        ParameterUncertainty((0, 0.5), 
                             "additional seasonal immune population fraction R2"),
        ParameterUncertainty((0.0001, 0.1), 
                             "fatality ratio region 1"),
        ParameterUncertainty((0.0001, 0.1), 
                             "fatality rate region 2"),
        ParameterUncertainty((0, 0.5), 
                             "initial immune fraction of the population of region 1"),
        ParameterUncertainty((0, 0.5), 
                             "initial immune fraction of the population of region 2"),
        ParameterUncertainty((0, 0.9), 
                             "normal interregional contact rate"),
        ParameterUncertainty((0, 0.5), 
                             "permanent immune population fraction R1"),
        ParameterUncertainty((0, 0.5), 
                             "permanent immune population fraction R2"),
        ParameterUncertainty((0.1, 0.75), 
                             "recovery time region 1"),
        ParameterUncertainty((0.1, 0.75), 
                             "recovery time region 2"),
        ParameterUncertainty((0.5,2), 
                             "susceptible to immune population delay time region 1"),
        ParameterUncertainty((0.5,2), 
                             "susceptible to immune population delay time region 2"),
        ParameterUncertainty((0.01, 5), 
                             "root contact rate region 1"),
        ParameterUncertainty((0.01, 5), 
                             "root contact ratio region 2"),
        ParameterUncertainty((0, 0.15), 
                             "infection ratio region 1"),
        ParameterUncertainty((0, 0.15), 
                             "infection rate region 2"),
        ParameterUncertainty((10, 100), 
                             "normal contact rate region 1"),
        ParameterUncertainty((10, 200), 
                             "normal contact rate region 2")]
                         
        
if __name__ == "__main__":
    logging.log_to_stderr(logging.INFO)
        
    model = FluModel(r'..\..\models\flu', "fluCase")
    ensemble = SimpleModelEnsemble()
    ensemble.set_model_structure(model)
    
    ensemble.parallel = True #turn on parallel processing

    startTime = time.time()
    results = ensemble.perform_experiments(1000)
    
    print time.time()-startTime
    save_results(results, r'../../src/analysis/1000 flu cases no policy.cPickle')