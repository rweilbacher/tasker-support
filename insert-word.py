from tempfile import NamedTemporaryFile
import shutil
import csv
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', help='Path to CSV word list', required=True)
parser.add_argument('-w', '--word', help='The word to be incremented', required=True)
args = parser.parse_args()

tempfile = NamedTemporaryFile(mode="w", newline="", delete=False)

with open(args.list, "r") as csv_file, tempfile:
    reader = csv.reader(csv_file)
    writer = csv.writer(tempfile)
    word_found = False
    for row in reader:
        if row[0].lower() == args.word.lower():
            try:
                new_row = [row[0], int(row[1]) + 1]
            except ValueError:
                sys.stderr.write(f"Amount for item {row[0]} is not a valid number: {row[1]}")
            writer.writerow(new_row)
            word_found = True
        else:
            writer.writerow(row)
    if word_found is False:
        writer.writerow([args.word, 1])

shutil.move(tempfile.name, args.list)
