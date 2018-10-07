import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go
from DataManager import DataManager
import colorlover as cl

bupu = cl.scales['9']['seq']['BuPu']
bupu500 = cl.interp( bupu, 500 ) # Map color scale to 500 bins

dm = DataManager()
project_counts = dm.get_project_count()
certified_projects = dm.get_certified_projects()
total_requested = dm.get_total_requested()
total_certified  = dm.get_total_certified()
sectors_by_region = dm.get_sectors_by_region()
top_10_sectors_by_project_count = dm.get_top_10_sectors_by_project_count()
top_6_codes = dm.get_top_6_codes()
budget_object_codes_by_region = dm.get_budget_object_codes_by_region()

def pull_regions():
    sectors_by_region_statewide = dm.get_sectors_by_region_statewide()
    return sectors_by_region_statewide

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


#build_sectors_by_region_helper function
def render_pie_sectors_by_region(region):
    return {'data': [
        go.Pie(
            labels = sectors_by_region[region]['sectors.sector'],
            values = sectors_by_region[region]['proposals_institutions.count'],
            marker = dict(
                line=dict(color='#000000', width=2))
            )
        ],
                'layout': go.Layout(
                    title="Sectors by Region", 
                    legend=dict(font=dict(size=12))
                    )}

def build_sectors_by_region_pie(region):
    if region == 'bay_area':
        return render_pie_sectors_by_region(region)
    elif region == 'central_mother_lode':
        return render_pie_sectors_by_region(region)
    elif region == 'north_far_north':
        return render_pie_sectors_by_region(region)
    elif region == 'los_angeles_orange_county':
        return render_pie_sectors_by_region(region)
    elif region == 'inland_empire_desert':
        return render_pie_sectors_by_region(region)
    elif region == 'south_central_coast':
        return render_pie_sectors_by_region(region)
    elif region == 'san_diego_imperial':
        return render_pie_sectors_by_region(region)
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


### helper for build_top_10 sectors by proj count
def render_bar_top_10_sectors_by_project_count(region):
    return { 'data': [
        go.Bar(
            x = top_10_sectors_by_project_count[region]['projects.count'], 
            y = top_10_sectors_by_project_count[region]['sectors.name'], 
            orientation='h', 
            marker = dict(
                color = 'rgb(255,140,0)',
                line=dict(color='#000000', width=2)
                )
            )
        ],
        'layout': go.Layout(
            title = "Top 10 Sectors by Project Count", 
            font=dict(size=10),
            margin = dict(
                l=250, r=15, pad=4
              ),
            xaxis=dict(tickangle=-25),
            yaxis=dict(
                showticklabels=True,
                ),
            )
        }

def build_top_10_sectors_by_project_count_bar(region):
    if region == 'bay_area':
        return render_bar_top_10_sectors_by_project_count(region)
    elif region == 'central_mother_lode':
        return render_bar_top_10_sectors_by_project_count(region)
    elif region == 'north_far_north':
        return render_bar_top_10_sectors_by_project_count(region)
    elif region == 'los_angeles_orange_county':
        return render_bar_top_10_sectors_by_project_count(region)
    elif region == 'inland_empire_desert':
        return render_bar_top_10_sectors_by_project_count(region)
    elif region == 'south_central_coast':
        return render_bar_top_10_sectors_by_project_count(region)
    elif region == 'san_diego_imperial':
        return render_bar_top_10_sectors_by_project_count(region)
    else:
        return { 'data': [
            go.Bar(
                x = top_10_sectors_by_project_count['statewide']['projects.count'], 
                y = top_10_sectors_by_project_count['statewide']['sectors.name'], 
                orientation='h', 
                marker = dict(
                    color = 'rgb(255,140,0)', 
                    line=dict(color='#000000', width=2)
                    )
                )
            ],
            'layout': go.Layout(
                title = "Top 10 Sectors by Project Count", 
                font=dict(size=10),
                margin = dict(
                    l=250, r=15, pad=5
                  ),
                xaxis=dict(
                    showticklabels=True,
                    ),
                yaxis=dict(
                    showticklabels=True,
                    ),
                )
            }

