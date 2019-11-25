import numpy as np
from sklearn.preprocessing import StandardScaler

'''
Transforms the data matrix in a normalized data matrix
It's used to apply properties from the normal distribution
'''
def get_standarized_data(data):
    return StandardScaler().fit_transform(data)


'''
Calculates the covariance matrix from an standarized matrix
'''
def get_covariance_matrix(standarized_data):
    return np.cov(standarized_data.T)

'''
Returns the eigenvalues, eigenvectors and pairs from those two
from a data covariance matrix.

Pair of eigenvalues/eigenvectors is sorted descendent.
'''
def get_eigens_from_data_covariance_matrix(data_covariance_matrix, descendantPairs = True):
    eig_vals, eig_vecs = np.linalg.eig(data_covariance_matrix)
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i]) for i in range(len(eig_vals))]
    eig_pairs.sort(key=lambda x: x[0], reverse=descendantPairs)
    return eig_vals, eig_vecs, eig_pairs

'''
Calculate the explained variation from data's eigenvalues
Returns an array with the explained variation for each dimension,
and a cumulative explained variation with each dimension
'''
def get_explained_variation(eigen_values):
    total = sum(eigen_values)
    explained_variation = [(i / total)*100 for i in sorted(eigen_values, reverse=True)]
    cumulative_explained_variation = np.cumsum(explained_variation)
    return explained_variation, cumulative_explained_variation

