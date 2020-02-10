#imports
import json
import Levenshtein as lev
import datetime
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
import nltk
import re
from collections import Counter
import json
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import regex
import string  
import imdb


def get_key(my_dict, val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key
        
def get_winner(movie):
    # TODO: make a real version of this
    answers = json.load(open("gg2013answers.json"))
    return answers["award_data"][movie]["winner"]

def leven(str1, str2):
    Distance = lev.distance(str1.lower(), str2.lower())
    Ratio = lev.ratio(str1.lower(), str2.lower())
    if Ratio > .9:
        return True
    else:
        return False
    
def isMovie(movie):
    ia = imdb.IMDb()
    movies = ia.search_movie(movie)
    if len(movies)==0:
        return False
    
    str1 = movie
    str2 = movies[0]['title']
    for m in movies:
        str2 = m['title']
        if leven(str1,str2):
            return str2
    return False

def get_nominees(file):
    tweets = json.load(open(file))
    reg = regex.Regex()
    results={}
    for movie in reg.award_names:
        if movie in reg.people_award:
            search_term = get_winner(movie)

            word_size = 2
            result = []
            for tweet in tweets:
                text = tweet['text'].lower()
                if 'RT' not in tweet['text']:
                    if re.search(search_term, text):
                        text = text.replace(',', "")
                        text = text.replace('.', "")
                        text = text.replace('!', "")
                        A = re.findall(r'“(.*?)”', text)
                        B = re.findall(r'"(.*?)"', text)

                        if len(A)!=0:
                            for sentence in A:
                                if len(sentence.split())<10:
                                    if search_term not in sentence and '@' not in sentence and '#' not in sentence and 'best' not in sentence and sentence != '':
                                        result.append(sentence)
                        if len(B)!=0:
                            for sentence in B:
                                if len(sentence.split())<10:
                                    if search_term not in sentence and '@' not in sentence and '#' not in sentence and 'best' not in sentence and sentence != '':
                                        result.append(sentence)



            if len(result)==0:
                for tweet in tweets:
                    text = tweet['text']
                    if 'RT' not in tweet['text']:
                        if re.search(search_term, text):
                                C = re.findall(r'-(.*?)-', text)
                                if len(C)!=0:
                                    for sentence in C:
                                        if len(sentence.split())<5:
                                            if search_term not in sentence and '@' not in sentence and '#' not in sentence:
                                                result.append(sentence)

            most_common = Counter(result).most_common()
            if len(most_common) != 0:
                results[movie] = [(most_common[0][0])]
                
            for i in range(1,5):
                if len(most_common) > i:
                    results[movie].append(most_common[i][0])
            for award in reg.award_dict.keys():
                if not award in results:
                    results[award] = ["a", "e", "i", "o", "u"]
                    
    return(results)