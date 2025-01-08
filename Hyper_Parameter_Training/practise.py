import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

dataset = sklearn.datasets.load_breast_cancer()

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target  # 1 for benign, 0 for malignant 


X = df.drop(columns='label', axis=1)
y = df['label']

X = np.asarray(X)
y = np.asarray(y)

#  GridSearchCV is used in determining the best paramters for the model

# loading the model
model = SVC()
# hyperparamters 
parameters = {
    'kernel': ['linear', 'rbf' , 'poly' , 'sigmoid'],
    'C': [0.1, 1, 10, 100]
}

grid_search = GridSearchCV(model, parameters, cv=5 )

grid_search.fit(X, y)

grid_search.cv_results_  # this will give the results with every combination of kernel and C

# to know which is best parameters
best_parameters = grid_search.best_params_

# to know the best accuracy
best_accuracy = grid_search.best_score_











