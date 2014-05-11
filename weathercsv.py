import json
import urllib2
import csv

dict = {"Washington Redskins":"Washington, DC",
"New York Jets":"East Rutherford, NJ",
"New York Giants":"East Rutherford, NJ",
"Green Bay Packers":"Green Bay, WI",
"Dallas Cowboys":"Dallas, TX",
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
"New England Patriots":"Foxboro, MA",
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
"Baltimore Colts": "Baltimore, MD",
"Tennessee Oilers": "Nashville, TN",
"Houston Oilers": "Houston, TX",
"Los Angeles Rams": "Los Angeles, CA",
"Los Angeles Raiders": "Los Angeles, CA",
"St Louis Cardinals": "St. Louis, MO",
"Phoenix Cardinals": "Tempe, AZ"}

def dformat(date):
	ind_one = date.index("/")
	mon = date[:ind_one]
	date = date[(ind_one+1):]
	if len(mon) != 2:
		mon = "0" + mon
	ind_two = date.index("/")
	day = date[:ind_two]
	date = date[(ind_two+1):]
	if len(day) != 2:
		day = "0" + day
	if int(date) < 50:
		date = "20" + date
	else:
		date = "19" + date
	return date + mon + day		
		
def lformat(team):
	place = dict[team]
	ind_one = place.index(",")
	state = place[ind_one+2:]
	city = place[:ind_one]
	if city.find(" ") != -1:
		city = city.replace(" ", "_")
	return state + "/" + city
def apicall(team, date):
	url1 = "http://api.wunderground.com/api/e0f9d0b91d8ee28c/history_" 
	url2 = "/q/" + lformat(team) + ".json"
	day = dformat(date)
	return url1 + day + url2

weather = []
with open('nflw_sn.csv', 'rU') as f:
	reader = csv.reader(f)
	for row in reader:
		datea = row[0]
		teama = row[1]
		print teama
		urlcall = apicall(teama,datea)
		j = urllib2.urlopen(urlcall)
		js= json.load(j)
		ds = js["history"]["dailysummary"]
		if not ds:
			rain = " "
			snow = " "
			inprecip = " "
		else:
			rain = js["history"]["dailysummary"][0]["rain"]
			snow = js["history"]["dailysummary"][0]["snow"]
			mmprecip = js["history"]["dailysummary"][0]["precipm"]
			mmsnow = js["history"]["dailysummary"][0]["snowfallm"]
		weather = (row + [str(rain),str(snow),str(mmprecip), str(mmsnow)])
		with open('nflwout_sn.csv', 'ab') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(weather)