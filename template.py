#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader
import argparse
import json

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False,
    extensions=['jinja2.ext.do'])


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def render_template_to_file(template_filename, output_filename, context):
    with open(output_filename, 'w') as f:
        output = render_template(template_filename, context)
        f.write(output)

def main():
    parser = argparse.ArgumentParser()

    #parser.add_argument('templatefile', type=argparse.FileType('r'))
    #parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'))
    parser.add_argument('contextfile', type=argparse.FileType('r'))

    args = parser.parse_args()
    
    with args.contextfile as contextfile:
        context = json.load(contextfile)
        
    print(context)
    
    render_template_to_file('javaclass.jinja', 'outputclass.java', context)


#############################################################################

if __name__ == "__main__":
    main()
