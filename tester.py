__author__='Josh Fass'

''' Class for testing DR algorithms on
a suite of example problems, comparing
all combinations of '''

from metric_learners import learner_dict
from sklearn.decomposition import PCA
from msmbuilder.example_datasets import AlanineDipeptide
from msmbuilder.featurizer import RawPositionsFeaturizer

ala = AlanineDipeptide().get().trajectories

# define the algorithms and the hyper parameters to sweep over
algorithms=learner_dict
datasets =[ala]
featurizers = [RawPositionsFeaturizer]

# to-dos: need to be flexible enough to accomodate distance functions
# as well as projection functions

for dataset in datasets:
    for featurizer in featurizers:
        feat_traj = featurizer().fit_transform(ala)
        for (name,algorithm) in algorithms.items():
            # do grid search over algorithm hyperparameters
            alg = algorithm()
            transformed = alg.fit_transform(feat_traj)
