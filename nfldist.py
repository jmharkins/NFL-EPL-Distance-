import csv
import time
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3

# define locations for NFL teams for 1978-2012 seasons
dict = {"Washington Redskins":"Landover, MD",
"New York Jets":"East Rutherford, NJ",
"New York Giants":"East Rutherford, NJ",
"Green Bay Packers":"Green Bay, WI",
"Dallas Cowboys":"Arlington, TX",
"Kansas City Chiefs":"Kansas City, MO",
"Denver Broncos":"Denver, CO",
"Miami Dolphins":"Miami Gardens, FL",
"Carolina Panthers":"Charlotte, NC",
"New Orleans Saints":"New Orleans, LA",
"Cleveland Browns":"Cleveland, OH",
"Buffalo Bills":"Orchard Park, NY",
"Atlanta Falcons":"Atlanta, GA",
"Houston Texans":"Houston, TX",
"Baltimore Ravens":"Baltimore, MD",
"San Diego Chargers":"San Diego, CA",
"Tennessee Titans":"Nashville, TN",
"New England Patriots":"Foxborough, MA",
"Philadelphia Eagles":"Philadelphia, PA",
"San Francisco 49ers":"Santa Clara, CA",
"Jacksonville Jaguars":"Jacksonville, FL",
"Seattle Seahawks":"Seattle, WA",
"St Louis Rams":"St. Louis, MO",
"Tampa Bay Buccaneers":"Tampa, FL",
"Cincinnati Bengals":"Cincinnati, OH",
"Pittsburgh Steelers":"Pittsburgh, PA",
"Detroit Lions":"Detroit, MI",
"Arizona Cardinals":"Glendale, AZ",
"Indianapolis Colts":"Indianapolis, IN",
"Chicago Bears":"Chicago, IL",
"Oakland Raiders":"Oakland, CA",
"Minnesota Vikings":"Minneapolis, MN",
"Baltimore Colts": "Baltimore,MD",
"Tennessee Oilers": "Nashville, TN",
"Houston Oilers": "Houston, TX",
"Los Angeles Rams": "Los Angeles, CA",
"Los Angeles Raiders": "Los Angeles,CA",
"St Louis Cardinals": "St. Louis, MO",
"Phoenix Cardinals": "Tempe, AZ"}

geolocator = GoogleV3()
#
# define travel function, which takes two team names,
# finds their location in the dicitonary, then calculates the 
# distance between them
#
def travel(teamA, teamB):
	locA, (latA, longA) = geolocator.geocode(dict[teamA])
	locB, (latB, longB) = geolocator.geocode(dict[teamB])
	coordA = (latA, longA)
	coordB = (latB, longB)
	return vincenty(coordA, coordB).miles

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
# vtravel = []
# with open('in_example.csv', 'rU') as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		teama = row[0]
# 		teamb = row[1]
# 		d = round(travel(teama, teamb),0)
# 		vtravel = (row + [str(d)])
# 		with open('out_example', 'ab') as csvfile:
# 			writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 			writer.writerow(vtravel)
# 		print teama
# 		time.sleep(0.5)