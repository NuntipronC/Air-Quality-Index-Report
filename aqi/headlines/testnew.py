from flask import Flask
from flask import render_template, request
import json
from urllib.request import urlopen
import urllib.parse
import requests

app = Flask(__name__)
cri_airurl = "https://www.cmuccdc.org/api/ccdc/value/75"
all_airurl = "https://www.cmuccdc.org/api/ccdc/stations"
a = " "
@app.route("/")
def get_city():

    
    cri_air = requests.get(cri_airurl).json()
    criair = cri_air

   
    all_air = requests.get(all_airurl).json()
    allair = all_air
    
  

    return render_template("testnew.html", air=criair, data = allair,airno=a)

@app.route("/" , methods=['GET', 'POST'])
def get_air():
  

    all_air = requests.get(all_airurl).json()
    allair = all_air

    id = request.form.get("comp_select")
    air_post_url = "https://www.cmuccdc.org/api/ccdc/value/" + id
    newair = requests.get(air_post_url).json()
    test = newair
    if test == [] :
        newair_url ="https://www.cmuccdc.org/api/ccdc/station/" + id  
        no_data = requests.get(newair_url).json()  
        nodata = no_data
        null = "no data"
        print("no data")
        return render_template( "testnew.html", airno = nodata , data = allair , air=a, null=null )    
    else :
        print('data')
        newair = newair
        return render_template( "testnew.html", air = newair, data = allair ,airno=a )
    #return render_template("test.html", selectair=selectair)

if __name__ == "__main__" :
    app.run(port=5000, debug=True)