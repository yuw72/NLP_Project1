import string
import json
import nltk;
import spacy
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import re

def find_before(text):
    for i in range(len(text)):
#         print(text[i])
        if re.match('w[io]n?',text[i]):
            return text[i-2]+" "+text[i-1]
    
def find_after(text):
    for i in range(len(text)):
#         print(text[i])
        if text[i]=='goes':
            result = text[i+1]
            if i+2<len(text):
                result = result + " " + text[i+2]
            return result

        if text[i]==':':
            result = ""
            if i+1<len(text):
                result = text[i+1]
            if i+2<len(text):
                result = result +" "+ text[i+2]
            return result

def extract_award(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
#     filtered_sentence = [w for w in word_tokens if not w in stop_words]
    gg_stop_words = ['Globe', 'RT', 'http', 'Golden', 'Globes', 'GoldenGlobes', 'Goldenglobes', 'Goldenglobe', 'gg','golden globes', 'golden globe', 'goldenglobe','goldenglobes','gg2015','gg15','goldenglobe2015','goldenglobe15','goldenglobes2015','goldenglobes15', 'gg2013','gg13','goldenglobe2013','goldenglobe13','goldenglobes2013','goldenglobes13', 'rt', '2013', '2015', '...', '`', 'MTVNews']
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words and w not in gg_stop_words:
#             w = w.replace('-',",")
            w = w.replace('/',",")
            filtered_sentence.append(w)
    result = ""
    for i in range(len(filtered_sentence)):
#         print(filtered_sentence[i])
        if re.match('goes',filtered_sentence[i]):
#             print('match goes to')
            return find_after(filtered_sentence)

        if re.match('win',filtered_sentence[i]):
            return find_before(filtered_sentence)
#             print('match win')
        if re.match(':', filtered_sentence[i]):
            return find_after(filtered_sentence)
#             print('match :')
    
    return ""

import Levenshtein as lev

def leven(str1, str2):
    Distance = lev.distance(str1.lower(), str2.lower())
    Ratio = lev.ratio(str1.lower(), str2.lower())
#     print(Ratio)
    if Ratio > .95:
        return True
    else:
        return False

import imdb
def validate_name(name):
    ia = imdb.IMDb()
    people = ia.search_person(name)
    for p in people:
        str1 = p['name']
        str2 = name
        if leven(str1,str2):
            return True
    return False

def get_names(text,nlp):
    article = nlp(text)
    labels = [x.label_ for x in article.ents]
    [(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(text) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]
    parts_of_speech = dict([(str(x), x.label_) for x in nlp(text).ents])
    names = []
    for (key, value) in parts_of_speech.items() :
        if(value == "PERSON") :
            names.append(key)
    return names

import re
import regex
from collections import Counter
def get_people_winner(tweets,award_names):
    nlp = spacy.load('en')
    stop_words = set(stopwords.words('english')) 
    reg = regex.Regex()
    results={}
    for movie in award_names:
    #     print(movie)
        if movie in reg.people_award:
    #         if movie != 'best performance by an actor in a supporting role in a motion picture':
    #             continue
            search_term = reg.getRegex(movie)
            
            word_size = 2
    #         print(search_term)
            result = []
            for tweet in tweets:  
                text = tweet['text']
                if 'RT' not in tweet['text']:
    #                 text = text.lower()
                    if re.search(search_term, text):
    #                     print(text)
                        winner = extract_award(text)
                        if winner:
                            result.append(winner)
    #                         print(winner)
            
    #         print(Counter(result).most_common())
            name = ""
            for res in Counter(result).most_common():
                name = res[0]
                if get_names(name,nlp) or validate_name(name):
                    break
            results[movie] = name
    return results
    # for key in results.keys():
    #     print(key,results[key])



from nltk.tokenize import RegexpTokenizer       
def validate_film(film_name):
    ia = imdb.IMDb()
    film = ia.search_movie(film_name)
    for f in film:
        str1 = f['title']
        str2 = film_name
        if leven(str1,str2):
            return True
    return False

def get_film_winner(tweets,award_names):
    reg = regex.Regex()
    # print(reg.film_award)
    results={}
    for movie in award_names:
    #     print(movie)
        if movie in reg.film_award:
    #         if movie != 'best original song - motion picture':
    #             continue
            search_term = reg.getRegex(movie)
            
            word_size = 2
    #         print(search_term)
            result = []
            for tweet in tweets:
                
                text = tweet['text']
                if 'RT' not in tweet['text']:
                    if re.search(search_term, text):
    #                     print(text)
                        A = re.findall(r'“(.*?)”', text)
                        B = re.findall(r'"(.*?)"', text)
                            
                        if len(A)!=0:
                            for sentence in A:
                                if len(sentence.split())<10:
                                    result.append(sentence.lower())
                        if len(B)!=0:
                            for sentence in B:
                                if len(sentence.split())<10:
                                    result.append(sentence.lower())
            
            
            if len(result)==0:
                for tweet in tweets:
                    text = tweet['text']
                    if 'RT' not in tweet['text']:
                        if re.search(search_term, text):
                                C = re.findall(r'-(.*?)-', text)
                                if len(C)!=0:
    #                                 print(text)
                                    for sentence in C:
                                        if len(sentence.split())<5:
                                            result.append(sentence.strip())
                

    #         print(Counter(result))
            name = ""
            for res in Counter(result).most_common():
                name = res[0]
                if validate_film(name):
                    name = res[0]
                    break
    #         name = Counter(result).most_common()[0][0]
            results[movie] = name
    return results          
    # for key in results.keys():
    #     print(key,results[key])
    # Counter(result).most_common()
# tweets = json.load(open("gg2013.json"))
# winner1 = get_film_winner(tweets)
# winner2 = get_people_winner(tweets)
# winner1.update(winner2)
# print(len(winner1))