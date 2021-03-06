#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:18:33 2018

@author: jcdazeredo
"""

from simple_tree import Tree
from scipy import stats
import bootstrap as bs
import numpy as np

class Random_Forest(object):
    def __init__(self, y_column, dataset, attribute_list, num_trees):
        self.num_trees = num_trees
        self.y_column = y_column
        self.dataset = dataset.copy()
        self.attribute_list = attribute_list
        self.bootstrap_list = None
        self.tree_list = [None]*num_trees
        self.accuracy = None
        
    def fit(self):
        self.create_bootstrap()

        for i in range(self.num_trees):
            self.tree_list[i] = Tree(self.y_column, self.bootstrap_list[i].training_set, self.attribute_list, True)
            self.tree_list[i].fit()
#            self.tree_list[i].printree()
            
        self.validation()
        
        
    def create_bootstrap(self):
        self.bootstrap_list = bs.create_bootstrap_list(self.dataset, self.num_trees, 0.6)
  
    def validation(self):
        accuracy = 0
        # Faz a predição de todas as árvores para o mesmo dataset
        for i in range(self.num_trees):
            y_pred = self.tree_list[i].classify(self.bootstrap_list[i].test_set)
            y_actual = (self.bootstrap_list[i].test_set).iloc[:, self.y_column]
            y_pred = np.reshape(y_pred, (y_actual.shape))
            
            accuracy += np.sum(y_pred == y_actual) / y_actual.shape[0]
            
            self.accuracy = accuracy/self.num_trees
            
    def classify(self, dataset):
        predictions = [None]*self.num_trees
        
        # Faz a predição de todas as árvores para o mesmo dataset
        for i in range(self.num_trees):
            predictions[i] = self.tree_list[i].classify(dataset)
            
        predictions = np.array(predictions)
        
        # Verifica qual teve mais votação
        mode = stats.mode(predictions)
        y_pred = mode[0].transpose()   
        return y_pred, mode
