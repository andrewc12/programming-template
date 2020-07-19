#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False,
    extensions=['jinja2.ext.do'])


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_class_java():
    fname = "outputclass.java"
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
    print(ds)
    if ds['methods']['opts']['adddefaultmethods']:
        defaultmethods = [
                        ("toString", "", "String"),
                        ("equals", "Object inObj", "boolean")
                        ]
        ds['methods']['data'].extend(defaultmethods)

    
    context = {
        'ds': ds
    }
    #
    with open(fname, 'w') as f:
        java = render_template('javaclass.jinja', context)
        f.write(java)


def main():
    create_class_java()

#############################################################################

if __name__ == "__main__":
    main()
