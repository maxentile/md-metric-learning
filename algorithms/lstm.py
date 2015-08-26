# adapted from the Keras LSTM text generation example

# basic imports
import numpy as np
import matplotlib.pyplot as plt

# load FsPeptide simulation data, featurize
from msmbuilder.example_datasets import FsPeptide
from msmbuilder.featurizer import DihedralFeaturizer

fs = FsPeptide().get().trajectories
n_atoms = fs[0].n_atoms
fs_dih_feat = DihedralFeaturizer().transform(fs)

# cut the sequence into semi-redundant sequences of maxlen steps

# given sequential frames i..i+maxlen as input
# redict the i+maxlen+1th frame
maxlen = 10
step = 3
sequences = []
next_frames = []
for ind,traj in enumerate(fs_dih_feat):
    if ind < 
    for i in range(0, len(traj) - maxlen, step):
        sequences.append(traj[i : i + maxlen])
        next_frames.append(traj[i + maxlen])
print('nb sequences:', len(sequences))
ndim = fs_dih_feat[0].shape[1]
print('nb sequences:', ndim)

X = np.zeros((len(sequences), maxlen, ndim))
y = np.zeros((len(sequences), ndim))
for i, sequence in enumerate(sequences):
    X[i] = sequences[i]
    y[i] = next_frames[i]



# build an LSTM
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.optimizers import SGD

print('Build model...')
model = Sequential()
model.add(LSTM(ndim, ndim*2, return_sequences=True))
#model.add(Dropout(0.2))
model.add(LSTM(ndim*2, ndim*2, return_sequences=False))
#model.add(Dropout(0.2))
model.add(Dense(ndim*2, ndim))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error', optimizer=sgd)

#
