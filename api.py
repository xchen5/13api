from flask import Flask, render_template
import json, urllib2

myapp = Flask(__name__)
u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=RG4u9Rp5uc2i8hVhhZ5BZeq8VAuJwduq7r2INQ6W")
j = json.loads(u.read())
#dic = {}
@myapp.route('/')
def root():
    #print j
    return render_template('base.html', stuff = j["explanation"], picture = j["url"])

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
