import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from utils import import_query_file
import sys
import os

class DataManager():
    def __init__(self):
        self.user = 'development_user'
        self.password = 'SDc8hd30sZBvkzDfPGoAcjZX'
        self.database = 'development_nova'
        self.engine = mysql.connector.connect(user=self.user, 
                password=self.password,
                database=self.database)

    def import_query_file(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
            return data

    ## Statewide functions
    def get_top_10_sectors_by_project_count_statewide(self): 
        query = self.import_query_file('./DATA_FILES/regions/statewide/top_10_sectors_by_project_count.txt')
        return pd.read_sql(query, self.engine)

    def get_sectors_by_region_statewide(self): 
        query = self.import_query_file('./DATA_FILES/regions/statewide/sectors_by_region.txt')
        return pd.read_sql(query, self.engine)

    def get_budget_object_codes_by_region_statewide(self):
        query = self.import_query_file('./DATA_FILES/regions/statewide/budget_object_codes_by_region.txt')
        return pd.read_sql(query, self.engine)

    def get_top_6_codes_statewide(self): 
        query = self.import_query_file('./DATA_FILES/regions/statewide/top_6_codes.txt')
        return pd.read_sql(query, self.engine)

    #####  Statewide Indicators

    def get_project_count_ind_statewide(self): 
        query = self.import_query_file('./DATA_FILES/regions/statewide/project_count.txt')
        res = pd.read_sql(query, self.engine)
        return res['projects.count'][0]

    def get_certified_projects_ind_statewide(self):
        query = self.import_query_file('./DATA_FILES/regions/statewide/certified_projects.txt')
        res = pd.read_sql(query, self.engine)
        return res['projects.count'][0]

    def get_total_requested_ind_statewide(self):
        query = self.import_query_file('./DATA_FILES/regions/statewide/total_requested.txt')
        res = pd.read_sql(query, self.engine)
        return '${:,.2f}'.format(res['budget_items.budget'][0])

    def get_total_certified_ind_statewide(self):
        query = self.import_query_file('./DATA_FILES/regions/statewide/total_certified.txt')
        res = pd.read_sql(query, self.engine)
        return '${:,.2f}'.format(res['budget_items.budget'][0])

    ##############################
    ##############################
    ##############################
    #### Region filtered functions
    ##############################
    ##############################
    ##############################
     
    def get_sectors_by_region(self, region_name='bay_area'):
        query = self.import_query_file('./DATA_FILES/regions/{}/sectors_by_region.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res

    def get_top_10_sectors_by_project_count(self, region_name='bay_area'): 
        query = self.import_query_file('./DATA_FILES/regions/{}/top_10_sectors_by_project_count.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res

    def get_budget_object_codes_by_region(self, region_name='bay_area'):
        query = self.import_query_file('./DATA_FILES/regions/{}/budget_object_codes_by_region.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res 

    def get_top_6_codes(self, region_name='bay_area'): 
        query = self.import_query_file('./DATA_FILES/regions/{}/top_6_codes.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res

    #indicators region filtered
    def get_project_count(self): 
        #for every folder in DATA_FILES/regions run query on project_count.txt
        project_count_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'project_count.txt':
                    project_count_dict.update({dirName: fname})

        project_counts = {} 
        for key, value in project_count_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            project_counts.update({key: res['projects.count'][0]})
            
        return project_counts

    def get_certified_projects(self, region_name='bay_area'):
        query = self.import_query_file('./DATA_FILES/regions/{}/certified_projects.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res['projects.count'][0]

    def get_total_requested(self, region_name='bay_area'):
        query = self.import_query_file('./DATA_FILES/regions/{}/total_requested.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res['budget_items.budget'][0]

    def get_total_certified(self, region_name='bay_area'):
        query = self.import_query_file('./DATA_FILES/regions/{}/total_certified.txt'.format(str(region_name)))
        res = pd.read_sql(query, self.engine)
        return res['budget_items.budget'][0]

'''
query = self.import_query_file('./DATA_FILES/regions/{}/project_count.txt'.format(str(region_name)))

'''

'''


'''
