#Team data is displayed 
import pandas as pd 
import nfl_data_py as nfl 
import matplotlib.pyplot as plt 
from matplotlib import style 

#Display columns 
pd.set_option('display.max.columns', None) 

#Data from teams as of the 2022 season 
year = 2022 

df = nfl.import_ngs_data(stat_type='passing')

df 

df = df[df['week'] == 0] 
df = df[df['season'] == year] 
df = df.reset_index() 
        
average_ttt = df['avg_time_to_throw'].mean() 
average_cpae = df['completion_percentage_above_expectation'].mean() 

plt.rcParams["figure.figsize"] = [20, 14]
plt.rcParams["figure.autolayout"] = True 

x = []
y = []

for qb in df.index:
    x.append(df['avg_time_to_throw'][qb] - average_ttt)
    x.append(df['completion_percentage_above_expectation'][qb] - average_cpae) 
    
xy = pd.DataFrame({'x' : x, 'y' : y})

fig, ax =plt.subplots()

ax.scatter(xy['x], xy['y'], s=500, c='blue') 
              
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
          
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
              
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
              
plt.xlim((-0.4,0.4))
plt.ylim((-20,20))
              
              
for nameyear in xy.index:
              plt.annotate(f"{df['player_display_name'][nameyear]}, {df['season'][nameyear]}",\
                           (xy['x'][nameyear] + 0.005,
                            xy['y'][nameyear] - 0.025),
                            fontsize=12) 
              
plt.annotate('Lots of time to throw, \nreceivers making great catches', (0.2,17.5), fontsize=18)
plt.annotate('Limited time to throw, \nreceviers making great catches', (-0.3,17.5), fontsize=18)
plt.annotate('Limited time to throw, \nreceviers not making great catches', (-0.3,17.5), fontsize=18)
plt.annotate('Lots of time to throw, \nreceivers not making great catches', (0.21,17.5), fontsize=18)
              
plt.title(f'QB Average Time to Throw (s) vs. Completion % Above/Below Expectation\n Both Centered
          fontdict={'fontsize':30}) 
              
plt.show() 
