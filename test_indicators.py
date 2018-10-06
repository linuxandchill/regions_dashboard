import pandas as pd
import mysql.connector
import sys
from sqlalchemy import create_engine
import utils.import_query_file

def import_query_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return data

engine = mysql.connector.connect(user='development_user', password='SDc8hd30sZBvkzDfPGoAcjZX',  database='development_nova')


project_count_query = import_query_file('project_count.txt')
project_count = pd.read_sql(project_count_query, engine)

certified_projects_query = import_query_file('certified_projects.txt')
certified_projects = pd.read_sql(certified_projects_query, engine)

total_requested_query = import_query_file('total_requested.txt')
total_requested = pd.read_sql(total_requested_query, engine)

total_certified_query = import_query_file('total_certified.txt')
total_certified = pd.read_sql(total_certified_query, engine)

indicators = {
        "project_count": project_count,
        "certified_projects": certified_projects.iloc[0,1],
        "total_requested": total_requested,
        "total_certified": total_certified
        }

print(indicators['certified_projects'])

