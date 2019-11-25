from utils.data_utils import get_data_from_url
from utils.pca_utils import get_pca_data_matrix
from utils.plot_utils import plotData

# from URL https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
url = "data/iris.data"
data_labels = ['lng sepalo','anch sepalo','lng petalo','anch petalo','especie']

X, y = get_data_from_url(url, data_labels)
print("\nX:", X)
print("\ny:", y)
optimal_data_matrix = get_pca_data_matrix(X, optimal_value_percentage = .8)

# Plot optimal data
y_labels = ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica')
plot_colors = ('magenta', 'cyan', 'limegreen')
plotData(optimal_data_matrix, y, y_labels, plot_colors)