'''Version 0.35'''
import json
import os
import winners as win
import Presenters as pres
import Nominees as noms
import allAwards
import host


OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']
tweets = []
winners = {}
def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    print("get hosts")
    filename = 'gg'+year+'.json'
    tweets = json.load(open(filename))
    hosts = host.get_hosts(tweets)
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    print("get awards")
    awards = []
    if year == '2013' or year == '2015':
        award_names = OFFICIAL_AWARDS_1315
    else:
        award_names = OFFICIAL_AWARDS_1819
    filename = 'gg'+year+'.json'
    tweets = json.load(open(filename))
    # awards = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
    # awards[1] = "hahahahah"
    awards = allAwards.get_allAwards(tweets,year)
    # print('awards length: ',len(awards))
    # print('answer length: ',len(OFFICIAL_AWARDS_1315))
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    print("get nominees")
    if year == '2013' or year == '2015':
        award_names = OFFICIAL_AWARDS_1315
    else:
        award_names = OFFICIAL_AWARDS_1819
    
#     nominees = {}
#     for name in award_names:
#         nominees[name] = 'a'

    global tweets
    global winner_has_run
    filename = 'gg'+year+'.json'
    tweets = json.load(open(filename))
    winners = get_winner(year)
    print("finish winners")
    nominees = noms.get_nominees(tweets, award_names, winners)
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    global winners
    print("get winners")

    if year == '2013' or year == '2015':
        award_names = OFFICIAL_AWARDS_1315
    else:
        award_names = OFFICIAL_AWARDS_1819

    global tweets
    filename = 'gg'+year+'.json'
    tweets = json.load(open(filename))
    winner1 = win.get_film_winner(tweets, award_names)
    winner2 = win.get_people_winner(tweets, award_names)
    winner1.update(winner2)
    winners = winner1
    return winner1

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    print("get presenters")
    if year == '2013' or year == '2015':
        award_names = OFFICIAL_AWARDS_1315
    else:
        award_names = OFFICIAL_AWARDS_1819
    

    global tweets
    filename = 'gg'+year+'.json'
    tweets = json.load(open(filename))
    presenters = pres.get_presenters(tweets)
    # print("winners:",winners)
    
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    # print("run main")
    year = '2013'
    if year == '2013' or year == '2015':
        award_names = OFFICIAL_AWARDS_1315
    else:
        award_names = OFFICIAL_AWARDS_1819
    
    filename = 'gg'+year+'.json'
    tweets = json.load(open(filename))
    
    # print human-readeable form
    print("hosts: ",end='')
    hosts = get_hosts(year)
    for host in hosts:
        print(host,end=", ")
    print()
    
    print("generated awards: ",end='')
    awards = get_awards(year)
    for award in awards:
        print(award,end=", ")
    print()
    
    presenters_dict = get_presenters(year)
    nominees_dict = get_nominees(year)
    winners_dict = get_winner(year)
    for award in award_names:
        print("\naward: ",award)
        presenters = presenters_dict[award]
        print("presenters: ",end="")
        for p in presenters:
            print(p,end=", ")

        nominees = nominees_dict[award]
        print("\nnominees: ",end="")
        for n in nominees:
            print(n,end=", ")

        print("\nwinner: ", winners_dict[award])
    
    #json format

    result = {}
    result['host'] = hosts
    award_dict={}
    for award in award_names:
        title_dict = {}
        title_dict['presenters'] = presenters_dict[award]
        title_dict['nominees'] = nominees_dict[award]
        title_dict['winner'] = winners_dict[award]
        award_dict[award] = title_dict
    result['award_data'] = award_dict
    # for key in award_dict.keys():
    #     title_dict = {}
    print(result)
    return

if __name__ == '__main__':
    main()
