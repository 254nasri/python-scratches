from geopy.geocoders import Nominatim
import time
from pprint import pprint

#create nominatim instance
instance=Nominatim(user_agent="tutorial")

#enter name of place
town=input()

#get location

location=instance.geocode(town+", Kenya").raw
pprint(location)

#incase of fail in the above process
time.sleep(1)
def getloc(address):
    time.sleep(1)
    try:
        return instance.geocode(address).raw
    except:
        return getloc(address)