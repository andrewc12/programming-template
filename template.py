#!/usr/bin/env python

import os
from jinja2 import Environment, BaseLoader
import argparse
import json



def render_template(template_file, context):
    with template_file as f:
        TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=BaseLoader(),
        trim_blocks=False,
        extensions=['jinja2.ext.do']).from_string(f.read())
    return TEMPLATE_ENVIRONMENT.render(context)

def render_template_to_file(template_filename, output_file, context):
    with output_file as f:
        output = render_template(template_filename, context)
        f.write(output)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('templatefile', type=argparse.FileType('r'))
    parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'))
    parser.add_argument('contextfile', type=argparse.FileType('r'))

    args = parser.parse_args()
    
    with args.contextfile as contextfile:
        context = json.load(contextfile)
        
    print(context)
    #print(args)
    
    render_template_to_file(args.templatefile, args.outfile, context)


#############################################################################

if __name__ == "__main__":
    main()
