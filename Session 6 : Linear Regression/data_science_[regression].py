import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assessing the Dataset

data = 'https://raw.githubusercontent.com/github-goog/colab/main/LinearRegression-Data.csv'
dataset = pd.read_csv(data)

dataset.head()
dataset.tail()
dataset

# Engineering the data

x = dataset[["YearsExperience"]]
y = dataset[["Salary"]]

x
y

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

x_train
x_test
y_train
y_test

# Performing Regression

regressor = LinearRegression()
regressor.fit(x_train,y_train)

# Predicting Test Values

y_pred = regressor.predict(x_test)

y_pred
y_test

# Evaluating model

mse = mean_squared_error(y_pred,y_test)
print("Mean Square Error : ", mse)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Square Error : ", rmse)

r2 = r2_score(y_test, y_pred)
print("R2 Score : ", r2)

# Visualizing model

plt.scatter(x_train, y_train, color='orange', marker="+")
plt.plot(x_train, regressor.predict(x_train), color='green')
plt.title("Salary | Experience (Train)")
plt.xlabel("Experience Years")
plt.ylabel("Salary")
plt.show()

plt.scatter(x_test, y_test, color='#0039BF', marker="*")
plt.plot(x_test, regressor.predict(x_test), color='#FF007F')
plt.title("Salary | Experience (Test)")
plt.xlabel("Experience Years")
plt.ylabel("Salary")
plt.show()

original_values = y_test.to_numpy()
predicted_values = y_pred
list_values = []
for i in range(len(original_values)):
  list_values.append(i)
plt.scatter(list_values, predicted_values, marker="*", color = '#E10600')
plt.scatter(list_values, original_values, color = 'green')

# Custom Prediction

custom_year = 90
custom_pred = regressor.predict([[custom_year]])
print("Salary for", custom_year, "years of experience : ", round(custom_pred[0][0]))

# Thank you!
