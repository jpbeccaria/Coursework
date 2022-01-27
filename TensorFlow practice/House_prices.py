# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:54:28 2022

@author: Juan
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.wrappers.scikit_learn import KerasRegressor

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

import os

# Importing datasets

os.chdir('.\Desktop\GitHub\Data')

dataset_train = pd.read_csv('train.csv')
dataset_test = pd.read_csv('test.csv')

dataset_train_Y = dataset_train.pop('SalePrice')
dataset_train_X = dataset_train

# Some columns have NaNs but it doesn't mean no-information but ausent of this feature.
# So taht, we are goint to replace NaN for a string
# This colums are:  Alley, FireplaceQu, PoolQu, Fence, MiscFeature

dataset_train_X['Alley'] = dataset_train_X['Alley'].replace(np.nan, 'no hay')
dataset_train_X['FireplaceQu'] = dataset_train_X['FireplaceQu'].replace(np.nan, 'no hay')
dataset_train_X['PoolQC'] = dataset_train_X['PoolQC'].replace(np.nan, 'no hay')
dataset_train_X['Fence'] = dataset_train_X['Fence'].replace(np.nan, 'no hay')
dataset_train_X['MiscFeature'] = dataset_train_X['MiscFeature'].replace(np.nan, 'no hay')

dataset_test['Alley'] = dataset_test['Alley'].replace(np.nan, 'no hay')
dataset_test['FireplaceQu'] = dataset_test['FireplaceQu'].replace(np.nan, 'no hay')
dataset_test['PoolQC'] = dataset_test['PoolQC'].replace(np.nan, 'no hay')
dataset_test['Fence'] = dataset_test['Fence'].replace(np.nan, 'no hay')
dataset_test['MiscFeature'] = dataset_test['MiscFeature'].replace(np.nan, 'no hay')

#Remuving the first 'Id' column
dataset_train_X.drop('Id', inplace=True, axis=1)
dataset_test_X = dataset_test.drop('Id', axis=1)


# Prepearing our cleaning pipeline, selectin the numerical, ordinal and nominal variables
numerical = dataset_train_X.select_dtypes(include=np.number).columns.tolist()

ordinal = ['LandSlope', 'GarageCond', 'HeatingQC', 'BsmtCond', 'ExterCond', 'GarageQual',
           'KitchenQual', 'BsmtQual', 'ExterQual']
nominal = dataset_train_X.select_dtypes(exclude=np.number).columns.difference(ordinal).tolist()


numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('encoder', StandardScaler()
     )])

nominal_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(sparse=True, handle_unknown='ignore'))
    ])

ordinal_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('encoder', OrdinalEncoder())
    ])

# Preprocessing pileline is the sum of the three previous ones.
preprocessing_pipeline = ColumnTransformer([
    ('ordinal_preprocessor', ordinal_pipeline, ordinal),
    ('nordinal_preprocessor', nominal_pipeline, nominal),
    ('numericao_preprocessor', numerical_pipeline, numerical)
    ])


#%%  Bilding the model

def create_model():
    model = keras.Sequential([
    layers.Dense(289, activation='relu'),
    layers.Dense(400, activation='relu'),
    layers.Dense(200, activation='relu'),
    layers.Dense(50, activation='relu'), 
    layers.Dense(1, activation='linear')
    ])

    model.compile(
    optimizer=tf.optimizers.Adam(learning_rate=0.1),   
    loss='mae',
    metrics=['mae', 'mse'])

    return model

# wrap the model using the function we created to be able to put it into a sklear pipeline
reg = KerasRegressor(build_fn=create_model, epochs=100, verbose = True)


#%%  Final pipeline

final_pipeline = Pipeline([
    ('preprocessor', preprocessing_pipeline),
    ('estimator', reg)])

#%% Training our model and making predictions

final_pipeline.fit(dataset_train_X, dataset_train_Y)

predictions = final_pipeline.predict(dataset_test_X)

#%% Exporting our predictions

submiting_data = pd.DataFrame()
submiting_data['Id'] = dataset_test['Id']
submiting_data['SalePrice'] = predictions
submiting_data.to_csv('submiting_data.csv', index=False)



