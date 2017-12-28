#!/bin/env python2.7
# Ivan Marin
# ispmarin@gmail.com
# Converting a hive dump to a semi comma separated value file
# In the case that the fields have a comma value
# The input file should be a dump from a query in hive like
# hive -e 'select * from database.table' > input_file

import csv
import argparse

parser = argparse.ArgumentParser(
        description='Convert a Hive dump to semi comma separated file.'
)
parser.add_argument('input', help='Hive dump')
parser.add_argument('output', help='output file')
args = parser.parse_args()

input_file = args.input
output_file = args.output

with open(input_file, 'r')as csvfile, open(output_file, 'w') as output:
    spamreader = csv.reader(csvfile, delimiter='\t')
    spamwriter = csv.writer(output, delimiter=';')
    for row in spamreader:
        spamwriter.writerow(row)
