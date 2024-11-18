import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
# import matplotlib.pyplot as plt

df = pd.read_csv("air traffic.csv")  # creation of the dataframe
data = df["Pax"].str.replace(",", "").values.astype('int')  # take only one column and take off commas from each value

values = []  # Initialize array of values to be evaluated
prediction = []
window = 36  # number of values to be evaluated

for i in range(window, data.shape[0]):
    values.append(data[i - window:i])
    prediction.append(data[i])

x = np.array(values)  # converting lists in numpy array
y = np.array(prediction)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0, shuffle=False)

print("-----Random Forest method-----")
clf = RandomForestRegressor(random_state=17)
clf.fit(x_train, y_train)
y_predicted1 = clf.predict(x_test)
print(mean_absolute_error(y_test, y_predicted1))

print("-----Linear Regression method-----")
clf = LinearRegression()
clf.fit(x_train, y_train)
y_predicted2 = clf.predict(x_test)
print(mean_absolute_error(y_test, y_predicted2))

print("-----KNN Regression method-----")
clf = KNeighborsRegressor(n_neighbors=15)
clf.fit(x_train, y_train)
y_predicted3 = clf.predict(x_test)
print(mean_absolute_error(y_test, y_predicted3))
