def see_candles(tv_daily_data, title):
    #TradingView Daily Data (our ML inputs)
    #Strig you want to name the chart
    fig = go.Figure(data=go.Ohlc(x=tv_daily_data['time'],
                    open=tv_daily_data['open'],
                    high=tv_daily_data['high'],
                    low=tv_daily_data['low'],
                    close=tv_daily_data['close'])
        )
    fig.update_layout(
        xaxis=dict(fixedrange=False),  
        yaxis=dict(fixedrange=False),
        title = title

        )
    fig.show()
    return()    

# The following function indicates the distance between two positions.
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

# The following function calculates the mean
def calc_mean_from_index(df, moving_average_length):
    reference_list_of_lists = generate_index(df, moving_average_length)
    rolling_price = (df['open'] + df['close'])/2
    df_length_index = range(df.shape[0])
    list_of_means = []
    for generated_means in df_length_index:
        list_of_means.append(np.round((np.mean(rolling_price[reference_list_of_lists[generated_means]])),2))
    return(list_of_means)
    

def neg_values_test(list_of_values):
    for values in flattened_list_index:
        if flattened_list[values] < 0:
            print("Negative Value detected")
            break
    print("Test has Passed")

def sum_to_1():
    a = np.random.rand()
    b = (1 - a) * np.random.rand()
    c = 1 - a - b
    return(a, b, c)
def root_sum_squred(input_list):
    sum_squares = 0
    for i in range(len(input_list)):
        sum_squares = sum_squares + (input_list[i] ** 2)
    return(np.sqrt(sum_squares))

def proportional_polynomials_errors(polyfxn_1, polyfxn_2, polyfxn_3, df):
    a, b, c = sum_to_1()
    range_input = range(len(df['new_index']))
    combination_p_x = a * np.polyval(polyfxn_1, range_input) + b * np.polyval(polyfxn_2, range_input) + c * np.polyval(polyfxn_3, range_input)
    error_results = ti_ppi_df['close'] - combination_p_x
    rss_errors = root_sum_squred(error_results)
    return(a, b, c, rss_errors)

def scale01(selected_column, return_min_max = False):
    '''
    This function scales the numerical inputs into 0 and 1, allowing for better training of the machine learning model
    To transform the ouput of the machine learning input back, we will save the min max of our target and apply the reverse formula
    to get back to our original values. 
    '''
    selected_column_min = min(selected_column)
    selected_column_max = max(selected_column)
    transformed_values = []
    for transformed_value_index in range(len(selected_column)):
        transformed_values.append((selected_column[transformed_value_index] - selected_column_min) / (selected_column_max - selected_column_min))
    if(return_min_max == False):
        return(transformed_values)
    if(return_min_max == True):
        return(selected_column_min, selected_column_max)
    
    
def scale01_t_back(scaled_column, selected_column_min, selected_column_max):
    '''
    The inverse of scale01, we are transforming back what we put in. Mostly, it will be for the value we are predicting to compare against what we put in.
    We also want to transform back form a tensor. Inputs for these are likely to be exclusively tensors. So the first transform gets it back to an array. 
    '''
    reverted_values = []
    scaled_column = scaled_column.detach().numpy()
    for scaled_value_index in range(len(scaled_column)):
        reverted_values.append( (scaled_column[scaled_value_index] * (selected_column_max - selected_column_min) ) + selected_column_min)

    return(pd.DataFrame(reverted_values))
