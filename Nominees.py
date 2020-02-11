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

def get_film_nominee(tweets, award_names, winners):
    reg = regex.Regex()
    # print(reg.film_award)
    results={}
    for movie in award_names:
    #     print(movie)
        cnt = 0
        if movie in reg.film_award:
    #         movie = ' best original song - motion picture '
            search_term = winners[movie]
            # search_term = reg.getRegex(movie)
            
            word_size = 2
    #         print(search_term)
            result = []
            for tweet in tweets:
                if cnt>500000:
                    break
                cnt += 1
                text = tweet['text'].lower()
                if 'RT' not in tweet['text']:
                    if re.search(search_term, text):
                        text = text.replace(',', "")
                        text = text.replace('.', "")
                        text = text.replace('!', "")
                        #text.translate(str.maketrans('', '', string.punctuation))
                        #                     print(text)
                        A = re.findall(r'“(.*?)”', text)
                        B = re.findall(r'"(.*?)"', text)
                            
                        if len(A)!=0:
                            for sentence in A:
                                if len(sentence.split())<10:
                                    if search_term not in sentence and '@' not in sentence and '#' not in sentence and 'best' not in sentence and sentence != '':
                                        result.append(sentence)
    #                                     movie_title = isMovie(sentence)
    #                                     if movie_title:
    #                                         result.append(movie_title)
                        if len(B)!=0:
                            for sentence in B:
                                if len(sentence.split())<10:
                                    if search_term not in sentence and '@' not in sentence and '#' not in sentence and 'best' not in sentence and sentence != '':
                                        result.append(sentence)
    #                                     movie_title = isMovie(sentence)
    #                                     if movie_title:
    #                                         result.append(movie_title)
            
            
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
                                            if search_term not in sentence and '@' not in sentence and '#' not in sentence:
                                                result.append(sentence)

            cnt = 0
            idx = 0
            answer = []
            while cnt<4 and idx<len(result):
                movie_title = isMovie(result[idx])
                
                if movie_title:
    #                 print(movie_title)
                    answer.append(movie_title)
                    cnt += 1
                idx += 1
            for i in range(cnt,4):
                answer.append('a')

            results[movie] = answer
    return results

def get_people_nominee(tweets, award_names, winners):
    reg = regex.Regex()
    results={}
    for movie in award_names:
        if movie in reg.people_award:
            search_term = winners[movie]

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
                    
    return results

def get_nominees(tweets, award_names, winners):
    nominees1 = get_film_nominee(tweets, award_names, winners)
    # print("finish getting film nominees")
    nominees2 = get_people_nominee(tweets, award_names, winners)
    # print("finish getting people nominees")
    nominees1.update(nominees2)
    return nominees1

# tweets = json.load(open("gg2013.json"))
# award_names = OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
# nominees = get_nominees(tweets, award_names)
# print(nominees)