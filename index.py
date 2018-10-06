import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
#from pie import * 
from DataManager import *
#from BAR_top_10_sectors_by_project_count import *
from content_layout import content_layout
from app import app

data_manager = DataManager()

project_count = data_manager.get_project_count()
certified_projects = data_manager.get_certified_projects()
total_requested = data_manager.get_total_requested()
total_certified = data_manager.get_total_certified()

app.layout = html.Div([
    html.Div([
        html.Span("Strong Workforce Program Uses of Regional Share", className='app-title')
        ],
        className='row header', style={'padding-top':'10px', 'background':'#00c6ff',
'background': '-webkit-linear-gradient(to right, #00c6ff, #0072ff)',
'background': 'linear-gradient(to right, #00c6ff, #0072ff)' }
        ),

    html.Div(project_count,
        id="project-count-indicator",
        style={"display":"none"}),

    html.Div(certified_projects,
        id="certified-projects-indicator",
        style={"display":"none"}),

    html.Div(total_requested,
        id="total-requested-indicator",
        style={"display":"none"}),

    html.Div(total_certified,
        id="total-certified-indicator",
        style={"display":"none"}),
    ########

    html.Div([
        html.Div(id='main-content', className='row', style={"margin": "2% 3%"}), 
        #html.Div(id='bar-chart-content', className='row', style={"margin": "2% 3%"}), 


        html.Div([
            content_layout
            ], className="row", style={"margin": "2%"})

        ], className='row'), 


    html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)


'''
html.Div(data_manager.get_sectors_by_region_statewide().to_json(orient="split"), 
    id="sectors-by-region-statewide", 
    style={"display":"none"}), 

html.Div(data_manager.get_top_10_sectors_by_project_count_statewide().to_json(orient="split"),
    id="top-10-sectors-by-project-count-statewide",
    style={"display":"none"}),

html.Div(data_manager.get_budget_object_codes_by_region_statewide().to_json(orient="split"),
    id="budget-object-codes-by-region-statewide",
    style={"display":"none"}),

html.Div(data_manager.get_top_6_codes_statewide().to_json(orient="split"),
    id="top-6-codes-statewide",
    style={"display":"none"}),

html.Div(data_manager.get_project_count_ind_statewide(),
    id="project-count-indicator-statewide",
    style={"display":"none"}),

html.Div(data_manager.get_certified_projects_ind_statewide(),
    id="certified-projects-indicator-statewide",
    style={"display":"none"}),

html.Div(data_manager.get_total_requested_ind_statewide(),
    id="total-requested-indicator-statewide",
    style={"display":"none"}),

html.Div(data_manager.get_total_certified_ind_statewide(),
    id="total-certified-indicator-statewide",
    style={"display":"none"}),

'''
# HIDDEN dataframe divs
######## HIDDEN region filtered data calls
######## all fncs require region_name as first arg
''' 
html.Div(data_manager.get_sectors_by_region().to_json(orient="split"), 
    id="sectors-by-region", 
    style={"display":"none"}), 

html.Div(data_manager.get_top_10_sectors_by_project_count().to_json(orient="split"),
    id="top-10-sectors-by-project-count",
    style={"display":"none"}),

html.Div(data_manager.get_budget_object_codes_by_region().to_json(orient="split"),
    id="budget-object-codes-by-region",
    style={"display":"none"}),

html.Div(data_manager.get_top_6_codes().to_json(orient="split"),
    id="top-6-codes",
    style={"display":"none"}),
'''