## helper fn
def render_bar_top_6_codes(region):
    return { 'data': [
        go.Bar(
            x = top_6_codes[region]['projects.count'], 
            y = top_6_codes[region]['top6_codes.top_codes'], 
            orientation='h', 
            marker = dict(
                color = 'rgb(255,0,255)',
                line=dict(color='#000000', width=2)
                )
            )
        ],
        'layout': go.Layout(
            title = "Project Top 10 Top 6 Codes", 
            font=dict(size=10),
            margin = dict(
                l=270, r=15, pad=5
              ),
            xaxis=dict(),
            yaxis=dict(
                showticklabels=False,
                ),
            )
        }

def build_top_6_codes(region):
    if region == 'bay_area':
        return render_bar_top_6_codes(region)
    elif region == 'central_mother_lode':
        return render_bar_top_6_codes(region)
    elif region == 'north_far_north':
        return render_bar_top_6_codes(region)
    elif region == 'los_angeles_orange_county':
        return render_bar_top_6_codes(region)
    elif region == 'inland_empire_desert':
        return render_bar_top_6_codes(region)
    elif region == 'south_central_coast':
        return render_bar_top_6_codes(region)
    elif region == 'san_diego_imperial':
        return render_bar_top_6_codes(region)
    else:
        return { 'data': [
            go.Bar(
                x = top_6_codes['statewide']['projects.count'], 
                y = top_6_codes['statewide']['top6_codes.top_codes'], 
                orientation='h', 
                marker = dict(
                    color = 'rgb(255,0,255)',
                    line=dict(color='#000000', width=2)
                    )
                )
            ],
            'layout': go.Layout(
                title = "Project Top 10 Top 6 Codes", 
                font=dict(size=10),
                margin = dict(
                    l=270, r=15, pad=4
                  ),
                xaxis=dict(
                    showticklabels=True),
                yaxis=dict(
                    showticklabels=True,
                    ),
                )
            }


def render_bar_budget_object_codes_by_region(region):
    return { 'data': [
        go.Bar(
            x = budget_object_codes_by_region[region]['object_codes.object_code'], 
            y = budget_object_codes_by_region[region]['budget_items.budget'], 
            marker = dict(
                color = 'rgb(255,0,255)',
                line=dict(color='#000000', width=2)
                )
            )
        ],
        'layout': go.Layout(
            title = "Budget Object Codes by Region", 
            font=dict(size=10),
            margin = dict(
                l=270, r=15, pad=5
              ),
            xaxis=dict(),
            yaxis=dict(
                showticklabels=False,
                ),
            )
        }
def build_budget_object_codes_by_region(region):
    if region == 'bay_area':
        return render_bar_budget_object_codes_by_region(region)
    elif region == 'central_mother_lode':
        return render_bar_budget_object_codes_by_region(region)
    elif region == 'north_far_north':
        return render_bar_budget_object_codes_by_region(region)
    elif region == 'los_angeles_orange_county':
        return render_bar_budget_object_codes_by_region(region)
    elif region == 'inland_empire_desert':
        return render_bar_budget_object_codes_by_region(region)
    elif region == 'south_central_coast':
        return render_bar_budget_object_codes_by_region(region)
    elif region == 'san_diego_imperial':
        return render_bar_budget_object_codes_by_region(region)
    else:
        return { 'data': [
            go.Bar(
                x = budget_object_codes_by_region['statewide']['object_codes.object_code'], 
                y = budget_object_codes_by_region['statewide']['budget_items.budget'], 
                marker = dict(
                    color = 'rgb(255,0,255)',
                    line=dict(color='#000000', width=2)
                    )
                )
            ],
            'layout': go.Layout(
                title = "Budget Object Codes by Region", 
                font=dict(size=10),
                margin = dict(
                    l=270, r=15, pad=5
                  ),
                xaxis=dict(),
                yaxis=dict(
                    showticklabels=False,
                    ),
                )
            }
