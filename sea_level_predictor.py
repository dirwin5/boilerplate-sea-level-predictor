import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], label='Sea Level')

    # Create first line of best fit
    line1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x1 = list(range(df['Year'].iloc[0], 2051))
    y1 = []
    for year in x1:
        y = line1.intercept + line1.slope * year
        y1.append(y)
    ax.plot(x1, y1, color='red', label='Best fit')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    line2 = linregress(x=df2['Year'], y=df2['CSIRO Adjusted Sea Level'])
    x2 = list(range(df2['Year'].iloc[0], 2051))
    y2 = []
    for year in x2:
        y = line2.intercept + line2.slope * year
        y2.append(y)
    ax.plot(x2, y2, color='green',label='Best fit post 2000')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()