import subprocess, time, sys, os
from datetime import datetime

class Scraper:
    def __init__(self):
        self.directory = {'home_dir': sys.path[0]}
        self.toggle = 1 
    
    def scrape_tweets(self):
        if self.toggle:
            self.scrape_trump_tweets()
            print("Done scraping trump tweets.....")
        else:
            self.scrape_biden_tweets()
            print("Done scraping biden tweets.....")
        
        # update id_set.pickle
        run_id_set = subprocess.run(["python3", "analyzing_redundant_tweets.py"], capture_output = True)
        self.toggle = 1 - self.toggle

    def scrape_trump_tweets(self):
        os.chdir(self.directory['home_dir'])
        cmd = subprocess.run(["python3", "bar_chart_race.py", 'trump'], capture_output = True)
        
    def scrape_biden_tweets(self):
        os.chdir(self.directory['home_dir'])
        cmd = subprocess.run(["python3", "bar_chart_race.py", 'biden'], capture_output = True)
    

scraper = Scraper() 
while True:
    time.sleep(60*15) # wait for 15 mins before attempting again
    scraper.scrape_tweets()
    