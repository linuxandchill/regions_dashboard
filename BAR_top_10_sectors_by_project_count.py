import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from DataManager import *

bay_area_chart = dcc.Graph(
        id='bay-area-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_bay_area_t10sbpc['sectors.name'],
                    x = data_bay_area_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )

central_mother_lode_chart = dcc.Graph(
        id='central-mother-lode-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_central_mother_lode_t10sbpc['sectors.name'],
                    x = data_central_mother_lode_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )

north_far_north_chart = dcc.Graph(
        id='north-far-north-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_north_far_north_t10sbpc['sectors.name'],
                    x = data_north_far_north_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )

san_diego_imperial_chart = dcc.Graph(
        id='san-diego-imperial-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_san_diego_imperial_t10sbpc['sectors.name'],
                    x = data_san_diego_imperial_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )

inland_empire_desert_chart = dcc.Graph(
        id='inland-empire-desert-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_inland_empire_desert_t10sbpc['sectors.name'],
                    x = data_inland_empire_desert_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )

south_central_coast_chart = dcc.Graph(
        id='south-central-coast-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_south_central_coast_t10sbpc['sectors.name'],
                    x = data_south_central_coast_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )


los_angeles_orange_county_chart = dcc.Graph(
        id='los-angeles-orange-county-top-10-sectors-by-project-count',
        figure = {
            'data':[
                go.Bar(
                    y = data_los_angeles_orange_county_t10sbpc['sectors.name'],
                    x = data_los_angeles_orange_county_t10sbpc['projects.count'],
                    orientation='h'
                    )
                ],
            'layout': go.Layout(
                title = "Top 10 sectors by project count",
                hovermode = 'closest'
                )
            }
        )

