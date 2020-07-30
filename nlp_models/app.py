from flask import Flask, render_template, url_for
import os
import sys
import glob
import pandas as pd
from app_prediction import Model

 
script_name = os.path.basename(__file__)
home_dir = os.path.abspath(__file__)[:-len(script_name)]
db_dir =  home_dir + 'static/dataset/'

app = Flask(__name__)


@app.route('/')
def home_page():
    csv_file = sys.argv[1] if len(sys.argv)>1 else "merged_tweets.csv"
    df = pd.read_csv(db_dir + csv_file)
    ml_model = Model()
    ids, tweets, predictions = [], [], []
    for i in range(len(1000)):
        ids += df['id'][i],
        tweets += df['text'][i],
        predictions += ml_model.predict(df['text'][i]),
    data = {'ID': ids, 'TWEET': tweets, 'SENTIMENT': predictions}
    return render_template('home.html', content = data, size = len(ids))

if __name__ == "__main__":
    app.run(debug=True)