#!/usr/bin/env python3

# TODO: Refactoring
# - Fix Unicode escaping in hints (and notes? and elsewhere?)
# - Preview metadata for Twitter/Slack/Facebook/etc

import os
import sys

from generator_year import GeneratorYear
from generator_month import GeneratorMonth
from month import Years, Months, Month
from puzzle import Puzzle
from template import Template

if len(sys.argv) != 3:
    print("Put source folder and destination folder on command line.")
    print("Example: ./generator.py .. ../static")
    sys.exit(1)

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

# Validate source.
if not os.path.isdir(source_folder):
    print("Source folder must be a directory")
    sys.exit(1)
if not os.path.isdir(os.path.join(source_folder, '2010')):
    print("Source folder does not appear to be correct. It needs to contain year subfolders.")
    sys.exit(1)

# Validate destination.
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)
if not os.path.isdir(source_folder):
    print("Destination folder must be a directory")
    sys.exit(1)

years = Years(source_folder)
generator_year = GeneratorYear(source_folder, destination_folder, years)
generator_year.generate()
generator_month = GeneratorMonth(source_folder, destination_folder, years)
generator_month.generate()
