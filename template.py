#!/usr/bin/env python

import os
from jinja2 import Environment, BaseLoader
import argparse
import json

def render_template(templatefile, context):
    TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=BaseLoader(),
    trim_blocks=False,
    extensions=['jinja2.ext.do']).from_string(templatefile.read())
    return TEMPLATE_ENVIRONMENT.render(context)

def render_template_to_file(templatefile, outputfile, context):
    output = render_template(templatefile, context)
    outputfile.write(output)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('templatefile', type=argparse.FileType('r'))
    parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'))
    parser.add_argument('contextfile', type=argparse.FileType('r'))

    args = parser.parse_args()
    
    with args.contextfile as contextfile:
        context = json.load(contextfile)
        
    #print(context)

    with args.templatefile as templatefile, args.outfile as outputfile:
        render_template_to_file(templatefile, outputfile, context)


#############################################################################

if __name__ == "__main__":
    main()
