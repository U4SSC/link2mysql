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
import json

sys.path.append('./')
sys.path.append('./../')

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

def create_country_dict():
    country_data = {}
    for country in country_list:
        unemployment_rate = []
        for year in year_list:
            unemployment_rate.append(float(df_country[df_country["Country Name"] == country][year]))
        country_data[country] = {}
        data_plot = pd.DataFrame({"Year":year_list, "Unemployment Rate":unemployment_rate})
        country_data[country]["plot"] = pd.DataFrame({"Year":year_list, "Unemployment Rate":unemployment_rate})
    return country_data

def create_2d_plot(selected_countries=[]):
    sns.set()
    for country in selected_countries:
        sns.lineplot(data=country_data[country]["plot"],
                    x="Year", y="Unemployment Rate",
                    label=country)

    plt.legend(loc='upper left')

    plt.savefig("./static/img/2d_plot.png")

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

    country_list = df_country["Country Name"]
    year_list = ['2010', '2011', '2012', '2013', '2014']

    try:
        os.mkdir("2d_plot")
    except:
        print("Directory already exists !")


    country_data = create_country_dict()

    # selected_countries = country_list[:5]
    file = open('country_list.json')

    # returns JSON object as
    # a dictionary
    selected_countries = json.load(file)
    selected_countries = list(selected_countries)
    create_2d_plot(selected_countries)


