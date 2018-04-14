import urllib.request
import json

polis_url = "https://polisen.se/H4S-2018-handelser.json"

def download_event_data(polis_url):
    with urllib.request.urlopen(polis_url) as url:
        data = json.loads(url.read().decode('utf-8-sig'))
        ListOfEvents = []
        for elem in data:
            event = {};
            # create event from elem
            event['id'] = elem['id']
            event['date'] = elem['datetime']
            event['type'] = elem['type']
            gps = elem['location']
            gps = gps['gps']
            gpslist = gps.split(",")
            event['longitude'] = float(gpslist[0])
            event['latitude'] = float(gpslist[1])
            event['id'] = elem['id']
            name = elem['name']
            nameparts = name.split(",")
            place = nameparts[len(nameparts) - 1]
            place = place[1:]
            event['place'] = place
            event['name'] = elem['type'] + " i " + place
            ListOfEvents.append(event)
    return ListOfEvents