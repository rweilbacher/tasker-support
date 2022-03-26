import csv
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', help='Path to CSV word list', required=True)
parser.add_argument('-w', '--word', help='The word to be checked', required=True)
args = parser.parse_args()

words = []
with open(args.list, "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if len(row) < 2:
            sys.stderr.write("CSV list contains a row with less than 2 elements")
            sys.exit(1)
        word = row[0]
        try:
            amount = int(row[1])
        except ValueError:
            sys.stderr.write(f"Amount for item {word} is not a valid number: {row[1]}")
            sys.exit(1)
        words.append((word, amount))

highest_match = 0
matching_word = ""
for word, amount in sorted(words, reverse=True, key=lambda x: x[1]):
    match = 0
    # Very inefficient but should never matter with the amount of words a list is expected to contain
    for i in range(0, min(len(word), len(args.word))):
        if word[i].lower() == args.word[i].lower():
            match += 1
        else:
            break
    if match > highest_match:
        matching_word = word
        highest_match = match

sys.stdout.write(matching_word)
sys.exit(0)
