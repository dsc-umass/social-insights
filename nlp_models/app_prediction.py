from keras.models import load_model
import keras
import pickle
import re
import sys, os
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import warnings
warnings.filterwarnings("ignore")
 

class Model:
    def __init__(self):
        self.script_name = os.path.basename(__file__)
        home_dir = os.path.abspath(__file__)[:-len(self.script_name)]
        self.directory = {'home_dir': home_dir}
        self.directory['db_dir'] = home_dir + 'static/dataset/'
        self.directory['model_dir'] = home_dir + 'static/models/'
        pickle_file = open(self.directory['db_dir'] + "tokenizer.pickle", "rb")
        self.tokenizer = pickle.load(pickle_file)
        self.model = load_model(self.directory['model_dir'] + "rnn_lstm_twitter.h5")


    def remove_tags(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', text)

    def preprocess(self, text):
        sentence = self.remove_tags(text)     # Removing html tags
        sentence = re.sub('[^a-zA-Z]', ' ', sentence)       # Remove punctuations and numbers
        sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)     # Single character removal
        sentence = re.sub(r'\s+', ' ', sentence)        # Removing multiple spaces
        return sentence

    def predict(self, instance):
        instance = self.preprocess(instance)
        instance = self.tokenizer.texts_to_sequences(instance)
        flat_list = []
        for sublist in instance:
            for item in sublist:
                flat_list += item,

        flat_list = [flat_list]
        instance = pad_sequences(flat_list, padding = 'post', maxlen = 35)
        prob = self.model.predict(instance)
        return 1 if prob > 0.5 else 0

