# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:14:33 2020

@author: chowkelvin
"""
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,total_sqft,bath,cond):
    try:
        loc_index = __data_columns.index(location)
    except:
        loc_index = -1
    
    x=np.zeros(len(__data_columns))
    x[0]=total_sqft
    x[1]=bath
    x[2]=cond
    if loc_index>=0:
        x[loc_index]=1
        
    return "{:,.2f}".format(np.round(__model.predict([x])[0][0],2))

def get_location_names():
    
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations
    global __model
    
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    with open("./artifacts/home_prices_model.pickle",'rb') as f:
          __model = pickle.load(f)
    
    print("loading saved artifacts...done")    

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('NAmes',1000,2,5))
