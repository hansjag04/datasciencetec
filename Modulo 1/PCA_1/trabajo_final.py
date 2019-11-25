from utils.data_utils import get_data_from_url, get_data_from_url_without_first
from utils.pca_utils import get_pca_data_matrix
from utils.plot_utils import plotData

# from URL https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
url = "data/pima-indians-diabetes.csv"
# data_labels = ['lng sepalo','anch sepalo','lng petalo','anch petalo','especie']
data_labels = [
"Concentración de glucosa en plasma",
"Presión sanguínea diastólica",
"Grosor de los pliegues cutáneos",
"Concentración de insulina en suero a las 2 horas",
"Índice de masa corporal",
"Función de herencia de diabetes",
"Edad",
"Es diabetico"
]

X, y = get_data_from_url_without_first(url, data_labels)
print("X: ", X)
print("y: ", y)


optimal_data_matrix = get_pca_data_matrix(X, optimal_value_percentage = 0.40)

print("X: ", optimal_data_matrix)


# Plot optimal data
y_labels = ('1', '0')

plot_colors = ('magenta', 'cyan')
plotData(optimal_data_matrix, y, y_labels, plot_colors)