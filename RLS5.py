import pandas
from pandas.tools import plotting
data = pandas.read_csv("data/RLS5_csv.csv", sep=",")

# Scatter
plotting.scatter_matrix(data[["Tmax", "Tmin"]])
