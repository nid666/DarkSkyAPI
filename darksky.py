import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim


#gets the html for the darksky page using given coordinates
def makeRequest(x, y):
    address = 'https://darksky.net/forecast/' + str(x) + ',' + str(y) + '/us12/en'
    r = requests.get(address)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


#function allows you to input an address and recieve the coordinates
#as a tuple
#ex: print(currentTemp(*(getCoords("144 Grand St, Jersey City, NJ"))))
def getCoords(address):
    geolocator = Nominatim(user_agent="Darksky API")
    location = geolocator.geocode(address)
    x = location.latitude
    y = location.longitude
    return x, y

#takes two coordinates as input and returns the current temperature in F
def currentTemp(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="summary swap"))
    return(temp[27:30])

#takes two coordinates and gives cloud coverage as a string
def getCloudCover(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="summary swap"))
    return(temp[30:-8])

#takes two coordinates and returns the real feel temperatures
def feelsLike(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="feels-like-text"))
    return(temp[30:-7])

#takes two coordinates and returns the daily low temp
def dailyLow(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="low-temp-text"))
    return(temp[28:-7])

#takes two coordinates and returns the daily high temp
def dailyHigh(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="high-temp-text"))
    return(temp[29:-7])

#Takes two coordinates and returns darksky's weather summary
def weatherSummary(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="currently__summary next swap"))
    return(temp[65:-7])

#takes two coordinates and returns the weekly weather summary
def weeklySummary(x, y):
    soup = makeRequest(x, y)
    temp = soup.find("div", id = "week", class_="center")
    temp = str(temp.find("div", class_="summary"))
    return(temp[32:-15])

#returns the wind speed in mph when given coordinates
def getWindSpeed(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="num swip wind__speed__value"))
    return(temp[42:-7])

#returns the humidity percentage when given coordinates
def getHumidity(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="num swip humidity__value"))
    return(temp[39:-7])

#returns the dew point when given coordinates
def getDewPoint(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="num dew__point__value"))
    return(temp[36:-7])

#returns the UV index when given coordinates
def getUVIndex(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="num uv__index__value"))
    return(temp[35:-7])

#returns the visibility in miles when given coordinates
def getVisiblity(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="num swip visibility__value"))
    return(temp[41:-7] + " mi")

#returns the pressure in mb when given coordinates
def getPressure(x, y):
    soup = makeRequest(x, y)
    temp = str(soup.find("span", class_="num swip pressure__value"))
    return(temp[39:-7] + " mb")

#simple test function to make sure things aren't broken
def test():
    print(getVisiblity(getPressure(*(getCoords("144 Grand st, Jersey City, NJ")))))


