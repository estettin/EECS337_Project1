
class award(object):
	name = ""
	regex = ""
	awardtype = ""

award1 = award()
award1.name = "best motion picture - drama"
award1.regex = ['Best Motion Picture(.*)Drama', "Best Drama"]

award2 = award()
award2.name = "best screenplay - motion picture"
award2.regex = ["Best Screenplay"]

award3 = award()
award3.name = "best original score - motion picture"
award3.regex = ["Best Original Score"]

award4 = award()
award4.name = "best motion picture - comedy or musical"
award4.regex = ["Best Motion Picture(.*)Musical(.*)Comedy","Best Motion Picture(.*)Comedy(.*)Musical"]

award5 = award()
award5.name = "best foreign language film"
award5.regex = ["Best Foreign Language Film"]

award6 = award()
award6.name = "best director - motion picture"
award6.regex = ["Best Director(.*)Motion Picture", "Best Director"]

award7 = award()
award7.name = "best mini-series or motion picture made for television"
award7.regex = ["Best Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)","Best Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)"]

award8 = award()
award8.name = "best television series - drama"
award8.regex = ["Best(.*)Series(.*)Drama","Best Drama(.*)Series"]

award9 = award()
award9.name = "best television series - comedy or musical"
award9.regex = ["Best(.*)Series(.*)Comedy","Best(.*)Series(.*)Musical", "Best Comedy(.*)Series", "Best Musical(.*)Series"]

award10 = award()
award10.name = "best original song - motion picture"
award10.regex = ["Best Original Song"]

award11 = award()
award11.name = "best animated feature film"
award11.regex = ["Best Animated(.*)Film", "Best Animation"]

award12 = award()
award12.name = "best performance by an actor in a television series - comedy or musical"
award12.regex = ["Best(.*)Actor(.*)(TV|Television) (Series|Show)(.*)Comedy", "Best(.*)Actor(.*)(TV|Television) (Series|Show)(.*)Musical", "Best(.*)Actor(.*)Comedy(.*)(TV|Television) (Series|Show)", "Best(.*)Actor(.*)Musical(.*)(TV|Television) (Series|Show)"]

award13 = award()
award13.name = "best performance by an actor in a television series - drama"
award13.regex = ["Best(.*)Actor(.*)(TV|Television) (Series|Show)(.*)Drama", "Best(.*)Actor(.*)Drama(.*)(TV|Television) (Series|Show)"]

award14 = award()
award14.name = "best performance by an actor in a motion picture - drama"
award14.regex = ["Best Actor(.*)Motion Picture(.*)Drama", "Best Actor(.*)Drama Motion Picture","Best Actor(.*)Drama Movie", "Best Performance By An Actor(.*)Motion Picture(.*)Drama","Best Performance By An Actor(.*)Drama Motion Picture"]

award15 = award()
award15.name = "best performance by an actor in a motion picture - comedy or musical"
award15.regex = ["Best Actor(.*)Motion Picture(.*)Comedy", "Best Actor(.*)Comedy(.*)Motion Picture","Best Actor(.*)Musical(.*)Motion Picture", "Best Actor(.*)Musical Movie","Best Actor(.*)Comedy Movie", "Best Performance By An Actor(.*)Motion Picture(.*)Comedy","Best Performance By An Actor(.*)Motion Picture(.*)Musical","Best Performance By An Actor(.*)(Comedy|Musical) Motion Picture"]

award16 = award()
award16.name = "best performance by an actor in a mini-series or motion picture made for television"
award16.regex = ["Best Actor(.*)Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actor(.*)Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actor(.*)Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)"]

award17 = award()
award17.name = "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television"
award17.regex = ["Best Supporting Actor(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Supporting Role(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actor(.*)Series", "Best Supporting Actor(.*)Mini", "Best Supporting Actor(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actor(.*)(TV|Television) (Movie|Film|Motion Picture)"]

award18 = award()
award18.name = "best performance by an actor in a supporting role in a motion picture"
award18.regex = ["Best Supporting Actor in a Motion Picture", "Best Performance by an Actor in a Supporting Role in a Motion Picture"]




award19 = award()
award19.name = "best performance by an actress in a television series - comedy or musical"
award19.regex = ["Best(.*)Actress(.*)(TV|Television) (Series|Show)(.*)Comedy", "Best(.*)Actress(.*)(TV|Television) (Series|Show)(.*)Musical", "Best(.*)Actress(.*)Comedy(.*)(TV|Television) (Series|Show)", "Best(.*)Actress(.*)Musical(.*)(TV|Television) (Series|Show)"]

award20 = award()
award20.name = "best performance by an actress in a television series - drama"
award20.regex = ["Best(.*)Actress(.*)(TV|Television) (Series|Show)(.*)Drama", "Best(.*)Actress(.*)Drama(.*)(TV|Television) (Series|Show)"]

award21 = award()
award21.name = "best performance by an actress in a motion picture - drama"
award21.regex = ["Best Actress(.*)Motion Picture(.*)Drama", "Best Actress(.*)Drama Motion Picture","Best Actress(.*)Drama Movie", "Best Performance By An Actress(.*)Motion Picture(.*)Drama","Best Performance By An Actress(.*)Drama Motion Picture"]

award22 = award()
award22.name = "best performance by an actress in a motion picture - comedy or musical"
award22.regex = ["Best Actress(.*)Motion Picture(.*)Comedy", "Best Actress(.*)Comedy(.*)Motion Picture","Best Actress(.*)Musical(.*)Motion Picture", "Best Actress(.*)Musical Movie","Best Actress(.*)Comedy Movie", "Best Performance By An Actress(.*)Motion Picture(.*)Comedy","Best Performance By An Actress(.*)Motion Picture(.*)Musical","Best Performance By An Actress(.*)(Comedy|Musical) Motion Picture"]

award23 = award()
award23.name = "best performance by an actress in a mini-series or motion picture made for television"
award23.regex = ["Best Actress(.*)Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actress(.*)Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actress(.*)Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)"]

award24 = award()
award24.name = "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television"
award24.regex = ["Best Supporting Actress(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Supporting Role(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actress(.*)Series", "Best Supporting Actress(.*)Mini", "Best Supporting Actress(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actress(.*)(TV|Television) (Movie|Film|Motion Picture)"]

award25 = award()
award25.name = "best performance by an actress in a supporting role in a motion picture"
award25.regex = ["Best Supporting Actress in a Motion Picture", "Best Performance by an Actress in a Supporting Role in a Motion Picture"]


"""


"best performance by an actor in a television series - comedy or musical"
"best performance by an actor in a television series - drama"
"best performance by an actor in a motion picture - drama"
"best performance by an actor in a motion picture - comedy or musical"
"best performance by an actor in a mini-series or motion picture made for television"
"best performance by an actor in a supporting role in a series, mini-series or motion picture made for television"
"best performance by an actor in a supporting role in a motion picture"

"""

awardarray = [award1,award2,award3,award4,award5, award6,award7, award8, award9, award10, award11, award12, award13, award14,award15,award16,award17,award18,award19,award20,award21,award22,award23,award24,award25]




