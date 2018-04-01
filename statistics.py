import plotly.plotly as py
import plotly.graph_objs as go
import plotly



data = open("time.txt", 'r')
x_data =[]
y_data = []
for line in data:
        x_data.append(line.strip().split('\t')[1])
        y_data.append(line.strip().split('\t')[2])
data.close()

trace = go.Scatter(
    x = x_data,
    y = y_data,
    mode = 'markers')

data = [trace]


plot_url = py.plot(data, filename='basic-line')
