# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:20:56 2022

@author: Si Kemal
"""

from tensorflow.keras.layers import Dense,Dropout,BatchNormalization
from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Plot_features():
    def __init__(self):
        pass
    
    # Plot categorical data
    def plot_cat(self,df,categorical_columns):
        '''
        This function is to generate plots for categorical columns
        Parameters
        ----------
        df : ARRAY
        Returns
        -------
        None.
        
        '''
        for cat in categorical_columns:
          plt.figure()
          sns.countplot(df[cat])
          plt.show()
    
    # Plot continuous data
    def plot_con(self,df,continuous_columns):
        '''
        This function is to generate plots for continuous columns
        Parameters
        ----------
        df : ARRAY
        Returns
        -------
        None.
        
        '''
        for con in continuous_columns:
          plt.figure()
          sns.distplot(df[con])
          plt.show()



class ModelCreation():
    def __init__(self):
      pass
    
    def model_layer(self,X_train,num_node=128,drop_rate=0.3,output_node=1):
      model = Sequential()
      model.add(Input(shape=(np.shape(X_train)[1:])))
      model.add(Dense(num_node,activation='relu',name='Hidden_layer1'))
      model.add(BatchNormalization())
      model.add(Dropout(drop_rate))
      model.add(Dense(num_node,activation='relu',name='Hidden_layer2'))
      model.add(BatchNormalization())
      model.add(Dropout(drop_rate))
      model.add(Dense(2,'softmax',name='Output_layer'))
      model.summary()
      return model