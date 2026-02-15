import unittest
import pandas as pd
import csv
import plotly
#import plotly.graph_obcalled_listects as go
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import unittest

cu_df = pd.read_csv("Relevant Data/copper.csv")
#copper
au_df = pd.read_csv("Relevant Data/gold.csv")
#gold
ag_df = pd.read_csv("Relevant Data/silver.csv")
#silver
oil_df = pd.read_csv("Relevant Data/oil.csv")
ti_ppi_df = pd.read_csv("Relevant Data/Ti_PPI.csv")
#Titanium PPI (A monthly metric)

def generate_index(df, moving_average_length):
    ma_index = range(moving_average_length)
    ma_index_list = []
    df_length_index = range(df.shape[0])
    for outer_index in df_length_index:  
        values_from_index = []
        for called_list in ma_index:
            #values_from_index.append([range(outer_index,abs(called_list - outer_index))])
            values_from_index.append(abs(called_list - outer_index))
        ma_index_list.append(values_from_index)
    return(ma_index_list)

#sample_lol = generate_index(oil_df, 5)

def calc_mean_from_index(df, moving_average_length):
    reference_list_of_lists = generate_index(df, moving_average_length)
    rolling_price = (df['open'] + df['close'])/2
    df_length_index = range(df.shape[0])
    list_of_means = []
    for generated_means in df_length_index:
        list_of_means.append(np.round((np.mean(rolling_price[reference_list_of_lists[generated_means]])),2))
    return(list_of_means)
        



negative_values_test_input = generate_index(oil_df, 5)
flattened_list = [item for sublist in negative_values_test_input for item in sublist]
flattened_list_index = range(len(flattened_list))


def neg_values_test(list_of_values):
    for values in flattened_list_index:
        if flattened_list[values] < 0:
            raise ValueError("Index value cannot be negative")

class neg_values (unittest.TestCase):
    def neg_values_test(self):
        with self.assertRaises(ValueError):
            neg_values_test(flattened_list)
            
            
