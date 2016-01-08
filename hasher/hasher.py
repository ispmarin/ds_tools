import hashlib
import csv


def hasher(input_string):
    return hashlib.sha256(input_string).hexdigest().upper()


if __name__ == '__main__':
    with open('data/sample.csv', 'r') as f, open('data/newfile.csv', 'w') as outf:
        reader = csv.DictReader(f)
        # here sets which columns should be on the output file
        fieldnames = reader.fieldnames + ['hash_cpf']
        writer = csv.DictWriter(outf, fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow(
                dict(
                    row, hash_cpf=hasher(
                        row['cpf']
                    )
                )
            )


