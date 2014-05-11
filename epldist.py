import csv
import time
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3

# define locations for EPL teams since 2000-2001 season
dict = {'Blackpool': 'Blackpool',
'Liverpool': 'Liverpool',
'West Ham': 'London',
'Oldham Athletic':	'Oldham',
'Sheffield United':	'Sheffield',
'Stoke':	'Stoke-on-Trent',
'Cardiff':	'Cardiff',
'Norwich':	'Norwich',
'Nottingham Forest':	'Nottingham',
'Man City':	'Manchester',
'Swindon Town':	'Swindon',
'Fulham':	'London',
'Wigan':	'Wigan',
'Leeds':	'Leeds',
'Arsenal':	'London',
'Coventry':'Coventry',
'Blackburn':	'Blackburn',
'Portsmouth':	'Portsmouth',
'Everton':	'Liverpool',
'West Brom':	'West Bromwich',
'Sheffield Wednesday':	'Sheffield',
'Hull': 'Kingston upon Hull',
'Leicester':	'Leicester',
'Swansea':	'Swansea',
'QPR': 'London',
'Fulham': 'London',
'Reading':	'Reading, UK',
'Wolves':	'Wolverhampton',
'Barnsley':	'Barnsley',
'Man United': 'Manchester',
'Ipswich':	'Ipswich',
'Derby':	'Derby',
'Bolton':	'Bolton',
'Middlesbrough':	'Middlesbrough',
'Birmingham':	'Birmingham, UK',
'Newcastle':	'Newcastle',
'Southampton':	'Southampton',
'Crystal Palace':	'London',
'Sunderland':	'Sunderland',
'Chelsea':	'London',
'Burnley':	'Burnley',
'Charlton':	'London',
'Bradford':	'Bradford',
'Watford':	'Watford',
'Aston Villa':	'Birmingham, UK',
'Tottenham':	'London'}

geolocator = GoogleV3()
# define travel function, which takes two team names,
# finds their location in the dicitonary, then calculates the 
# distance between them
def travel(teamA, teamB):
	locA, (latA, longA) = geolocator.geocode(dict[teamA])
	locB, (latB, longB) = geolocator.geocode(dict[teamB])
	coordA = (latA, longA)
	coordB = (latB, longB)
	return vincenty(coordA, coordB).miles

vtravel = []
# take input
hteam = input("Enter the name of the home team in quotes:")
ateam = input("Enter the name of the away team in quotes:")
print "Distance: " + str(travel(hteam,ateam)) + " miles"

# uncomment for use for reading and writing csv files
# as currently written, the code reads in a csv which
# has home and away teams in two columns, and writes to a
# csv file with the two teams, and a third column for the
# distance between them
#
# with open('in_example.csv', 'rU') as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		teama = row[0]
# 		teamb = row[1]
# 		d = round(travel(teama, teamb),0)
# 		vtravel = (row + [str(d)])
# 		with open('out_example.csv', 'ab') as csvfile:
# 			writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 			writer.writerow(vtravel)
# 		print teama
# 		time.sleep(0.25)