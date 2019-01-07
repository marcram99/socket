# encoding: utf-8

import pygal

line_chart = pygal.Line()
line_chart.title = 'Température(en degré Celsius)'
line_chart.add('Cave', [0, 1, 2, -1, -3, 5, 2, 8,-2, 4, 5])  # Add some values
line_chart.add('outdoor', [2, 0, 1, 2, -1, -3, 5, 2, 8,-2, 4])  # Add some values
line_chart.render_to_file('temp_chart.svg')                          # Save the svg to a file