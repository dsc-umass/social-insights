import os, sys, glob
import pandas as pd 
import pickle

home_dir = sys.path[0]
db_dir = home_dir + '/static/dataset/'
os.chdir(db_dir)

idSet = set()
for file in glob.glob("*.csv"):
    if file[:4]=='2020':
        df = pd.read_csv(file)
        for id in df['id']:
            idSet.add(id)

pickle_file = open("id_set.pickle", "wb")
pickle.dump(idSet, pickle_file)
pickle_file.close()
