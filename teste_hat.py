import statsmodels.api as sm
from xlsxreader import ExcelDataReader
import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt


data = ExcelDataReader('data/hat.xlsx', usecols=(0, 1), l1=1)
data = np.array(data.dados())

x = data[:, np.newaxis, 0]
y = data[:, np.newaxis, 1]


rgr = linear_model.LinearRegression()

rgr.fit(x, y)
print(x)
plt.scatter(x, y, color='black')
plt.plot(x, rgr.predict(x), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

