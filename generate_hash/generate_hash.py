"""
Ivan Marin
Vivo Data Labs
ivan.smarin@telefonica.com
"""
import hashlib
import csv
import argparse
import base64
import os


def hash_function(input_string):
    """
    Generates a SHA 256 hash from a string and encodes it
    in base64.
    :param input_string:
    :return: base64(sha256(string))
    """
    return base64.b64encode(
        hashlib.sha256(
            input_string
        ).hexdigest()
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert a list of numbers to SHA 256 hashes encoded in base64.'
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
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    with open(input_file, 'rUb') as f, open(output_file, 'wb') as out_f:
        reader = csv.DictReader(f)
        # here sets which columns should be on the output file
        fieldnames = reader.fieldnames + ['hash_field']
        writer = csv.DictWriter(out_f, fieldnames, lineterminator=os.linesep)
        writer.writeheader()
        for row in reader:
            try:
                data_to_hash = row.get('cpf')
                print(data_to_hash)
                writer.writerow(
                    dict(
                        row,
                        hash_field=hash_function(
                            data_to_hash
                        )
                    )
                )
            except ValueError:
                print "failure to read row ", row
