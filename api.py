from flask import Flask, render_template
import json, urllib2

myapp = Flask(__name__)
u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=RG4u9Rp5uc2i8hVhhZ5BZeq8VAuJwduq7r2INQ6W")
j = json.loads(u.read())


@myapp.route('/')
def root():
    #print j
    fdaLink = "https://api.fda.gov/drug/event.json"
    fdaLink += "?search=receivedate:[20160101+TO+20161231]+AND+patient.drug.medicinalproduct:caffeine"
    fda = urllib2.urlopen(fdaLink)
    fdaJSON = json.loads(fda.read())
    return render_template('base.html', stuff = j["explanation"], picture = j["url"], fdaAPI = "# FDA cases related to caffeine in 2016: " + str(fdaJSON["meta"]["results"]["total"]))

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
