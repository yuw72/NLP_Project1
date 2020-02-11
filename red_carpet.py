import re
import statistics
import spacy
import string
import json
import nltk
import operator
from collections import Counter
import collections
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

nlp = spacy.load('en')

def parse_tweets_rc(tweets):
    nlp = spacy.load('en')
    stop_words = set(stopwords.words('english')) 

    gg_stop_words = ['HuffingtonPost','amp', 'Globe', 'RT', 'http', 'Golden', 'Globes', 'GoldenGlobes', 'Goldenglobes', 'Goldenglobe', 'gg','golden globes', 'golden globe', 'goldenglobe','goldenglobes','gg2015','gg15','goldenglobe2015','goldenglobe15','goldenglobes2015','goldenglobes15', 'gg2013','gg13','goldenglobe2013','goldenglobe13','goldenglobes2013','goldenglobes13', 'rt', '2013', '2015', '...', '`', 'MTVNews']

    rc_stop_words = ['eredcarpet', '\'', 'lt', 'damn', '^']

    gg_stop_words.extend(stop_words)
    gg_stop_words.extend(rc_stop_words)

    rc_tweets = []
    for t in tweets:
        text = t['text']
        if re.search(r'.*red.*carpet.*', text.lower()):
            rc_tweets.append(text)

    clean_tweets = []
    for text in rc_tweets:
        text_tokens = word_tokenize(text)
        t = []
        sent = ''
        for w in text_tokens:
            if w.lower() not in gg_stop_words:
                if w not in string.punctuation: 
                    no_url = re.sub(r'(//t.co.*|`)', '', w) # remove urls
                    t.append(no_url)
        for i in range(len(t)): 
            sent += t[i] + ' '
        clean_tweets.append(sent)

    return clean_tweets

def get_names(text):
    names = []
    article = nlp(text)
    entities = [(ent.text, ent.label_) for ent in article.ents]
    for ent in entities:
        if ent[1] == 'PERSON' and len(ent[0].split()) == 2:
            names.append(ent[0])
    return names

def best_dressed(tweets):
    pos_words = ['beautiful', "ravishing", 'gorgeous', 'stunning',
                 'attractive', 'pretty', 'handsome', 'good',
                 'prepossessing', 'lovely',  
                 'ravishing', 'glamorous', 
                 'elegant', 'exquisite',
                 'cute', 'photogenic', 'sexy']
    positive_sent = []
    for t in tweets:
        if bool([ele for ele in pos_words if(ele in t)]):
            positive_sent.append(t)
    count = {}
    for t in positive_sent: 
        names = get_names(t)
        for name in names :
            if len(name.split()) == 2:
                if name in count :
                    count[name] = count[name] + 1
                else:
                    count[name] = 1
    winners = Counter(count).most_common(5)
    result = []
    for n in winners:
        result.append(n[0])
    return result

def worst_dressed(tweets):
    
    neg_words = ['bad', 'worst', 'awful', 'horrible', 'suck', 'poor']
    neg_sent = []
    for t in tweets:
        if bool([ele for ele in neg_words if(ele in t)]):
            neg_sent.append(t)

    count = {}
    for t in neg_sent: 
        names = get_names(t)
        for name in names :
            if len(name.split()) == 2:
                if name in count :
                    count[name] = count[name] + 1
                else:
                    count[name] = 1
    winners = Counter(count).most_common(5)
    result = []
    for n in winners:
        result.append(n[0])
    return result

def most_controversial(best, worst):
    controversial = []
    for b in best:
        for w in worst:
            if b == w:
                controversial.append(w)
    return controversial

def most_discussed(tweets):
    count = {}
    names = []
    for t in tweets:
        names = get_names(t)
    for name in names :
        if len(name.split()) == 2:
            if name in count :
                count[name] = count[name] + 1
            else:
                count[name] = 1
    winner = max(count.items(), key=operator.itemgetter(1))[0]
    return winner

def results(tweets):
    b = best_dressed(tweets)
    w = worst_dressed(tweets)
    c = most_controversial(b, w)
    m = most_discussed(tweets)
    return b, w, c, m

