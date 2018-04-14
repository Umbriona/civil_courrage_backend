import urllib.request
import json

polis_url = "https://polisen.se/H4S-2018-handelser.json"

#unparsedEventsListDummy = ['"id":37919,"datetime":"2018-04-13 9:58:49 +02:00","name":"13 april 09.58, Trafikolycka, personskada, Härryda","summary":"På riksväg 40 vid Landvettermotet är det två bilister som kolliderar in i riktning mot Göteborg.","url":"https://polisen.se/aktuellt/handelser/2018/april/13/13-april-09.58-trafikolycka-personskada-harryda/","type":"Trafikolycka, personskada","location":{"name":"Härryda","gps":"57.691744,12.294416"}', '"id":37918,"datetime":"2018-04-13 9:56:41 +02:00","name":"13 april 09.56, Trafikbrott, Gävle","summary":"En man i 50-års åldern rapporteras för grov olovlig körning vid framförande av en moped.","url":"https://polisen.se/aktuellt/handelser/2018/april/13/13-april-10.53-trafikbrott-gavle/","type":"Trafikbrott","location":{"name":"Gävle","gps":"60.67488,17.141273"}']

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