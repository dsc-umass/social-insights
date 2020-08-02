# App for Twitter sentiment classification

A bunch of scripts to collect tweets about US Elections 2020 candidates  using twitter API and a deep learning model to classify the sentiments of the accumulated tweets.

## Install Dependencies
```
pip3 install -r requirements.txt
```

### Scripts to mine tweets
```
python3 scraping_tweets.py
```
Keeps collecting tweets related to keywords 'Trump' and 'Biden' until stopped manually. It automatically takes care of 'Rate limit exceeded' exception thrown by twitter API.


```
python3 merging_tweets.py
```
This script merges the result of previous step into two CSV files.


### Running the App
```
python3 app.py <filename>.csv
```
The app displays the sentiments of the tweets in the given <filename>.csv as predicted by the RNN LSTM model. "1" represents positive comment and "0" represents negative comment.  
