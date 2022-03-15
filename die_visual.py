import imp
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

dies = [Die(), Die(), Die()]
results = []
for roll_num in range(1000):
    result = sum([die.roll() for die in dies])
    results.append(result)

frequencies = []
x_values = list(range(len(dies), len(dies) * dies[0].num_sides + 1))
for value in x_values:
    frequency = results.count(value)
    frequencies.append(frequency)

data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling three D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
