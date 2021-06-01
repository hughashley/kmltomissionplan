import tkinter as tk
from tkinter import *
from lxml import etree
from pykml import parser
from os import path
import json



# create the application
#myapp = Tk()

def convertFile():
    pass

#myapp.title(".KML to QGC file format")
#myapp.geometry('400x400')
#Label(myapp, text="select input file").pack()
#Button(myapp, text = 'convert', width = 10, height = 1, command = convertFile).pack()



inputFile = "test.kml"
lines = {
    "fileType": "Plan",
    "geoFence": {
        "circles": [],
        "polygons": [],
        "version": 2
    },
    "groundStation": "QGroundControl",
    "mission": {
        "cruiseSpeed": 15,
        "firmwareType": 12,
        "hoverSpeed": 5,
        "items": [],
        "vehicleType": 2,
        "version": 2
    },
    "rallyPoints": {
        "points": [],
        "version": 2
    },
    "version": 1
}
n = 0
with open(inputFile) as fileIn:
    doc = parser.parse(fileIn)
    root = doc.getroot()
    for placemark in root.Document.Folder.Placemark:

        print(placemark.Point.coordinates)
        data = str(placemark.Point.coordinates)
        out = data.split(",")
        n += 1 
        lat = out[0]
        long = out[1]
        alt = out[2]
        missionitem = {
                "AMSLAltAboveTerrain": 500,
                "Altitude": 500,
                "AltitudeMode": 3,
                "autoContinue": True,
                "command": 16,
                "doJumpId": n,
                "frame": 3,
                "params": [
                    10,
                    0,
                    0,
                    10,
                    lat,
                    long,
                    alt
                ],
                "type": "SimpleItem"
            }
        lines['mission']['items'].append(missionitem)


print (lines)
fout = open("outputfile.plan", "w+")
jsonlines = json.dumps(lines)
fout.write(jsonlines)
fout.close()
    


# start the program
#myapp.mainloop()
