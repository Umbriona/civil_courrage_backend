import urllib.request
import json

polis_url = "https://polisen.se/H4S-2018-handelser.json"

def download_event_data(polis_url):
    with urllib.request.urlopen(polis_url) as url:
        data = json.loads(url.read().decode('utf-8-sig'))
        data_str = str(data)

        url_dest = r'events'
        fx = open(url_dest, 'w')
        splitEventData = data_str.split("}}")
        listEvents = "Events"

        counter_1 = 1
        for listEvent in splitEventData:
            listEvents = listEvents + "\n" + listEvent
            counter_1 += 1

         for    

        print(listEvents)

download_event_data(polis_url)