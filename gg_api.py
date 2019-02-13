'''Version 0.3'''
import hosttest
import tweetsorter
import csv
import json
import pandas as pd
from pandas.io.json import json_normalize
import config
import helpers
import winner
import awards as pres
import nominees as nom
from collections import Counter
import results

OFFICIAL_AWARDS = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
# put official awards in

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here

    #look at shuffling and randomizing for the larger datasets
    print("starting to find hosts")
    tweets = tweetsorter.loadTweets(year)
    hosts = hosttest.getHost(tweets)
    print("found hosts")
    print("hosts: ", hosts)
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    print("starting to find awards")
    awards = [" "]
    print("found awards")
    print("awards: ", awards)
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    print("starting to find nominees")
    nominees = {}
    d = helpers.loadDictionary(year)
    a = config.awardarray
    for award in a:
        nominees[award.name] = nom.findNominees(award,d[award.name])
    print("found nominees")
    print("Nominees: ")
    print(nominees)
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    print("starting to find winners")
    d = helpers.loadDictionary(year)
    a = config.awardarray
    winners = {}
    for award in a:
        winners[award.name] = winner.findWinner(award,d[award.name])
    print("found winners")
    print("winners: ")
    print(winners)
    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    print("starting to find presenters")
    d = helpers.loadDictionary(year)
    presenters = {}
    a = config.awardarray
    for award in a:
        presenters[award.name] = pres.findPresenters(award,d[award.name])
    print("found presenters")
    print("presenters: ")
    print(presenters)
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    years = ["2013","2015"]
    for year in years:
        print(year)
        print("Creating CSVs")
        helpers.createCSV(year)
        print("Finished creating CSVs")
        print("Getting rid of RTs") 
        helpers.removeRetweets(year)
        print("Finished getting rid of RTs")
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    years = ["2013"]
    for year in years:
        tweets_dictionary = helpers.loadTweetsFromJson(year)
        
        presenter_counter = Counter()
        tweet_count = len(tweets_dictionary)
        count = 0
        if year == "2013" or year == "2015":
            awards = config.awardarray
        else:
            awards = config1819.awardarray
        winners_dict = {}
        presenters_dict = {}
        for award in awards:
            winners_dict[award.name] = Counter()
            presenters_dict[award.name] = Counter()


        print (tweet_count)
        for tweet in tweets_dictionary:
            
            # HOST TWEET
            count = count + 1
            # if count % 1000 == 0:
            #     print (count)
            # print (count)
            if count == int(tweet_count/4):
                print("25% done")
            elif count == int(tweet_count/2):
                print("50% done")
            elif count == int(tweet_count*3/4):
                print("75% done")

            if count < tweet_count / 4:
                host_bigrams = hosttest.regexHosts(tweet)
                if len(host_bigrams) > 0:
                    for bg in host_bigrams:
                        presenter_counter[bg] += 1
            # AWARDS


            for award in awards:
                if tweetsorter.sortTweet(tweet,award): #is this tweet relevant for the given award
                    # add possible winners to dictionary
                    winner.findWinner(award,tweet, winners_dict[award.name], tweets_dictionary[tweet])
                    # add presenters to dictionary
                    pres.findPresenters(award, tweet, presenters_dict[award.name] ,tweets_dictionary[tweet])


                                        # WINNER
                    # winner.findWinner(award,tweet, winners_dict, tweets_dictionary[tweet])
                    # PRESENTERS

                    # NOMINEES
        for award in awards:
            print(award.name)
            print(presenters_dict[award.name].most_common(3))
        
        final_results = {}
        for a in awards:
            final_results[a.name] = results.Award()
            
            final_results[a.name].name = a.name

            winners = winners_dict[a.name].most_common(1) 
            if len(winners) > 0:
                final_results[a.name].winner = winners[0][0]
            else:
                final_results[a.name].winner = ""
            print(a.name, "     ", final_results[a.name].winner)

            # 
            presenters = presenters_dict[a.name].most_common(2) 
            if len(presenters) > 0:
                final_results[a.name].presenters = [presenters[0][0]]
                if len(presenters) > 1 and presenters[1][1] >= .5 * presenters[0][1]:
                    final_results[a.name].presenters.append(presenters[1][0])
            else:
                final_results[a.name].presenters = []
            print(a.name, "     ", final_results[a.name].presenters)
        
    
        # process winners for each award
        # process presenters for each award
        # process nominees for each award
        # human print
        # print(presenter_counter.most_common(3))
        # Find host from bigram counter
        print("Finding hosts")
        hosts = hosttest.determineHosts(presenter_counter)
        print("Hosts: ", hosts)
        print("Finished finding hosts")

    

    

    return

if __name__ == '__main__':
    main()









