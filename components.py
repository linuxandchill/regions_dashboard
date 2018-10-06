import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from DataManager import DataManager

dm = DataManager()

def pull_regions():
    sectors_by_region_statewide = dm.get_sectors_by_region_statewide()
    return sectors_by_region_statewide

def generate_bar_chart(dataframe): 
    data = dcc.Graph(

            )

def generate_pie(df, column):
    layout = go.Layout(
            )

    labels = []
    values = []

    trace = go.Pie(
            labels = labels, # [sm business, retail, agriculture]
            values = values # [45, 25, 40]
            )

    return {"data" : [trace], "layout" : layout}

def generate_indicator_box(text, id_value):
    return html.Div(
            [
                html.P(
                    text,
                    className = "twelve columns indicator_text"
                    ),

                html.P(
                    id = id_value,
                    className="indicator_value"
                    ),
                ], 

            className = "three columns indicator"
            )

