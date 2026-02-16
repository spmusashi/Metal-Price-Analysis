import unittest
import pandas as pd
import csv
import plotly
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

def check_for_negatives_in_list(self, list_of_numbers ):
    neg_val_count = 0
    flattened_list_index_length = len(list_of_numbers)
    flattened_list_index = range(flattened_list_index_length)
    for number_instance in flattened_list_index:
        if list_of_numbers[number_instance] < 0:
            neg_val_count = neg_val_count + 1
    return(neg_val_count)

    
        
negative_values_test_input = generate_index(oil_df, 5)
flattened_list = [item for sublist in negative_values_test_input for item in sublist]
flattened_list_index = range(len(flattened_list))


class reasonable_values (unittest.TestCase):
    def test_count_neg_fxn(self):
        example_list = list([-5,6, 7, 8])
        self.test_count_neg_fxn_input = check_for_negatives_in_list(self, example_list)
        self.assertEqual(self.test_count_neg_fxn_input, 1) #there is one negative value in the list        

    
    def test_neg_val(self):
        self.assertEqual(check_for_negatives_in_list(self, flattened_list) , 0 )
    def test_index_is_integer(self):
        self.assertTrue(all(isinstance(item, int) for item in flattened_list))



class reasonable_values (unittest.TestCase):
    def test_count_neg_fxn(self):
        example_list = list([-5, 6, 7, 8])
        self.test_count_neg_fxn_input = calc_mean_from_index(self, example_list)
        self.assertEqual(self.test_count_neg_fxn_input, 1) #there is one negative value in the list

    def test_neg_val(self):
        self.assertEqual(check_for_negatives_in_list(self, flattened_list) , 0)
    def test_index_is_integer(self):
        self.assertTrue(all(isinstance(item, int) for item in flattened_list))

