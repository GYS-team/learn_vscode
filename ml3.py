import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, model_selection, metrics, neighbors, linear_model, neural_network


def compare_models(X, y, dataname, model_modelnames):
    '''Comparing the performance of given ML models, on given data.
# Example:
X, y = datasets.make_circles(noise=0.3, factor=0.5); dataname = 'circles'
model_modelnames = [
        [linear_model.LogisticRegression(),  'Logistic Reg'],
        [neighbors.KNeighborsClassifier(3), 'knn (n=3)'],
        [neighbors.KNeighborsClassifier(5), 'knn (n=5)'],
        [neighbors.KNeighborsClassifier(10), 'knn (n=10)'],
        [neural_network.MLPClassifier((100,)), 'ANN (100,)'],
    ]
compare_models(X, y, dataname, model_modelnames)
 '''
    ix = 0
    fig, ax = plt.subplots(figsize=(14, 5))
    modelnames = []
    for model, modelname in model_modelnames:
        ax.scatter(np.linspace(ix-0.1, ix+0.1, 5),
                   model_selection.cross_val_score(model, X, y, cv=5))
        modelnames.append(modelname)
        ix += 1
    ax.set_xticks(range(len(model_modelnames)))
    ax.set_xticklabels(modelnames)
    ax.grid()
    ax.set_title(dataname, fontsize=18)
    ax.set_ylabel('Accuracy', fontsize=16)
