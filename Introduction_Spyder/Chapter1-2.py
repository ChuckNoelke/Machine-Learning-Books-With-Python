# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:19:41 2019

@author: marno
"""

# Bring data into workspace and replicate plots
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# matplotlib inline

df_wage = pd.read_csv('data/wage.csv')


df_wage.info()

# gives only string features

df_wage.describe(include=['object'])

# Unique = number of options included

# gives only string features

df_wage.describe(include=['number'])


# Look at all available plotting styles
plt.style.available


# need to reshape data to plot correctly

# create column for feature option in eductation and map wages to it
 
df_edu = df_wage.pivot(columns='education', values='wage')


# Image from ISLR
from IPython.display import Image
Image('images/ch1_pg2.png')

# importing statsmodels library to fit lowess curve through data
import statsmodels.api as sm

fig, ax = plt.subplots(1, 3, figsize=(15,6)) # set frame for 3 diagrams
df_wage.plot.scatter('age', 'wage', ax=ax[0])

lowess = sm.nonparametric.lowess(df_wage['wage'], df_wage['age'], frac=.2)
ax[0].plot(lowess[:, 0], lowess[:, 1], color='red')

df_wage.plot.scatter('year', 'wage', ax=ax[1])
year_median = df_wage.groupby('year')['wage'].median() # weise dem Jahr die Mittelwerte zu

ax[1].plot(year_median,color='yellow')



boxplot = df_edu.plot.box(ax=ax[2], rot=45, patch_artist='true')
colors = ['lightblue', 'green', 'yellow', 'blue', 'red']
for artist, color in zip(boxplot.artists, colors):
    artist.set_facecolor(color)
    
import seaborn as sns

# Similar plots to those above
sns.lmplot('age', 'wage', data=df_wage, hue='education')
sns.lmplot('year', 'wage', data=df_wage, ci=99.99, hue='education')


sns.boxplot('education', 'wage', data=df_wage)


df1 = df_wage[['age', 'year', 'education', 'wage']]


df_melt = pd.melt(df1, id_vars=['education', 'wage'])

df_melt.head()

seaborn_grid = sns.lmplot('value', 'wage', col='variable', hue='education', data=df_melt, sharex=False)
seaborn_grid.fig.set_figwidth(8)

left, bottom, width, height = seaborn_grid.fig.axes[0]._position.bounds
left2, bottom2, width2, height2 = seaborn_grid.fig.axes[1]._position.bounds
left_diff = left2 - left
seaborn_grid.fig.add_axes((left2 + left_diff, bottom, width, height))

sns.boxplot('education', 'wage', data=df_wage, ax = seaborn_grid.fig.axes[2])
ax2 = seaborn_grid.fig.axes[2]
ax2.set_yticklabels([])
ax2.set_xticklabels(ax2.get_xmajorticklabels(), rotation=30)
ax2.set_ylabel('')
ax2.set_xlabel('');

leg = seaborn_grid.fig.legends[0]
leg.set_bbox_to_anchor([0, .1, 1.5,1])

