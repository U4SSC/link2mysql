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

country_list = ['Afghanistan', 'Angola', 'Albania', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Chile', 'China', 'Cameroon', 'Congo', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Guinea', 'Greece', 'Guatemala', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'India', 'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Cambodia', 'Korea, Rep.', 'Kuwait', 'Lebanon', 'Liberia', 'Libya', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Morocco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'North America', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'New Zealand   ', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Papua New Guinea', 'Poland', 'Puerto Rico', 'Portugal', 'Paraguay', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'Somalia', 'Serbia', 'Slovenia', 'Sweden', 'Swaziland', 'Syrian Arab Republic', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'Venezuela, RB', 'Vietnam', 'Yemen, Rep.', 'South Africa', 'Congo, Dem. Rep.', 'Zambia', 'Zimbabwe'
                ]
# for plot setting
metricscale = [[0, 'rgb(102,194,165)'], [0.05, 'rgb(102,194,165)'],
               [0.15, 'rgb(171,221,164)'], [0.2, 'rgb(230,245,152)'],
               [0.25, 'rgb(255,255,191)'], [0.35, 'rgb(254,224,139)'],
               [0.45, 'rgb(253,174,97)'], [0.55, 'rgb(213,62,79)'], [1.0, 'rgb(158,1,66)']]


def create_circle_world_plot(year='2010'):
    data = [ dict(
            type = 'choropleth',
            autocolorscale = False,
            colorscale = metricscale,
            showscale = True,
            locations = country_clean['Country Name'].values,
            z = country_clean[year].values,
            locationmode = 'country names',
            text = country_clean['Country Name'].values,
            marker = dict(
                line = dict(color = 'rgb(250,250,225)', width = 0.5)),
                colorbar = dict(autotick = True, tickprefix = '',
                title = 'Unemployment\nRate')
                )
            ]

    layout = dict(
        title= f'World Map of Global Youth Unemployment in the Year {year}',
        geo=dict(
            showframe=True,
            showocean=True,
            oceancolor='rgb(28,107,160)',
            projection=dict(
                type='orthographic',
                rotation=dict(
                    lon=60,
                    lat=10),
            ),
            lonaxis=dict(
                showgrid=False,
                gridcolor='rgb(202, 202, 202)',
                width='0.05'
            ),
            lataxis=dict(
                showgrid=False,
                gridcolor='rgb(102, 102, 102)'
            )
        ),
    )
    fig = dict(data=data, layout=layout)
    py.plot(fig,validate=False, filename=f'./static/plot/circle_world_plot_{year}', auto_open=False)


if __name__ == "__main__":
    # read data
    # from db
    country = dbconnect.select_all("kpi_1")
    # from csv path
    # country = pd.read_csv('../data/API_ILO_country_YU.csv')

    # filter the data by noncountry list
    country_clean = country[country['Country Name'].isin(country_list)]

    # create directory to place the scatter plots
    try:
        os.mkdir("circle_world_plots")
    except:
        print("Directory already exists !")

    year_list = ['2010', '2011', '2012', '2013', '2014']

    for year in year_list:
        create_circle_world_plot(year)
