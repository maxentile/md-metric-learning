# md-metric-learning
Benchmarking metric learning algorithms for constructing Markov models from molecular dynamics data

## Overview
We would like to construct simple models from all-atom simulations. One way to do this is to construct Markov State Models, where we project the observed dynamics onto discrete states and estimate transition rates between these states. Performing this discretization requires that the observed configurations be clustered using a suitable metric.

Here we benchmark a variety of approaches for learning an appropriate metric from simulation trajectories.

### Metric learning approaches considered
The input objects are configurations, N-by-3 matrices containing the raw 3D coordinates of each of the N atoms in the molecule.

There are two main ways we can represent a metric over configurations: (1) we can directly compute a distance between the input objects (for example, by computing the [RMSD](https://en.wikipedia.org/wiki/Root-mean-square_deviation_of_atomic_positions)), (2) we can embed the input objects into a vector space where Euclidean distance might be meaningful (for example, by representing each configuration with a weighted feature vector).

#### List of metric learning algorithms
- Principal Comonent Analysis (PCA)
 - Project onto eigenvectors of covariance matrix
- Time-structured independent component analysis (tICA)
 - Solution to generalized eigenvalue problem with a covariance matrix and a symmetrized time-lagged covariance matrix
- Nonequilibrium-tICA
 - tICA, but with unsymmetric time-lagged covariance matrices
- Slow Feature Analysis (SFA)
 - Equivalent to tICA with lag-time 1
- Kernel PCA (KPCA)
 - Dual-space formulation of PCA,
- Probabilistic PCA (PPCA)
 - Rephrasing of PCA as a latent variable model, with observations modeled as linear projections of the latent variables, corrupted with Gaussian noise.
- Factor analysis (FA)
 - Generalization of PPCA to non-isotropic Gaussian noise
- Gaussian Process Latent Variable Model (GP-LVM)
 - Generalization of PPCA where the mapping from latent space to observed space is modeled as a GP instead of a linear transformation
- Deep autoencoder
 - Train a multilayer perceptron to reconstruct its own inputs, with constraints to force the hidden layers to learn compressed representations.
- Root mean squared deviation (RMSD)
 - Average of the squared distance between corresponding atoms after alignment
- Weighted RMSD
 - RMSD, but with variable weights on each atom
 - Weights can be learned from a fixed reference ([RMSF](https://en.wikipedia.org/wiki/Root_mean_square_fluctuation))
 - Weights can be learned from a sliding window of fixed lag-time
