import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import plotly.express as px

def get_cmap(n):
    return cm.rainbow(np.linspace(0, 1, n))


'''
Plots the explained variation as bars with a step for the cumulative explained variation
'''
def plotExplainedVariation(explained_variation, cumulative_explained_variation):
    with plt.style.context('seaborn-pastel'):
        plt.figure(figsize=(6, 4))
        plt.bar(range(len(explained_variation)), explained_variation, alpha=0.5, align='center',
                label='Varianza individual explicada', color='g')
        plt.step(range(len(explained_variation)), cumulative_explained_variation, where='mid', linestyle='--', label='Varianza explicada acumulada')
        plt.ylabel('Ratio de Varianza Explicada')
        plt.xlabel('Componentes Principales')
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

'''
Plots data in 1-3D maximum
'''
def plotData(optimal_data_matrix, data_Y, data_Y_labels, colors=None):
    if colors is None or len(data_Y_labels) != len(colors):
        colors = get_cmap(len(data_Y))

    if len(optimal_data_matrix[0]) > 4:
        print("Error before plotting: Can't plot with more than 4 dimensions")
        return

    if len(optimal_data_matrix[0]) == 1:
        plot1dData(optimal_data_matrix, data_Y, data_Y_labels, colors)
        return

    if len(optimal_data_matrix[0]) == 2:
        # plot2dData(optimal_data_matrix, data_Y, data_Y_labels, colors)
        plot3dDataExpress()
        return

    if len(optimal_data_matrix[0]) == 3:
        # plot3dData(optimal_data_matrix, data_Y, data_Y_labels, colors)
        plot3dDataExpress()
        return

    if len(optimal_data_matrix[0]) == 4:
        plot4dData(optimal_data_matrix, data_Y, data_Y_labels, colors)
        return




'''
Plots 1D matrix with Y results labels and colors
'''
def plot1dData(data_matrix, data_Y, data_Y_labels, colors):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(16, 8))
        for lab, col in zip(data_Y_labels, colors):
            plt.scatter(data_matrix[data_Y == lab, 0],
                        np.zeros(len(data_matrix[data_Y == lab, 0])),
                        label=lab,
                        c=col)
        plt.xlabel('Componente Principal 1')
        plt.legend(loc='lower right')
        plt.tight_layout()
        plt.show()

'''
Plots 2D matrix with Y results labels and colors
'''
def plot2dData(data_matrix, data_Y, data_Y_labels, colors):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(16, 8))
        for lab, col in zip(data_Y_labels, colors):
            plt.scatter(data_matrix[data_Y == lab, 0],
                        data_matrix[data_Y == lab, 1],
                        label=lab,
                        c=col)
        plt.xlabel('Componente Principal 1')
        plt.ylabel('Componente Principal 2')
        plt.legend(loc='lower right')
        plt.tight_layout()
        plt.show()

'''
Plots 3D matrix with Y results labels and colors
'''
def plot3dData(data_matrix, data_Y, data_Y_labels, colors):
    with plt.style.context('seaborn-whitegrid'):
        fig = plt.figure(figsize=(6, 4))
        ax = Axes3D(fig)
        for lab, col in zip(data_Y_labels, colors):
            ax.scatter(data_matrix[data_Y == lab, 0],
                       data_matrix[data_Y == lab, 1],
                       data_matrix[data_Y == lab, 2],
                       label=lab)
        ax.set_xlabel('Componente Principal 1')
        ax.set_ylabel('Componente Principal 2')
        ax.set_zlabel('Componente Principal 3')
        plt.show()

def plot3dDataExpress():
    election = px.data.election()
    fig = px.scatter_3d(election, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total",
                        hover_name="district",
                        symbol="result", color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})
    fig.show()
    print("yes")

'''
Plots 4D matrix with Y results labels and colors
'''
def plot4dData(data_matrix, data_Y, data_Y_labels, colors):
    with plt.style.context('seaborn-whitegrid'):
        fig = plt.figure(figsize=(6, 4))
        ax = Axes3D(fig)
        for lab, col in zip(data_Y_labels, colors):
            z = ax.scatter(data_matrix[data_Y == lab, 0],
                       data_matrix[data_Y == lab, 1],
                       data_matrix[data_Y == lab, 2],
                       c=data_matrix[data_Y == lab, 3],
                       cmap = plt.hot(),
                       label=lab)
        ax.set_xlabel('Componente Principal 1')
        ax.set_ylabel('Componente Principal 2')
        ax.set_zlabel('Componente Principal 3')
        fig.colorbar(z)
        plt.show()