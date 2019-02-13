# EECS337_Project1

Elana Stettin, Jake Reifer, Kevin Chan, Eshan Tarneja

TO SET UP:
In the command line:
`pip3 install -r requirements.txt` on Mac or device running Python 2.7 by default or `pip install -r requirements.txt` on device running Python 3 by default
`python3 -m spacy download en_core_web_sm`
*Instructions have paths specifically for Macs*
`sudo python3.6 -m nltk.downloader -d /usr/local/share/nltk_data all`
if this give you an ssl error, run 
`bash /Applications/Python 3.6/Install Certificates.command`

Non-Mac running Python 3 by default
*Perform inside a python3 shell*:
`~$: Python
>> 
```>> import nltk
>> nltk.download()``` in python3 shell open interactive installer
Select all-nltk and download

## References - Larry said to list repos that we looked at for references. We looked at these two github repos to look for ideas about what regex searches to use for our code. 
- https://github.com/brownrout/EECS-337-Golden-Globes
- https://github.com/olivergoodman/goldenglobes
