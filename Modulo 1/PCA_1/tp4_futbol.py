from utils.data_utils import get_data_from_url
from utils.pca_utils import get_pca_data_matrix
from utils.plot_utils import plotData

url = "data/futbol.data"
X, y = get_data_from_url(url)

# print("DATA:\n", X)
# print("Y:\n", y)
# input()
optimal_data_matrix = get_pca_data_matrix(X, optimal_value_percentage = .90)

# Plot optimal data
plotData(optimal_data_matrix, y, y)