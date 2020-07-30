import os, sys, glob
import pandas as pd 
import pickle

class Merger:
    def __init__(self):
        self.directory = {'home_dir': sys.path[0]}
        self.directory['db_dir'] = sys.path[0] + '/static/dataset'
        self.file_key = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)
    
    def mergeCSV(self):
        os.chdir(self.directory['db_dir'])
        df_trump = pd.DataFrame()
        df_biden = pd.DataFrame()
        for file in glob.glob("2020*.csv"):
            if 'trump' in file:
                new_df = pd.read_csv(file)
                df_trump = df_trump.append(new_df)
                os.remove(file)
            elif 'biden' in file:
                new_df = pd.read_csv(file)
                df_biden = df_biden.append(new_df)
                os.remove(file)

        df_trump.to_csv(self.file_key + "merged_trump_tweets.csv", index=False)
        df_trump.to_csv(self.file_key + "merged_biden_tweets.csv", index=False)


obj = Merger()
obj.mergeCSV()
