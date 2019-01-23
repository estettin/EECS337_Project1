# EECS337_Project1

Elana Stettin, Jake Reifer, Kevin Chan, Eshan Tarneja

Code Due: 11:59pm Sunday February 17 through Canvas.

Presentations: Meetings to present your project will take place on Feb 18-19 and as needed on the 20th (Monday, Tuesday and Wednesday). You'll sign up for a meeting time in the last week before the project is due. Meeting location is TBA.

Project Deliverables:

- All code must be in Python 2.7. You can use any Python package or NLP toolkit.
- You must use a publicly accessible repository such as Github, and commit code regularly. When pair programming, note in the commit message those who were present and involved. We use these logs to verify complaints about AWOL teammates, and to avoid penalizing the entire group for one student’s violation of academic integrity. We don’t look at the commits unless there’s something really wrong with the code, or there’s a complaint.
- Please use the Python standard for imports described here: https://www.python.org/dev/peps/pep-0008/#imports (Links to an external site.)Links to an external site.
Bundle all your code together, your submission will be a .zip file on canvas.
- If you use a DB, it must be Mongo DB, and you must provide the code you used to populate your database.
- Your code must be runnable by the TAs: Include a readme.txt file with instructions on what file(s) to run, what packages to download / where to find them, how to install them, etc and any other necessary information. The readme should also include the address for your github repository.
- Your code must run in a reasonable amount of time. Your grade will likely be impacted if this is greater than 5 minutes.
- Your code cannot rely on a single Twitter user for correct answers. Particularly, the official Golden Globes account.
 

## Minimum Requirements:

Fulfilling only the minimum requirements puts your group on track for a B

A project must do a reasonable job identifying each of these components.
- Host(s) (for the entire ceremony)
- Award Names
- Presenters, mapped to awards*
- Nominees, mapped to awards*
- Winners, mapped to awards*
* These will default to using a hardcoded list of the awards to avoid penalizing you for cascading error.

It is OK not to have 100% accuracy on some of these components. It's very rare for any group not to have some error, especially with nominees. Even getting just half of the nominees for a given award is quite good performance.

Additional Goals:

To get better than a B, you must do exceptionally well on the minimum requirements, or complete one or more additional goals. Some examples of additional goals:
- Red carpet – For example, determine who was best dressed, worst dressed, most discussed, most controversial, or perhaps find pictures of the best and worst dressed, etc.
- Humor – For example, what were the best jokes of the night, and who said them?
- Parties – For example, what parties were people talking about the most? Were people saying good things, or bad things?
- Sentiment – What were the most common sentiments used with respect to the winners, hosts, presenters, acts, and/or nominees?
- Acts – What were the acts, when did they happen, and/or what did people have to say about them?
- Your choice – If you have a cool idea, suggest it to the TA! Ideas that will require the application of NLP and semantic information are more likely to be approved.
- Typical performance on the minimum requirements, plus a well-done additional goal, is likely to earn an A- or better.

Required Output Format:
You are required to output your results in two different formats.
- A human-readable format. This is where your additional goals output happens. For example:
-- Host: Seth Meyers
-- Award: Best Motion Picture - Drama
-- Presenters: Barbara Streisand
-- Nominees: “Three Billboards Outside Ebbing, Missouri”, "Call Me by Your Name", "Dunkirk", "The Post", "The Shape of Water"
-- Winner: “Three Billboards Outside Ebbing, Missouri”
-- Best Dressed: Jane Doe
-- Worst Dressed: John Doe
-- Most Controversially Dressed: John Smith

A json format compatible with the autograder; this is only containing the information for the minimum tasks. For example:
```{
"Host" : "Seth Meyers",
"Best Motion Picture - Drama" : {
"Presenters" : ["Barbra Streisand"],
"Nominees" : ["Three Billboards Outside Ebbing, Missouri", "Call Me by Your Name", "Dunkirk", "The Post", "The Shape of Water"],
"Winner" : "Three Billboards Outside Ebbing, Missouri"
},
"Best Motion Picture - Musical or Comedy" : {
"Presenters" : ["Alicia Vikander", "Michael Keaton"],
"Nominees" : ["Lady Bird", "The Disaster Artist", "Get Out", "The Greatest Showman", "I, Tonya"],
"Winner" : "Lady Bird"
}```

 

The Data:
[{u'id': 554402424728072192, u'text': u'just had to scramble to find a golden globes stream for my brother. :D', u'user': {u'id': 19904553, u'screen_name': u'baumbaTz'}, u'timestamp_ms': u'1421014813011'}, {"text": "What?!? https://t.co/NSPtGtbCvO", "id_str": "950142397194821632"}, ...]

Tweets for 2015 were collected if they matched the query
track=['gg','golden globes', 'golden globe', 'goldenglobe','goldenglobes','gg2015','gg15','goldenglobe2015','goldenglobe15','goldenglobes2015','goldenglobes15','redcarpet','red carpet','redcarpet15','redcarpet2015','nominees','nominee','globesparty','globesparties' ]

2013 used fewer keywords, as did 2018 and 2019. You will be graded on at least one year you have not seen.

See twitter api "track" parameter (Links to an external site.)Links to an external site. for details.
Tweets that are retweets have a text field that begins "RT"
Unicode characters (such as "\ud83d") are usually emoji or non-English letters. You can decode these or just skip / prune them.
 

The Autograder:

The autograder is your way of benchmarking your progress as you work on improving accuracy.

The master repository is at [https://github.com/milara/gg-project-master] (Links to an external site.)Links to an external site., and it contains:
A copy of the autograder program, which will assess how well you did on the basic tasks. It has undergone some changes as the project format has changed, so please report bugs early and often so that I can get it fixed ASAP.
A template for the API the autograder uses, saved as gg_api.py. Be sure to read the doc strings and ask the TA if you have any questions about how to use this file.
JSON files with the correct answers for the minimum tasks for both 2013 and 2015; these are used by the autograder. DO NOT read this into memory in your own code. Doing so is grounds for an automatic zero.
