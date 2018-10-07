import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
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
        temp_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'sectors_by_region.txt':
                    temp_dict.update({dirName: fname})

        final_dict = {} 
        for key, value in temp_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            final_dict.update({key: res})
            
        return final_dict

    def get_top_10_sectors_by_project_count(self): 
        temp_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'top_10_sectors_by_project_count.txt':
                    temp_dict.update({dirName: fname})

        final_dict = {} 
        for key, value in temp_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            final_dict.update({key: res})
            
        return final_dict

    def get_budget_object_codes_by_region(self, region_name='bay_area'):
        temp_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'budget_object_codes_by_region.txt':
                    temp_dict.update({dirName: fname})

        final_dict = {} 
        for key, value in temp_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            final_dict.update({key: res})
            
        return final_dict

    def get_top_6_codes(self): 
        temp_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'top_6_codes.txt':
                    temp_dict.update({dirName: fname})

        final_dict = {} 
        for key, value in temp_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            final_dict.update({key: res})
            
        return final_dict

    #indicators region filtered
    def get_project_count(self): 
        #for every folder in DATA_FILES/regions/ run query on project_count.txt
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
        certified_projects_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'certified_projects.txt':
                    certified_projects_dict.update({dirName: fname})

        certified_projects = {} 
        for key, value in certified_projects_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            certified_projects.update({key: res['projects.count'][0]})

        return certified_projects


    def get_total_requested(self):
        total_requested_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'total_requested.txt':
                    total_requested_dict.update({dirName: fname})

        total_requested = {} 
        for key, value in total_requested_dict.items():
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            total_requested.update({key: '${:,.0f}'.format(res['budget_items.budget'][0])})

        return total_requested

    def get_total_certified(self):
        total_certified_dict = {}
        rootDir = "./DATA_FILES/regions/"
        for dirName, subDirList, fileList in os.walk(rootDir):
            for fname in fileList:
                if fname == 'total_certified.txt':
                    total_certified_dict.update({dirName: fname})


        total_certified = {}
        for key, value in total_certified_dict.items(): 
            query = self.import_query_file('{}/{}'.format(key, value))
            res = pd.read_sql(query, self.engine)
            key = key.split("/")[-1]
            total_certified.update({key: '${:,.0f}'.format(res['budget_items.budget'][0])})

        return total_certified




