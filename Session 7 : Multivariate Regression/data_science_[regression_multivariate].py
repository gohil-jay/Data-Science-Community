import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assessing the Dataset

data = 'https://raw.githubusercontent.com/github-goog/colab/main/multivariate_regression_dataset.csv'
dataset = pd.read_csv(data)
dataset.head()
dataset.tail()
print(dataset)

# Identifying necessary variables

# Understanding correlation among columns
print("Visualizing correlation between features using heatmap -->", "\n"*2)
temp_plot = sns.heatmap(dataset.corr(method='pearson'), cmap='Blues')
print(temp_plot)

# Engineering the data

x = dataset[["R&D Spend", "Administration", "Marketing Spend"]]
y = dataset[["Profit"]]

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

print(x_train)
print(x_test)

print(y_train)
print(y_test)

# Performing Regression

regressor = LinearRegression()
regressor.fit(x_train,y_train)

# Predicting Test Values

y_pred = regressor.predict(x_test)
print(y_pred)
print(y_test)

# Evaluating model

mse = mean_squared_error(y_pred,y_test)
print("Mean Square Error : ", mse)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Square Error : ", rmse)

r2 = r2_score(y_test, y_pred)
print("R2 Score : ", r2)

# Visualizing model

var_1 = []
var_2 = []
var_3 = []
var_4 = []

for i in range(len(x)):
  var_1.append(x["R&D Spend"][i]/1000)

for j in range(len(x)):
  var_2.append(x["Administration"][j]/1000)

for k in range(len(x)):
  var_3.append(x["Marketing Spend"][k]/1000)

for l in range(len(y)):
  var_4.append(y["Profit"][l]/1000)

print("Multi-Dimensioanl Visualization of original data -->", "\n"*2)

fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection ='3d')
ax.scatter(var_1, var_2, var_3, s = var_4, c="green")
ax.set_xlabel('\n R&D Spend (in 1K)')
ax.set_ylabel('\n Administration (in 1K)')
ax.set_zlabel('\n Marketing Spend (in 1K)')
print(ax)

var_11 = []
var_12 = []
var_13 = []
var_14 = []

for i in x_train["R&D Spend"]:
  var_11.append(i/1000)

for j in x_train["Administration"]:
  var_12.append(j/1000)

for k in x_train["Marketing Spend"]:
  var_13.append(k/1000)

for l in y_train["Profit"]:
  var_14.append(l/1000)

print("Multi-Dimensioanl Visualization of train data -->", "\n"*2)

fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection ='3d')
ax.scatter(var_11, var_12, var_13, s = var_14, c="blue")
ax.set_xlabel('\n R&D Spend (in 1K)')
ax.set_ylabel('\n Administration (in 1K)')
ax.set_zlabel('\n Marketing Spend (in 1K)')
print(ax)

var_21 = []
var_22 = []
var_23 = []
var_24 = []

for i in x_test["R&D Spend"]:
  var_21.append(i/1000)

for j in x_test["Administration"]:
  var_22.append(j/1000)

for k in x_test["Marketing Spend"]:
  var_23.append(k/1000)

for l in y_test["Profit"]:
  var_24.append(l/1000)

print("Multi-Dimensioanl Visualization of original test data -->", "\n"*2)

fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection ='3d')
ax.scatter(var_21, var_22, var_23, s = var_24, c="orange")
ax.set_xlabel('\n R&D Spend (in 1K)')
ax.set_ylabel('\n Administration (in 1K)')
ax.set_zlabel('\n Marketing Spend (in 1K)')
print(ax)

var_31 = []
var_32 = []
var_33 = []
var_34 = []

for i in x_test["R&D Spend"]:
  var_31.append(i/1000)

for j in x_test["Administration"]:
  var_32.append(j/1000)

for k in x_test["Marketing Spend"]:
  var_33.append(k/1000)

for l in range(len(y_pred)):
  var_34.append(int(y_pred[l])/1000)

print("Multi-Dimensioanl Visualization of predicted values -->", "\n"*2)

fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection ='3d')
ax.scatter(var_31, var_32, var_33, s = var_34, c="red")
ax.set_xlabel('\n R&D Spend (in 1K)')
ax.set_ylabel('\n Administration (in 1K)')
ax.set_zlabel('\n Marketing Spend (in 1K)')
print(ax)

original_values = y_test.to_numpy()
predicted_values = y_pred

list_values = []
for i in range(len(original_values)):
  list_values.append(i)

plt.scatter(list_values, predicted_values, marker="+", color = 'orange')
plt.scatter(list_values, original_values, color = 'blue')

# Custom Prediction
custom_R_D = 10000
custom_Administration = 65000
custom_Marketing = 4000
custom_pred = regressor.predict([[custom_R_D, custom_Administration, custom_Marketing]])
print("Profit for custom aforementioned values : ", round(custom_pred[0][0]))

# Thank you!
