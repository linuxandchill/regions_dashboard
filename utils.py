import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly import graph_objs as go

def import_query_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return data

        
#print(import_query_file('Bay_Area_t10sbpc.txt'))
'''
folder_ext = './DATA_FILES/'
##CREATE SQLALCHEMY ENGINE 
#engine = create_engine('mysql+mysqlconnector://ccccoadmin:71jIP8hmBqKszhmXuMil2wc7@cccco-nova-cluster-1.cluster-c9r56oodso6l.us-west-1.rds.amazonaws.com:3306/sandbox_nova', echo=False)

engine = mysql.connector.connect(user='development_user', password='SDc8hd30sZBvkzDfPGoAcjZX',  database='development_nova')

bay_area_t10sbpc = import_query_file(folder_ext + 'Bay_Area_t10sbpc.txt')
central_mother_lode_t10sbpc = import_query_file(folder_ext + 'Central_Mother_Lode_t10sbpc.txt')
north_far_north_t10sbpc = import_query_file(folder_ext + 'North_Far_North_t10sbpc.txt')
san_diego_imperial_t10sbpc = import_query_file(folder_ext + 'San_Diego_Imperial_t10sbpc.txt')
inland_empire_desert_t10sbpc = import_query_file(folder_ext + 'Inland_Empire_Desert_t10sbpc.txt')
south_central_coast_t10sbpc = import_query_file(folder_ext + 'South_Central_Coast_t10sbpc.txt')
los_angeles_orange_county_t10sbpc = import_query_file(folder_ext + 'Los_Angeles_Orange_County_t10sbpc.txt')

data_bay_area_t10sbpc = pd.read_sql(bay_area_t10sbpc, engine)
data_central_mother_lode_t10sbpc = pd.read_sql(central_mother_lode_t10sbpc, engine)
data_north_far_north_t10sbpc = pd.read_sql(north_far_north_t10sbpc, engine)
data_san_diego_imperial_t10sbpc = pd.read_sql(san_diego_imperial_t10sbpc, engine)
data_inland_empire_desert_t10sbpc = pd.read_sql(inland_empire_desert_t10sbpc, engine)
data_south_central_coast_t10sbpc = pd.read_sql(south_central_coast_t10sbpc, engine)
data_los_angeles_orange_county_t10sbpc = pd.read_sql(los_angeles_orange_county_t10sbpc, engine)

#print(data_bay_area_10tsbpc)

'''
