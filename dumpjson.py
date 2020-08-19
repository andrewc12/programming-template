#!/usr/bin/env python
import json

def main():
    ds = {
    "class": {
                "opts": 0,
                "name": "GeoData"
            },
    "fields": {
                "opts": 0,
                "data": [
                        ("countries", "Country[]"),
                        ("states", "State[]"),
                        ("locations", "Location[]"),
                        ("countryCount", "int"),
                        ("stateCount", "int"),
                        ("locationCount", "int")
                        ]
                },
    "methods": {
                "opts": {"makegetterssetters": True,
                        "adddefaultmethods": True},
                "data": [
                        ("readFile", "String", "void"),
                        ("writeFile", "String", "void"),
                        ("addCountry", "Country", "void"),
                        ("removeCountry", "Country", "void"),
                        ("addState", "State", "void"),
                        ("removeState", "State", "void"),
                        ("addLocation", "Location", "void"),
                        ("removeLocation", "Location", "void")
                        ]
                },
    }
                
    
    if ds['methods']['opts']['adddefaultmethods']:
        defaultmethods = [
                        ("toString", "", "String"),
                        ("equals", "Object inObj", "boolean")
                        ]
        ds['methods']['data'].extend(defaultmethods)

    
    context = {
        'ds': ds
    }
     






    ds = {
            "aggregation": [
                        ("Country", "country", "GeoData", "countries",),
                        ("State", "state", "GeoData", "states",),
                        ("Location", "location", "GeoData", "locations",)
                        ],
            "inheritance": [
                        ("Country", "country", "Area", "area",),
                        ("State", "state", "Area", "area",)
                        ],
            "composition": [
                        ("Coordinates", "coordinates", "Location", "coordinates",)
                        ]
        }
       
    context = {
        'ds': ds
    }
    
    print(json.dumps(context))
    
#############################################################################

if __name__ == "__main__":
    main()
