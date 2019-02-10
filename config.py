
class award(object):
	name = ""
	regex = []
	must = []
	mustnot = []
	ors = []
	awardtype = ""

award1 = award()
award1.name = "best motion picture - drama"
award1.regex = ['Best Motion Picture(.*)Drama', "Best Drama"]
award1.must = ["best", "drama"]
award1.mustnot = ["actor", "actress", "television", "tv", "series"]
award1.ors = []
award1.awardtype = "movie"

award2 = award()
award2.name = "best screenplay - motion picture"
award2.regex = ["Best Screenplay"]
award2.must = ["best", "screenplay"]
award2.mustnot = ["television", "tv", "series"]
award2.ors = []
award2.awardtype = "movie"

award3 = award()
award3.name = "best original score - motion picture"
award3.regex = ["Best Original Score"]
award3.must = ["best", "score"]
award3.mustnot = ["television", "tv", "series"]
award3.ors = []
award3.awardtype = "movie"

award4 = award()
award4.name = "best motion picture - comedy or musical"
award4.regex = ["Best Motion Picture(.*)Musical(.*)Comedy","Best Motion Picture(.*)Comedy(.*)Musical"]
award4.must = ["best", "picture"]
award4.mustnot = ["actor", "actress", "television", "tv", "series"]
award4.ors = ["comedy", "musical"]
award4.awardtype = "movie"

award5 = award()
award5.name = "best foreign language film"
award5.regex = ["Best Foreign Language Film"]
award5.must = []
award5.mustnot = ["actor", "actress", "television", "tv", "series"]
award5.ors = ["best foreign film", "best foreign language film"]
award5.awardtype = "movie"

award6 = award()
award6.name = "best director - motion picture"
award6.regex = ["Best Director(.*)Motion Picture", "Best Director"]
award6.must = ["best director"]
award6.mustnot = ["actor", "actress", "television", "tv", "series"]
award6.ors = []
award6.awardtype = "person"

award7 = award()
award7.name = "best mini-series or motion picture made for television"
award7.regex = ["Best Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)","Best Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)"]
award7.must = []
award7.mustnot = ["actor", "actress"]
award7.ors = ["best miniseries", "best mini-series", "best mini series", "motion picture for tv", "motion picture for television", "motion picture made for tv", "motion picture made for television"]
award7.awardtype = "movie"

award8 = award()
award8.name = "best television series - drama"
award8.regex = ["Best(.*)Series(.*)Drama","Best Drama(.*)Series"]
award8.must = ["best", "drama"]
award8.mustnot = ["actor", "actress", "picture"]
award8.ors = ["tv","television"]
award8.awardtype = "movie"

award9 = award()
award9.name = "best television series - comedy or musical"
award9.regex = ["Best(.*)Series(.*)Comedy","Best(.*)Series(.*)Musical", "Best Comedy(.*)Series", "Best Musical(.*)Series"]
award9.must = ["best"]
award9.mustnot = ["actor", "actress", "picture", "drama"]
award9.ors = ["comedy series", "musical series", "comedy tv series", "musical tv series", "comedy television series", "musical television series", "comedy tv show", "musical tv show", "comedy television show", "musical television show"]
award9.awardtype = "movie"


award10 = award()
award10.name = "best original song - motion picture"
award10.regex = ["Best Original Song"]
award10.must = []
award10.mustnot = []
award10.ors = ["best original song","best song"]
award10.awardtype = "movie"

award11 = award()
award11.name = "best animated feature film"
award11.regex = ["Best Animated(.*)Film", "Best Animation"]
award11.must = ["best"]
award11.mustnot = ["actor", "actress", "picture"]
award11.ors = ["animation","animated film", "animated feature film"]
award11.awardtype = "movie"

award12 = award()
award12.name = "best performance by an actor in a television series - comedy or musical"
award12.regex = ["Best(.*)Actor(.*)(TV|Television) (Series|Show)(.*)Comedy", "Best(.*)Actor(.*)(TV|Television) (Series|Show)(.*)Musical", "Best(.*)Actor(.*)Comedy(.*)(TV|Television) (Series|Show)", "Best(.*)Actor(.*)Musical(.*)(TV|Television) (Series|Show)"]
award12.must = ["best", "actor"]
award12.mustnot = ["actress", "movie", "supporting", "drama"]
award12.ors = ["television", "tv"]
award12.awardtype = "person"

