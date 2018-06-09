import requests
import urllib2
import json
import webbrowser
# https://www.ipify.org/
ip = requests.get('https://api.ipify.org').text
print 'My public IP address is:', ip
# http://freegeoip.net/json/+ip get json file and read it
data = urllib2.urlopen("http://freegeoip.net/json/"+ip).read()
# convert json file to a slice
result = json.loads(data)
latitude = str(result['latitude'])
longitude =  str(result['longitude'])

# https://www.openstreetmap.org/#map=11/latitude/longitude
print "Location link: " + "http://www.openstreetmap.org/#map=11/%(la)s/%(lo)s" %{"la":latitude, "lo":longitude}
# open the browser with url
webbrowser.open("http://www.openstreetmap.org/#map=11/%(la)s/%(lo)s" %{"la":latitude, "lo":longitude})
