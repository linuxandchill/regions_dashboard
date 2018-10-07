import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from components import *
from app import app
import components
from DataManager import DataManager
from components import *

dm = DataManager()

sectors_by_region_statewide = components.pull_regions()
region_options = []
for region in sectors_by_region_statewide['institutions.region'].unique():
    region_options.append({'label':str(region), 'value':str(region)})

def render_radio_items():
    sectors_by_region_statewide = dm.get_sectors_by_region_statewide()
    region_options = [{'label':'Statewide', 'value':'statewide'}]
    for region in sectors_by_region_statewide['institutions.region'].unique():
        region_options.append({'label':str(region), 'value': str(region).lower().replace(" ", "_").replace("/", "_") })

    return region_options

content_layout = html.Div([
    ### RADIO BUTTONS 
    html.Div([
        dcc.RadioItems(id = 'regions-radio-items', 
            options = render_radio_items(),
            value = 'statewide',
            labelStyle={'display': 'inline-block'},
            style={'margin':'10'}
            )

        ], className='row'),  

    ### INDICATORS 
    html.Div(id = 'indicator-row', children = [
        generate_indicator_box("Project count", "project-count-ind"),
        generate_indicator_box("Certified projects", "certified-projects-ind"),
        generate_indicator_box("Total requested", "total-requested-ind"),
        generate_indicator_box("Total certified", "total-certified-ind"),

        ], className='row', style={'margin':'10', 'textAlign':'center'}),  

    ### SECTORS BY REGION PIE CHART 
    html.Div([
        html.Div([
            html.P("Sectors by Region"),
            '''
            dcc.Graph(id='sectors-by-region',
                figure = {
                    'data': [trace0, trace1, trace2, trace3],
                    'layout': go.Layout(
                        xaxis=dict(tickangle=-45),
                        barmode='group',
                        )
                    }
                ),

            '''
            ], className="chart_div"), 

        ], className = 'row',  style={'margin':'10'}), 

    ### TWO (6 cols each) BAR CHARTS 
    html.Div([
        html.Div([
            html.P("Top 10 Sectors by Project Count"),
            '''
            dcc.Graph(id='top-10-sectors-by-project-count',
                figure = {
                    'data': [trace0, trace1, trace2, trace3],
                    'layout': go.Layout(
                        xaxis=dict(tickangle=-45),
                        )
                    }
                ),
            '''
            ], className="six columns chart_div"), 

        html.Div([
            html.P("Project Top 10 - Top 6 Codes"), 
            '''
            dcc.Graph(id='project-top-10-top-6-codes',
                figure = {
                    'data': [trace0, trace1, trace2, trace3],
                    'layout': go.Layout(
                        xaxis=dict(tickangle=-45),
                        barmode='group',
                        )
                    }
                ),
            '''
            ], className="six columns chart_div"), 

        ], className = 'row', style={"margin":"10"}), 

    ### Budget Object Codes by Region grouped
    html.Div([
        html.Div([
            html.P("Budget Object Codes by Region"), 
            '''
            dcc.Graph(id='budget-object-codes-by-region',
                figure = {
                    'data': [trace0, trace1, trace2, trace3],
                    'layout': go.Layout(
                        xaxis=dict(tickangle=-45),
                        barmode='group',
                        )
                    }
                ),
            '''
            ], className="chart_div"), 
        ], className = 'row', style={"margin":"10"}), 

    ### Map
    html.Div([
        html.Div([
            html.P("Project Density by District")
            ], className="chart_div"), 
        ], className = 'row', style={"margin":"10"}), 

    ### Table
    html.Div([
        html.Div([
            html.P("Projects")
            ], className="chart_div"), 
        ], className = 'row', style={"margin":"10"}), 
    ### CLOSING MAIN BODY DIV
    ], )

@app.callback(Output("project-count-ind", "children"), 
        [ 
            Input("regions-radio-items","value")
            ])
def project_count_indicator_callback(region):
    return components.build_project_count_indicator(region)


@app.callback(Output("certified-projects-ind", "children"),
        [
            Input("regions-radio-items", "value")
            ])
def certified_projects_indicator_callback(region):
    return components.build_certified_projects_indicator(region)

@app.callback(Output("total-requested-ind", "children"), 
        [
            Input("regions-radio-items", "value")
            ])
def total_requested_indicator_callback(region):
    return components.build_total_requested_indicator(region)


@app.callback(Output("total-certified-ind", "children"),
        [
            Input("regions-radio-items", "value")
            ])
def total_certified_indicator_callback(region): 
    return components.build_total_certified_indicator(region)


