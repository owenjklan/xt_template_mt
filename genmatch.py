#!/usr/bin/env python3
"""
Generate the boiler-plate for an xtables match extension.
Generates the following files, where 'name' is the name used for
the generated match:
  - xt_name.c      - Source for xtables kernel module component
  - xt_name.h      - Header file for the extension
  - libxt_name.c   - iptables cmd extension plugin for '-m name'
  - Makefile       - Builds the kernel module as xt_name.ko
  - Makefile.libxt - Builds the iptables cmd extension as libxt_name.so
"""
import sys

import jinja2
from jinja2 import Template


TEMPLATE_FILES = [
    "xt_template.c.j2",
    "xt_template.h.j2",
    "libxt_template.c.j2",
    "Makefile.j2",
    "Makefile.libxt.j2",
]


def get_output_filename(match_name, template_filename):
    """
    When given a particular 'match_name', manipulates the name of
    the given 'template_filename' to be representative of where the
    processed template should be written to on disk.
    """
    base_name = template_filename.split('.j2')[0]
    return base_name.replace('template', match_name.lower())


def process_template(input_template, output_filename, template_data):
    with open(input_template, "r") as template_file:
        template = Template(template_file.read())

    with open(output_filename, "w+") as output_file:
        output_file.write(template.render(**template_data))


def main():
    template_data = {}
    template_data['name'] = input(
        "Name of the match. This should be lower-case and short: ")
    template_data['module_description'] = input(
        "Description of match module: ")
    template_data['module_version_string'] = input(
        "Version string for module: ")
    template_data['module_license'] = input(
        "License string for module: ")
    template_data['module_author'] = input(
        "Author's name: ")

    for tmpfile in TEMPLATE_FILES:
        print("{:>32} => {}".format(
            tmpfile, get_output_filename(template_data['name'], tmpfile)))
        process_template(
            tmpfile,
            get_output_filename(template_data['name'], tmpfile),
            template_data)


if __name__ == '__main__':
    main()
