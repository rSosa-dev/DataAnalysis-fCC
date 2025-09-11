import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
upper = df["value"].quantile(0.025)
lower = df["value"].quantile(0.975)
df = df[df["value"].gt(upper) & df["value"].lt(lower)]


def draw_line_plot():
    # Draw line plot
    figwidth = 16
    figheight = 9
    fig, ax = plt.subplots(figsize=(16, 9))

    # Set the title of the chart and also the labels for both axes
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016 - 12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Display data in the chart
    ax.plot(df["date"], df["value"], color='red')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Convert the Date column into DateTime
    df["date"] = pd.to_datetime(df["date"])

    # Extract year and month
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.strftime('%B') # Complete name of the month

    # Create a list to set the order of the months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(["year", "month"])['value'].mean().unstack()
    df_bar = df_bar[month_order] # Reorder columns by month

    # Draw bar plot
    fig, ax = plt.su
    bplots(figsize=(12, 6))
    df_bar.plot.bar(rot=0, ax=ax) # There is no need of putting X and Y axis because we are telling the df to create the plot with its data

    # Set the titles for each axis
    ax.set_xlabel = ("Years")
    ax.set_ylabel = ("Average Page Views")
    ax.legend(title="Months")

    fig.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

print(draw_bar_plot())