import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from DataManager import DataManager

dm = DataManager()
project_counts = dm.get_project_count()
certified_projects = dm.get_certified_projects()
total_requested = dm.get_total_requested()
total_certified  = dm.get_total_certified()
sectors_by_region = dm.get_sectors_by_region()

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


def build_project_count_indicator(region): 
    #data comes in as dictionary {'bay_area': 270}
    if region == 'bay_area':
        return project_counts['bay_area']
    elif region == 'central_mother_lode':
        return project_counts['central_mother_lode']
    elif region == 'north_far_north':
        return project_counts['north_far_north']
    elif region == 'los_angeles_orange_county':
        return project_counts['los_angeles_orange_county']
    elif region == 'inland_empire_desert':
        return project_counts['inland_empire_desert']
    elif region == 'south_central_coast':
        return project_counts['south_central_coast']
    elif region == 'san_diego_imperial':
        return project_counts['san_diego_imperial']
    else:
        return project_counts['statewide']

def build_certified_projects_indicator(region):
    if region == 'bay_area':
        return certified_projects['bay_area']
    elif region == 'central_mother_lode':
        return certified_projects['central_mother_lode']
    elif region == 'north_far_north':
        return certified_projects['north_far_north']
    elif region == 'los_angeles_orange_county':
        return certified_projects['los_angeles_orange_county']
    elif region == 'inland_empire_desert':
        return certified_projects['inland_empire_desert']
    elif region == 'south_central_coast':
        return certified_projects['south_central_coast']
    elif region == 'san_diego_imperial':
        return certified_projects['san_diego_imperial']
    else:
        return certified_projects['statewide']

def build_total_requested_indicator(region):
    if region == 'bay_area':
        return total_requested['bay_area']
    elif region == 'central_mother_lode':
        return total_requested['central_mother_lode']
    elif region == 'north_far_north':
        return total_requested['north_far_north']
    elif region == 'los_angeles_orange_county':
        return total_requested['los_angeles_orange_county']
    elif region == 'inland_empire_desert':
        return total_requested['inland_empire_desert']
    elif region == 'south_central_coast':
        return total_requested['south_central_coast']
    elif region == 'san_diego_imperial':
        return total_requested['san_diego_imperial']
    else:
        return total_requested['statewide']

def build_total_certified_indicator(region):
    if region == 'bay_area':
        return total_certified[region]
    elif region == 'central_mother_lode':
        return total_certified[region]
    elif region == 'north_far_north':
        return total_certified[region]
    elif region == 'los_angeles_orange_county':
        return total_certified[region]
    elif region == 'inland_empire_desert':
        return total_certified[region]
    elif region == 'south_central_coast':
        return total_certified[region]
    elif region == 'san_diego_imperial':
        return total_certified[region]
    else:
        return total_certified['statewide']

def build_sectors_by_region_pie(region):
    if region == 'bay_area':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

    elif region == 'central_mother_lode':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

    elif region == 'north_far_north':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

    elif region == 'los_angeles_orange_county':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

    elif region == 'inland_empire_desert':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

    elif region == 'south_central_coast':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

    elif region == 'san_diego_imperial':
        return {'data': [
            go.Pie(
                labels = sectors_by_region[region]['sectors.sector'],
                values = sectors_by_region[region]['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region: {}".format(region), 
                        legend=dict(font=dict(size=12))
                        )}

    else:
        return {'data': [
            go.Pie(
                labels = sectors_by_region['statewide']['sectors.sector'],
                values = sectors_by_region['statewide']['proposals_institutions.count'],
                marker = dict(line=dict(color='#000000', width=2))
                )
            ],
                    'layout': go.Layout(
                        title="Sectors by Region", 
                        legend=dict(font=dict(size=12))
                        )}

