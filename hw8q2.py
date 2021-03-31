import pandas as pd 
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

data = pd.read_excel(r"/home/mattias/Documents/class/hw8/hw8_q1.xlsx",
                     engine='openpyxl')

fig = interaction_plot(data['discharge_time_mins'],data['battery_type'], data['connector_type'], data['battery_temp'],
                       colors=['red','blue'], 
                       markers=['D','^'], 
                       ms=10)
plt.show()