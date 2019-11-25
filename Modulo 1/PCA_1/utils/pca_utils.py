from utils.plot_utils import plotExplainedVariation
from utils.statistics_utils import *

'''
Calculates how many dimensions will have the most optimal variation information
This assumes that the explained variation array is sorted descendent
'''
def dimensionsWithMostVariance(explained_variation_array, optimal_value_percentage = .9):
    for max_optimal_dimensions in range(1, len(explained_variation_array) + 1):
        optimal_variation = sum(explained_variation_array[:max_optimal_dimensions])
        if optimal_variation >= optimal_value_percentage*100:
            return max_optimal_dimensions

    return len(explained_variation_array)

'''
Calculates the PCA data matrix with most optimal dimensions with most variation
from data eigen values/vectors and normalized data matrix

Takes an optional percentage to calculate max number of dimensions needed to reach that optimal value 
'''
def get_optimal_data_matrix(eigen_pairs, optimal_dimensions, normalized_data_matrix):
    eigen_vectors = []
    for i in range(optimal_dimensions):
        # This step selects the appropriate dimension with more variation information
        eigen_vectors.append(eigen_pairs[i][1].reshape(len(normalized_data_matrix[0]), 1))

    # New matrix will be a stack of eigenvectors for each dimension
    optimal_eigen_vectors = np.hstack(tuple(eigen_vectors))
    return normalized_data_matrix.dot(optimal_eigen_vectors)

'''
Calculates the PCA data matrix with most optimal dimensions with most variation
from non-normalized data

Takes an optional percentage to calculate max number of dimensions needed to reach that optimal value 
'''
def get_pca_data_matrix(data_matrix, optimal_value_percentage = .9):
    X_standard = get_standarized_data(data_matrix)
    X_covariance = get_covariance_matrix(X_standard)
    print("\nMATRIZ DE COV:\n", X_covariance)
    eigen_values, eigen_vectors, eigen_pairs = get_eigens_from_data_covariance_matrix(X_covariance)
    explained_variation, cumulative_explained_variation = get_explained_variation(eigen_values)

    plotExplainedVariation(explained_variation, cumulative_explained_variation)

    optimal_dimensions = dimensionsWithMostVariance(explained_variation, optimal_value_percentage=optimal_value_percentage)
    print("Number of optimal dimensions with %f%%: %d" % (optimal_value_percentage*100, optimal_dimensions))

    return get_optimal_data_matrix(eigen_pairs, optimal_dimensions, X_standard)
