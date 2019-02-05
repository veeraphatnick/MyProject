import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv("C:\\Users\\58050379\\PycharmProjects\\Floc Detection in Water Treatment Process\\1\\dataEdit1.csv")

data = [go.Scatter( x=df['Time'], y=df['  NoF'])]

py.plot(data, filename='Number of Floc')