award13 = award()
award13.name = "best performance by an actor in a television series - drama"
award13.regex = ["Best(.*)Actor(.*)(TV|Television) (Series|Show)(.*)Drama", "Best(.*)Actor(.*)Drama(.*)(TV|Television) (Series|Show)"]
award13.must = ["best", "actor"]
award13.mustnot = ["actress", "movie", "supporting", "comedy", "musical"]
award13.ors = ["television", "tv"]
award13.awardtype = "person"


award14 = award()
award14.name = "best performance by an actor in a motion picture - drama"
award14.regex = ["Best Actor(.*)Motion Picture(.*)Drama", "Best Actor(.*)Drama Motion Picture","Best Actor(.*)Drama Movie", "Best Performance By An Actor(.*)Motion Picture(.*)Drama","Best Performance By An Actor(.*)Drama Motion Picture"]
award14.must = ["best", "actor"]
award14.mustnot = ["actress", "supporting", "comedy", "musical"]
award14.ors = ["movie", "motion-picture", "motion picture", "film"]
award14.awardtype = "person"

award15 = award()
award15.name = "best performance by an actor in a motion picture - comedy or musical"
award15.regex = ["Best Actor(.*)Motion Picture(.*)Comedy", "Best Actor(.*)Comedy(.*)Motion Picture","Best Actor(.*)Musical(.*)Motion Picture", "Best Actor(.*)Musical Movie","Best Actor(.*)Comedy Movie", "Best Performance By An Actor(.*)Motion Picture(.*)Comedy","Best Performance By An Actor(.*)Motion Picture(.*)Musical","Best Performance By An Actor(.*)(Comedy|Musical) Motion Picture"]
award15.must = ["best", "actor"]
award15.mustnot = ["actress", "supporting", "drama"]
award15.ors = ["movie", "motion-picture", "motion picture", "film", "comedy", "musical"]
award15.awardtype = "person"

award16 = award()
award16.name = "best performance by an actor in a mini-series or motion picture made for television"
award16.regex = ["Best Actor(.*)Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actor(.*)Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actor(.*)Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)"]
award16.must = ["best", "actor"]
award16.mustnot = ["actress", "supporting"]
award16.ors = ["motion picture made for television","motion picture made for tv", "motion-picture for television","motion-picture for tv", "miniseries", "mini-series", "mini series"]
award16.awardtype = "person"


award17 = award()
award17.name = "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television"
award17.regex = ["Best Supporting Actor(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actor in a Supporting Role(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actor(.*)Series", "Best Supporting Actor(.*)Mini", "Best Supporting Actor(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actor(.*)(TV|Television) (Movie|Film|Motion Picture)"]
award17.must = ["best", "actor", "supporting"]
award17.mustnot = ["actress"]
award17.ors = ["motion picture made for television","motion picture made for tv", "motion-picture for television","motion-picture for tv", "miniseries", "mini-series", "mini series", "series"]
award17.awardtype = "person"


award18 = award()
award18.name = "best performance by an actor in a supporting role in a motion picture"
award18.regex = ["Best Supporting Actor in a Motion Picture", "Best Performance by an Actor in a Supporting Role in a Motion Picture"]
award18.must = ["best", "actor", "supporting"]
award18.mustnot = ["television", "tv", "actress"]
award18.ors = []
award18.awardtype = "person"


award19 = award()
award19.name = "best performance by an actress in a television series - comedy or musical"
award19.regex = ["Best(.*)Actress(.*)(TV|Television) (Series|Show)(.*)Comedy", "Best(.*)Actress(.*)(TV|Television) (Series|Show)(.*)Musical", "Best(.*)Actress(.*)Comedy(.*)(TV|Television) (Series|Show)", "Best(.*)Actress(.*)Musical(.*)(TV|Television) (Series|Show)"]
award19.must = ["best", "actress"]
award19.mustnot = ["actor", "movie", "supporting", "drama"]
award19.ors = ["television", "tv"]
award19.awardtype = "person"

