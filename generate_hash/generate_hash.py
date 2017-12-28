"""
Ivan Marin
ispmarin@gmail.com


Generate SHA 256 hashes from fields in a CSV file.
"""
import hashlib
import csv
import argparse
import base64
import os
import sys


def hash_function_base64(input_string):
    """
    Generates a SHA 256 hash from a string and encodes it
    in base64.
    :param input_string:
    :return: base64(sha256(string).upper())
    """
    return base64.b64encode(
        hashlib.sha256(
            input_string
        ).hexdigest().upper()
    )

def hash_function(input_string):
    """
    Generates a SHA 256 hash from a string
    :param input_string:
    :return: (sha256(string).upper())
    """
    return hashlib.sha256(
            input_string
        ).hexdigest().upper()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert a list of fields in a CSV file to SHA 256 hashes.'
    )
    parser.add_argument(
        '-i',
        '--input_file',
        help='CSV file with the numbers to be hashed.',
        type=str,
        required=True
    )
    parser.add_argument(
        '-o',
        '--output_file',
        help='CSV file with the hashed numbers.',
        type=str,
        required=True
    )
    parser.add_argument(
        '-n',
        '--name_field',
        help='Name of the field to be read.',
        type=str,
        required=True
    )

    parser.add_argument(
        '-f',
        '--out_field',
        help='Name of the field to be written.',
        type=str,
        required=True
    )

    parser.add_argument(
        '-b',
        '--base64_flag',
        help='If the hash SHA 256 is encoded on Base64 or not. Default is no.',
        type=str,
        choices=['yes', 'no'],
        default='no'
    )
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    field_name = args.name_field
    out_field = args.out_field
    base64_flag = args.base64_flag

    with open(input_file, 'rUb') as f, open(output_file, 'wb') as out_f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + [out_field] 
        writer = csv.writer(out_f, fieldnames, lineterminator=os.linesep)
        writer.writerow(fieldnames)
        if base64_flag == 'yes':
            hash_func = hash_function_base64
        else:
            hash_func = hash_function
        for row in reader:
            try:
                data_to_hash = row.get(field_name)
                writer.writerow(
                        [data_to_hash, hash_func(data_to_hash)]
                        )
            except ValueError as e:
                print "failure to read row ", row
                print e
