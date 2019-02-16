'''Version 0.3'''
import hosttest
import tweetsorter
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
import findawards
import sentiment 
import redcarpet

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

# put official awards in

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here

    #look at shuffling and randomizing for the larger datasets
    values = helpers.loadResultJson(year, "hosts")
    hosts = values["hosts"]
    return hosts

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    values = helpers.loadResultJson(year, "awards")
    awards = values["awards"]
    return awards

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    nominees = helpers.loadResultJson(year, "nominees")
    return nominees

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    winners = helpers.loadResultJson(year, "winners")
    return winners

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    presenters = helpers.loadResultJson(year, "presenters")
    return presenters

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    years = ["2013","2015", "2018", "2019"]
    for year in years:
        try:
            print(year)
            print("Creating CSVs")
            helpers.createCSV(year)
            print("Finished creating CSVs")
            print("Getting rid of RTs") 
            helpers.removeRetweets(year)
            print("Finished getting rid of RTs")
        except:
            print("Could not find data for year %s" % year)
    print("Pre-ceremony processing complete.")
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
    pre_ceremony()
    years = ["2013"]

    for year in years:
        tweets_dictionary = helpers.loadTweetsFromJson(year)
        hosttweets = {}
        presenter_counter = Counter()
        tweet_count = len(tweets_dictionary)
        count = 0
        if year == "2013" or year == "2015":
            awards = config.awardarray
        else:
            awards = config1819.awardarray
        winners_dict = {}
        presenters_dict = {}
        nominees_dict = {}
        phrases = {}
        best_dressed_counter = Counter()
        worst_dressed_counter = Counter()
        for award in awards:
            winners_dict[award.name] = Counter()
            presenters_dict[award.name] = Counter()
            nominees_dict[award.name] = Counter()

        print ("Number of Unique Tweets :", tweet_count)
        print("Progress:")
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
                host_bigrams = hosttest.regexHosts(tweet, hosttweets)
                if len(host_bigrams) > 0:
                    for bg in host_bigrams:
                        presenter_counter[bg] += 1

            redcarpet.getRedCarpetInfo(tweet, best_dressed_counter, worst_dressed_counter, tweets_dictionary[tweet])    


            # AWARDS
            findawards.PopulatePhrasesforAwards(tweet,tweets_dictionary[tweet],phrases)

            for award in awards:
                if tweetsorter.sortTweet(tweet,award): #is this tweet relevant for the given award
                    # add possible winners to dictionary
                    winner.findWinner(award,tweet, winners_dict[award.name], tweets_dictionary[tweet])
                    # add presenters to dictionary
                    pres.findPresenters(award, tweet, presenters_dict[award.name], tweets_dictionary[tweet])
                    # add nominees to dictionary
                    nom.findNominees(award, tweet, nominees_dict[award.name], tweets_dictionary[tweet])

                                        # WINNER
                    # winner.findWinner(award,tweet, winners_dict, tweets_dictionary[tweet])
                    # PRESENTERS

                    # NOMINEES
        # for award in awards:
            # print(award.name)
            # print(nominees_dict[award.name].most_common(10))
        print(" ")
        print("Done looking at tweets. Starting to analyze results")
        print("Year: ", year)
        print(" ")
        final_results = {}
        hosts = hosttest.determineHosts(presenter_counter)
        host_string = ""
        for h in hosts:
            host_string = host_string + h + ", "
        print("Host(s): ", host_string)
        print("")
        hostJSON = {}
        hostJSON["hosts"] = hosts

        for a in awards:
            print("Award: ", a.name.title())
            final_results[a.name] = results.Award()
            final_results[a.name].name = a.name

            final_results[a.name].presenters = helpers.finalizePresenters(presenters_dict[a.name]) 
            presenters_string = ""
            for p in final_results[a.name].presenters:
                presenters_string = presenters_string + p + ", "
            print("Presenters: ", presenters_string)

            winners = winners_dict[a.name].most_common(1)
            if len(winners) > 0:
                final_results[a.name].winner = winners[0][0]
            else:
                final_results[a.name].winner = ""
            winner_string = ""
            if a.awardtype == "movie":
                winner_string = '"' + final_results[a.name].winner + '"'
            else:
                winner_string = final_results[a.name].winner
            print("Winner: ", winner_string)
            
            
            final_results[a.name].nominees = helpers.finalizeNominees(nominees_dict[a.name], final_results[a.name].winner, a, year)
            nominees_string = ""
            if a.awardtype == "movie":
                for n in final_results[a.name].nominees:
                    nominees_string = '"' + n + '", '
            else:
                for n in final_results[a.name].nominees:
                    nominees_string = n + ", "
            print("Nominees: ", nominees_string)
            print(" ")

        
        #awards
        awardsJSON = {}
        awardsJSON["awards"] = findawards.PostProcessFindAwards(phrases)
        print("Award Names:")
        for a in awardsJSON["awards"]:
            print("    ", a)
        print(" ")
        #dumps
        winnerJSON = {}
        presentersJSON = {}
        nomineesJSON = {}
        
        for a in awards:
            winnerJSON[a.name] = final_results[a.name].winner
            presentersJSON[a.name] = final_results[a.name].presenters
            nomineesJSON[a.name] = final_results[a.name].nominees

        with open('results/' + year + "/" + "winners.json", 'w') as fp:
            json.dump(winnerJSON, fp)
        with open('results/' + year + "/" + "presenters.json", 'w') as fp:
            json.dump(presentersJSON, fp)
        with open('results/' + year + "/" + "nominees.json", 'w') as fp:
            json.dump(nomineesJSON, fp)
        with open('results/' + year + "/" + "hosts.json", 'w') as fp:
            json.dump(hostJSON, fp)
        with open('results/' + year + "/" + "awards.json", 'w') as fp:
            json.dump(awardsJSON, fp)

        host_sentiment = {}
        print("Host Sentiment:")
        for host in hosts:
            host_sentiment[host] = sentiment.findSentiment(hosttweets[host])
            print("     ", host, ": ", host_sentiment[host])
        print("")

        best_dressed = best_dressed_counter.most_common(1)
        if len(best_dressed) > 0:
            best_dressed = best_dressed[0][0]
        else:
            best_dressed = ""
        worst_dressed = worst_dressed_counter.most_common(1)
        if len(worst_dressed) > 0:
            worst_dressed = worst_dressed[0][0]
        else:
            worst_dressed = ""
        
        print("Red Carpet Info")
        print("     Best Dressed: ", best_dressed)
        print("     Worst Dressed: ", worst_dressed)
        print("")
    return

if __name__ == '__main__':
    main()









