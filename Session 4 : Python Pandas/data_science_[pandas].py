import pandas as pd

# Create Dataframes

temp1 = ['This' , 'is' , 'a' , 'simple' , 'list' , 'for' , 'array']

temp2 = {'University' : ['Harvard', 'Princeton', 'Yale', 'Columbia', 'Cornell'], 'Rank' : [1, 2, 3, 4, 5]}

temp3 = 'https://raw.githubusercontent.com/gohil-jay/Widhya-ML-Internship/main/Week-3/clean_data.csv'

frame1 = pd.DataFrame(temp1)

#frame2 = pd.DataFrame(temp2, dtype=float)
#frame2 = pd.DataFrame(temp2, index=['rank1','rank2','rank3','rank4','rank5'])
frame2 = pd.DataFrame(temp2)

frame3 = pd.read_csv(temp3)

frame1

# print(frame2)

frame2

frame3

# Manipulate DataFrames

# Manipulate Columns
frame4 = frame3[['Followers']]

#print(frame4)
frame4

# Manipulate Rows
frame5 = pd.read_csv(temp3, index_col ="USERNAME")

row_select_1 = frame5.loc["drgorillapaints"]
print(row_select_1)

print("\n"*2)

row_select_2 = frame5.iloc[3]
print(row_select_2)

print("\n"*2)

row_select_3 = frame5.iloc[3:10]
print(row_select_3)

# Manipulate column values
frame6 = pd.read_csv(temp3)
frame6['NEW1'] = frame6['Likes'] + frame6['time']
frame6['NEW2'] = frame6['Likes'] + 100
frame6['NEW3'] = frame6['Likes'] * 28
frame6

# Undertsand Null Values
temp4 = frame3.isnull()
temp4

# Fill Null Values
value = 99999999
temp5 = frame3.fillna(value)
temp5

# Delete Null Values
temp6 = frame3.dropna()
temp6

# Delete particular row
temp7 = frame3.drop(2)
temp7

# Add two dataframes

frame7 = frame3.append(frame3)
# frame7 = frame3[['time', 'Likes']].append(frame3[['time', 'Likes']])
frame7

# Iterate through Dataframe

# Direct Access
temp8 = frame3['Followers'][5]
temp8

# Access entire column
temp10 = frame3[['USERNAME']]
temp10

# Access entire row(s)
temp9 = frame3.iloc[2:10]
temp9

# Analyse Dataframe

# See the top dataframe values
top = frame3.head()
top

# See the bottom dataframe values

bottom = frame3.tail()
bottom

perc_list =[.10, .20, .30, .40, .50, .60, .70, .80, .90]
types = ['object', 'float', 'int']

# desc = frame7.describe()
desc_1 = frame7.describe(percentiles = perc_list, include = types)
desc_1

# Visualize DataFrame

# Histogram
x = frame7['time'].hist()
x

# Area Plots
y = frame3.plot.area()
y

# Bar Plots
#y_1 = frame3.plot.bar()
# y_2 = frame3['time'].plot.bar()
# y_3 = frame3.iloc[2:10].plot.bar()
y_4 = frame3.iloc[2:10].plot.bar(stacked = True)
y_4

# Line Graphs

# z_1 = frame3.plot.line()
# z_2 = frame3['Likes'].plot.line()
z_3 = frame3.iloc[2:11].plot.line()
z_3

# Scatter Plots

# w_1 = frame3.plot.scatter(x = 'Likes', y = 'time')
w_2 = frame3.plot.scatter(x = 'Likes', y = 'time', c ='Red')
w_2

# Thank you!
