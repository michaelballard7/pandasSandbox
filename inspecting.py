import pandas as pd
import numpy as np 

# loading a csv 
df = pd.read_csv('intel.csv')

# print(df.head())

# print DF to ensure it loaded
# print(df)

# checking the columns of df
# print(df.columns)

# check the shape of the dataFrame
# print(df.shape)

# check the head of the dataFrame
# print(df.head())

# check the end of the dataFrame
# print(df.tail())

# check all available meta info
# print(df.info())

# extract a specific column and create a pandas series
# open = df['Open']
# print(open.head())

# extract multiple specific columns
# open_close = df[['Open', 'Close']]
# print(open_close)

# Describe the general dataFrame for count, mean, std, 25%, 50%, 75%
# print(df.describe())

# practice conditional filtering by creating a boolean and pass to my dataframe
intel_open = df['Open'] > 40
# print(df[intel_open])

# or 
# print(df[df['Open']>40])

# pandas is built on top of numpy, a df is a collection of series
# print(type(intel_open))
# a series is 1D numpy array
# new_open = intel_open.values
# print(type(new_open))

## create a dataframe from Numpy
# new_array = np.arange(0,10).reshape(2,5)
# print(new_array)

# df = pd.DataFrame(data=new_array, columns=["A","B","C","D","E"])
# print(df)


## How to create a DF from a dictionary
# course_sale = {'course':['Python', 'Ruby','Java','C++'],
#     'day': ['Mon',"Tue", 'Wed','Thur'],
#     'price':[5,10,20,30],
#     'sales':[2,3,4,5]
# }

# df_sales = pd.DataFrame(course_sale)
# # print(df_sales)


# # When I have arrays of different sizes they can not be operated upon
# # if i want to add a value to a dataFrame it is broadcasted
# df_sales['new sales'] = 2

# # I can update labels in a pandas dataFrame by passing in column labels
# column_labels = ['Course','Day', 'Price','Old Sale', '24Hr Sale Price']

# df_sales.columns = column_labels
# print(df_sales)

# I can build data frames by broadcasting:
# column_names = ["App",'Rating','Reviews','Size', 'Number of Install','Type', 'Price', 'Lasted Updated']
# google_sales = pd.read_csv('Google Play Data.csv',names=column_names, na_values=-1)
# print(google_sales.head())


