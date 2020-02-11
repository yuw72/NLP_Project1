#imports
import json
import Levenshtein as lev
import datetime
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
import nltk
import re
from collections import Counter
import regex

def get_key(my_dict, val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key

def get_presenters(tweets):
    search_terms = [r'[Pp]resent']
    stop_terms = [r'[Rr]epresent']
    award_dict = reg = regex.Regex().award_dict
    gg_stop_words = ['Globe', 'RT', 'http', 'Golden', 'Globes', 'GoldenGlobes', 'Goldenglobes', 'Goldenglobe', 'gg','golden globes', 'golden globe', 'goldenglobe','goldenglobes','gg2015','gg15','goldenglobe2015','goldenglobe15','goldenglobes2015','goldenglobes15', 'gg2013','gg13','goldenglobe2013','goldenglobe13','goldenglobes2013','goldenglobes13', 'rt', '2013', '2015']
    awards = list(award_dict.values())
    clean_data = []
    for x in tweets:
        if 'RT' not in x['text']:
            clean_data.append(x)
    award_results = {}
    for x in clean_data:
        tweet = x["text"]
        for award_regex in awards:
            award = get_key(award_dict, award_regex)
            for search_term in search_terms:
                if re.search(search_term, tweet) and not re.search(stop_terms[0], tweet) and re.search(award_regex, tweet):
                    if award_results.get(award):
                        award_results[award].append(x['text'])
                    else:
                        award_results[award] = [x['text']]
                    break
    gg_stop_words = ['Globe', 'RT', 'http', 'Golden', 'Globes', 'GoldenGlobes', 'Goldenglobes', 'Goldenglobe', 'gg','golden globes', 'golden globe', 'goldenglobe','goldenglobes','gg2015','gg15','goldenglobe2015','goldenglobe15','goldenglobes2015','goldenglobes15', 'gg2013','gg13','goldenglobe2013','goldenglobe13','goldenglobes2013','goldenglobes13', 'rt', '2013', '2015', 'Best', 'BEST', 'Present', 'Presents', 'Angeles']
    final = {}
    proper = []
    for award in award_results.keys():
        final[award] = []
        proper_bi = []
        for tweet in award_results[award]:
            bigrams = list(nltk.bigrams(nltk.word_tokenize(tweet)))
            text = nltk.word_tokenize(tweet)
            tagged_text = nltk.pos_tag(text)
            ''' for single tokens:
            for token in tagged_text:
                if token[1] == "NNP" and token[0] not in gg_stop_words:
                    #print(token[0])
                    proper.append(token[0])
                    '''

            # tag double words with pos and pull out the two-proper-nouns-in-a-row
            for bigram in bigrams:
                tagged_text = nltk.pos_tag(bigram)
                if tagged_text[0][1] == "NNP" and tagged_text[0][0] not in gg_stop_words and tagged_text[1][1] == "NNP" and tagged_text[1][0] not in gg_stop_words:
                        proper_bi.append((tagged_text[0][0], tagged_text[1][0]))

        most_common = Counter(proper_bi).most_common()
        presenter_count = 3  # maximum of 3 presenters
        i = 0
        while len(most_common) > 1 and i < len(most_common)-1:
            # combine any 3-name sets among the most common, eg "Sacha Baron Cohen". >3 names is not accounted for.
            if(most_common[i][0][1] == most_common[i+1][0][0]):
                if presenter_count > 0:
                    final[award].append(most_common[i][0][0] + ' ' + most_common[i][0][1] + ' ' + most_common[i+1][0][1])
                    del most_common[i]
                    del most_common[i]
                    presenter_count = presenter_count - 1
            else:
                i = i + 1
        # fill in the rest of the most common up to the top 3 (seems like max # of presenters is 3)
        while presenter_count > 0 and len(most_common) != 0:
            presenter_count = presenter_count - 1
            final[award].append(most_common[0][0][0] + ' ' + most_common[0][0][1])
            del most_common[0]
            

    for award in award_dict.keys():
        if not award in final:
            final[award] = ["a", "e"]
            
#     print(final)
    return(final)
# todo improvements: remove references to the award name
# todo improvements: remove winners
# todo improvements: check against name database somehow? or else screen out common words?
# todo improvements: combine misspellings - how?
# todo improvements: change all casing to Xxxxx Xxxxx
# todo improvements: check name/word right before "presents"
