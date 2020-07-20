#!/usr/bin/env python

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
     
    print(context)
    ds = {
            "aggregate": [
                        ("Country", "country", "GeoData", "countries",),
                        ("State", "state", "GeoData", "states",)
                        ]
        }
       
    context = {
        'ds': ds
    }
    
#############################################################################

if __name__ == "__main__":
    main()
