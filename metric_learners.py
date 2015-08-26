__author__='Josh Fass'

''' contains all metric learning algorithms
under consideration'''

from msmbuilder.decomposition import tICA

class MetricLearner():
    ''' abstract class representing a metric learning
    algorithm that can either embed an object into a
    vector space compute the distance'''

    def __init__(self,):

        # if you can

        # if you transform the 
        self.greedy_selectable = True

learner_dict = {'tICA':tICA}