award20 = award()
award20.name = "best performance by an actress in a television series - drama"
award20.regex = ["Best(.*)Actress(.*)(TV|Television) (Series|Show)(.*)Drama", "Best(.*)Actress(.*)Drama(.*)(TV|Television) (Series|Show)"]
award20.must = ["best", "actress"]
award20.mustnot = ["actor", "movie", "supporting", "comedy", "musical"]
award20.ors = ["television", "tv"]
award20.awardtype = "person"

award21 = award()
award21.name = "best performance by an actress in a motion picture - drama"
award21.regex = ["Best Actress(.*)Motion Picture(.*)Drama", "Best Actress(.*)Drama Motion Picture","Best Actress(.*)Drama Movie", "Best Performance By An Actress(.*)Motion Picture(.*)Drama","Best Performance By An Actress(.*)Drama Motion Picture"]
award21.must = ["best", "actress"]
award21.mustnot = ["actor", "supporting", "comedy", "musical"]
award21.ors = ["movie", "motion-picture", "motion picture", "film"]
award21.awardtype = "person"

award22 = award()
award22.name = "best performance by an actress in a motion picture - comedy or musical"
award22.regex = ["Best Actress(.*)Motion Picture(.*)Comedy", "Best Actress(.*)Comedy(.*)Motion Picture","Best Actress(.*)Musical(.*)Motion Picture", "Best Actress(.*)Musical Movie","Best Actress(.*)Comedy Movie", "Best Performance By An Actress(.*)Motion Picture(.*)Comedy","Best Performance By An Actress(.*)Motion Picture(.*)Musical","Best Performance By An Actress(.*)(Comedy|Musical) Motion Picture"]
award22.must = ["best", "actress"]
award22.mustnot = ["actor", "supporting", "drama"]
award22.ors = ["movie", "motion-picture", "motion picture", "film", "comedy", "musical"]
award22.awardtype = "person"

award23 = award()
award23.name = "best performance by an actress in a mini-series or motion picture made for television"
award23.regex = ["Best Actress(.*)Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actress(.*)Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Actress(.*)Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Mini-Series(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Miniseries(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Mini Series(.*)Motion Picture(.*)(for|made for) (TV|Television)"]
award23.must = ["best", "actress"]
award23.mustnot = ["actor", "supporting"]
award23.ors = ["motion picture made for television","motion picture made for tv", "motion-picture for television","motion-picture for tv", "miniseries", "mini-series", "mini series"]
award23.awardtype = "person"


award24 = award()
award24.name = "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television"
award24.regex = ["Best Supporting Actress(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Performance by an Actress in a Supporting Role(.*)Series(.*)Mini(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actress(.*)Series", "Best Supporting Actress(.*)Mini", "Best Supporting Actress(.*)Motion Picture(.*)(for|made for) (TV|Television)", "Best Supporting Actress(.*)(TV|Television) (Movie|Film|Motion Picture)"]
award24.must = ["best", "actress", "supporting"]
award24.mustnot = ["actor"]
award24.ors = ["motion picture made for television","motion picture made for tv", "motion-picture for television","motion-picture for tv", "miniseries", "mini-series", "mini series", "series"]
award24.awardtype = "person"

award25 = award()
award25.name = "best performance by an actress in a supporting role in a motion picture"
award25.regex = ["Best Supporting Actress in a Motion Picture", "Best Performance by an Actress in a Supporting Role in a Motion Picture"]
award25.must = ["best", "actress", "supporting"]
award25.mustnot = ["television", "tv", "actor"]
award25.ors = []
award25.awardtype = "person"

award26 = award()
award26.name = "cecil b. demille award"
award26.regex = ["Cecil(.*)de(.*)award"]
award26.must = []
award26.mustnot = ["best"]
award26.ors = ["cecil b demille award","cecil b. demille award","cecil b. de mille award", "cecil b de mille award"]
award26.awardtype = "person"



awardarray = [award1,award2,award3,award4,award5, award6,award7, award8, award9, award10, award11, award12, award13, award14,award15,award16,award17,award18,award19,award20,award21,award22,award23,award24,award25]




