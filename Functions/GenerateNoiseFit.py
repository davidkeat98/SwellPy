from StatisticalRecognition import *
import numpy as np

def rateData(Nlist, areaFrac, Min, Max, incr, iterPerN, dataFilename = "rateNoiseData.txt"):
	"""
	Generate the mean noise rate values for a range of particle system sizes. 

	Parameters
	----------
		Nlist: 1D int array-like object
			A list or array-like object of ints that represent the number of particles
			for which data will be collected
		areaFrac: float
				Total particle area to box area ratio at swell of 1.0
		Min: float
            The minimum swollen diameter length
        Max: float
            The maximum swollen diameter length, inclusive
        incr: float
            The step size of diameter length when increasing from Min to Max
        iterPerN: int
        	The number of times noise values are taken as if it were a single paticle 
        	system. The number of times values are measured for each system size
        	is avgIters/N
        dataFilename: str, optional
        	The name of the file where the data will be stored. Default is "rateNoiseData.txt"

	"""
	x = StatisticalRecognition()
	(mean, sd) = x.rateNoiseCollect(Nlist, Min, Max, incr, iterPerN)
	header = "Areafrac: %0.4lf, Incr: %0.4lf, IterPerN: %d\nN,mean,sd" %(areaFrac, incr, iterPerN)
	x.save(dataFilename, [Nlist, mean, sd], header)