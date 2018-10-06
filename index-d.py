import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from pie import * 
from DataManager import *
from BAR_top_10_sectors_by_project_count import *
import content_layout import content

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.Div([
        html.Span("Strong Workforce Program Uses of Regional Share", className='app-title')
        ],
        className='row header', style={'padding-top':'10px', 'background':'#00c6ff',
'background': '-webkit-linear-gradient(to right, #00c6ff, #0072ff)',
'background': 'linear-gradient(to right, #00c6ff, #0072ff)' }
        ),

    #### html.Div class row
    #### INDICATORS HERE
    #### INDICATORS HERE
    #### INDICATORS HERE
    #### INDICATORS HERE

    dcc.RadioItems(
        id='radio-items',
        options = [
            {'label': 'Statewide', 'value': 'statewide'},
            {'label': 'Bay Area', 'value': 'bay_area_chart'},
            {'label': 'Central/Mother Lode', 'value': 'central_mother_lode_chart'},
            {'label': 'Inland Empire/Desert', 'value': 'inland_empire_desert_chart'},
            {'label': 'Los Angeles/Orange County', 'value': 'los_angeles_orange_county_chart'},
            {'label': 'North/Far North', 'value': 'north_far_north_chart'},
            {'label': 'San Diego/Imperial', 'value': 'san_diego_imperial_chart'},
            {'label': 'South Central Coast', 'value': 'south_central_coast'},
            ],
        value = 'statewide',
        labelStyle={'display': 'inline-block'}
        ),

    ### test radio items
    dcc.RadioItems(
        id='radio-items2',
        options = [
            {'label': 'USA', 'value': 'usa'},
            {'label': 'CHINA', 'value': 'china'},
            ],
        value = 'INSIDE RADIO ITEMS',
        labelStyle={'display': 'inline-block'}
        ),

    html.Div([
        html.Div(id='tab-content', className='row', style={"margin": "2% 3%"}), 
        #html.Div(id='bar-chart-content', className='row', style={"margin": "2% 3%"}), 
        html.Div([
            html.P("Test bar chart content title html.P"), 

            #place each graph here in the children section
            html.Div(id = 'bar-chart-div'), 
            ], className='six columns chart_div'), 

        html.P("LSJDFLKSDJFLKJS LJLKFJSDLKFJ", className='row'), 

        ], className='row', style={'marginTop': '5px'}), 

    html.Div([
        html.Div(id='main-content', className='row', style={"margin": "2% 3%"}), 
        #html.Div(id='bar-chart-content', className='row', style={"margin": "2% 3%"}), 
        html.Div([
            html.P("Test bar chart content title html.P"), 

            #place each graph here in the children section
            ], className='six columns chart_div'), 


        ], className='row', style={'marginTop': '5px'}), 


    html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
    html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet")
    ], className='row', style={'marginTop': '5px'})

### this function will create graphs
### based on the data
def return_bar(df, region):
    data = dcc.Graph(
            id='top-10-sectors-by-project-codes',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'LA'},
                    ],
                'layout': {
                    'title': ''
                    }
                }
            )
    layout = go.Layout(
            title = 'Top 10 Sectors By Project Codes',
            )

    return {'data' : data, 'layout' : layout}

@app.callback(
        Output("bar-chart-div", "children"),
        [Input("radio-items", "value")])
def render_top_10_sectors_by_project_count_bar_callback(selection):
    if selection == 'bay_area':
        ## load bay_area_chart
    elif selection == 'central_mother_lode':
        ## load data for region
    elif selection == 'inland_empire_desert':
        #load data
    elif selection == 'los_angeles_orange_county':
        #load data
    elif selection == 'north_far_north':
        #load data
    elif selection == 'san_diego_imperial':
        #load data
    elif selection == 'south_central_coast':
        #load data
    else:
        selection == 'statewide'

#@app.callback(Output("main-content", "children"), [Input("content")])

if __name__ == '__main__':
    app.run_server(debug=True)


### this will ultimately call return_bar()
@app.callback(
        Output("bar-chart-div", "children"),
        [Input("radio-items", "value")])
def render_bar_callback(selected_option):
    print("########################")
    if selected_option == 'usa': 
        return dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'LA'},
                        ],
                    'layout': {
                        'title': 'First return UNITED STATES'
                        }
                    }
                )
    else: 
        return dcc.Graph(
                id='example-graph2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Beijing'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Shangha'},
                        ],
                    'layout': {
                        'title': 'SECOND RADIO CHINAIi w'
                        }
                    }
                )

