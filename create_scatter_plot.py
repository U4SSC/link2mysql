import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import warnings
import os
import sys
sys.path.append(os.path.dirname("../../link2mysql/"))
sys.path.append('../../')
import link2mysql
from link2mysql import dbconnect,config
warnings.filterwarnings('ignore')


non_country_list = ['Arab World', 'Central Europe and the Baltics', 'Caribbean small states', 'East Asia & Pacific (excluding high income)',
                    'Early-demographic dividend', 'East Asia & Pacific', 'Europe & Central Asia (excluding high income)',
                    'Europe & Central Asia', 'Euro area', 'European Union', 'Fragile and conflict affected situations', 'High income',
                    'Heavily indebted poor countries (HIPC)', 'IBRD only', 'IDA & IBRD total', 'IDA total', 'IDA blend', 'IDA only',
                    'Latin America & Caribbean (excluding high income)', 'Latin America & Caribbean', 'Least developed countries: UN classification',
                    'Low income', 'Lower middle income', 'Low & middle income', 'Late-demographic dividend', 'Middle East & North Africa',
                    'Middle income', 'Middle East & North Africa (excluding high income)', 'North America', 'OECD members', 'Other small states',
                    'Pre-demographic dividend', 'Post-demographic dividend', 'South Asia', 'Sub-Saharan Africa (excluding high income)',
                    'Sub-Saharan Africa', 'Small states', 'East Asia & Pacific (IDA & IBRD countries)',
                    'Europe & Central Asia (IDA & IBRD countries)', 'Latin America & the Caribbean (IDA & IBRD countries)',
                    'Middle East & North Africa (IDA & IBRD countries)', 'South Asia (IDA & IBRD)',
                    'Sub-Saharan Africa (IDA & IBRD countries)', 'Upper middle income', 'World']


def create_scatter_plot(year='2010'):
    trace = go.Scatter(
        y=df_country[year],
        mode='markers',
        name='Unemployment (%)',
        marker=dict(size=df_country[year].values,
                    line=dict(width=1),
                    color=df_country[year].values,
                    opacity=0.7,
                    colorscale='Portland',
                    showscale=True),
        text=df_country['Country Name'].values)  # The hover text goes here...
    layout = go.Layout(
        title=f'Scatter plot of unemployment rates in {year}',
        hovermode='closest',
        xaxis=dict(
            ticklen=5,
            zeroline=False,
            gridwidth=2,
        ),
        yaxis=dict(
            title='Unemployment Rate (%)',
            ticklen=5,
            gridwidth=2,
        ),
        showlegend=False,
    )
    fig = go.Figure(data=[trace], layout=layout)
    py.plot(fig, filename=f'./static/plot/scatter_plot_{year}', auto_open=False)

if __name__ == "__main__":
    # read data
    # from db
    df = dbconnect.select_all("kpi_1")
    # from csv path
    # df = pd.read_csv('../data/API_ILO_country_YU.csv')

    # filter the data by noncountry list
    df_non_country = df[df['Country Name'].isin(non_country_list)]
    index = df_non_country.index
    df_country = df.drop(index)

    # create directory to place the scatter plots
    # try:
    #     os.mkdir("scatter_plots")
    # except:
    #     print("Directory already exists !")


    year_list = ['2010', '2011', '2012', '2013', '2014']

    for year in year_list:
        create_scatter_plot(year)
