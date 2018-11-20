import urllib



url = 'https://data.boston.gov/api/3/action/datastore_search?resource_id=6ddcd912-32a0-43df-9908-63574f8c7e77&limit=5&q=title:jones'  
# fileobj = urllib.urlopen(url)
fileobj= urllib.request.urlopen(url) 
print (fileobj)