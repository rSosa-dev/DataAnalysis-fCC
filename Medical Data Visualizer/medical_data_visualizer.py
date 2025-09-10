import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv("medical_examination.csv")

# Add "overweight" columns
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. 
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns={0:'total'})

    # Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    # Get the figure for the output and store it in the fig variable.
    fig = sns.catplot(data = df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    fig.savefig('catplot.png')
    return fig

# Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:

    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & # diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
                (df['height'] >= df['height'].quantile(0.025)) & # height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
                (df['height'] <= df['height'].quantile(0.975)) & # height is more than the 97.5th percentile
                (df['weight'] >= df['weight'].quantile(0.025)) & # weight is less than the 2.5th percentile
                (df['weight'] <= df['weight'].quantile(0.975))] # weight is more than the 97.5th percentile

    # Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()

    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(16, 9))

    # Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")

    fig.savefig('heatmap.png')
    return fig