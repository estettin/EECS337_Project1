import json
from pprint import pprint
class Award(object):
	name = ""
	presenters = []
	nominees = []
	winner = ""

class Results(object):
	host = []
	awards = []

def humanPrint(r):
	if len(r.host) < 2:
		print "Host: " + r.host[0]
	else:
		print "Host: " + ', '.join(r.host)
	print ""

	for a in r.awards:
		print "Award: " + a.name 
		if len(a.presenters) < 2:
			print "Presenter: " + a.presenters[0]
		else:
			print "Presenters: " + ', '.join(a.presenters)
		print "Nominees: " + ', '.join(a.nominees)
		print "Winner: " + a.winner
		print ""

def jsonPrint(r):
	if len(r.host) < 2:
		hoststring = r.host[0]
	else:
		hoststring = ', '.join(r.host)
	result = {
		"Host": hoststring
	}
	for a in r.awards:
		if len(a.presenters) < 2:
			presentersString = a.presenters[0]
		else:
			presentersString = ', '.join(a.presenters)
		if len(a.nominees) < 2:
			nomineesString = a.nominees[0]
		else:
			nomineesString = ', '.join(a.nominees)
		temp = {}
		temp["Presenters"] = presentersString
		temp["Nominees"] = nomineesString
		temp["Winner"] = a.winner
		result[a.name] = temp
	return json.dumps(result)


r = Results();
r.host = ["Jake Reifer", "Eshan Tarneja"]
award1 = Award();
award1.name = "Best Motion Picture - Drama"
award1.presenters = ["Barbara Streisand"]
award1.nominees = ["Three Billboards Outside Ebbing, Missouri", "Call Me by Your Name", "Dunkirk", "The Post", "The Shape of Water"]
award1.winner = "Three Billboards Outside Ebbing, Missouri"
award2 = Award();
award2.name = "Best Motion Picture - Musical or Comedy"
award2.presenters = ["Alicia Vikander", "Michael Keaton"]
award2.nominees = ["Lady Bird", "The Disaster Artist", "Get Out", "The Greatest Showman", "I, Tonya"]
award2.winner = "Lady Bird"
r.awards = [award1, award2]

humanPrint(r)
print ""
print ""
print ""
print jsonPrint(r)






