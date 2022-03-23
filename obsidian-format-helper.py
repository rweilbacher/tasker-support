#!/data/data/com.termux/files/usr/bin/python
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input text', required=True)
args = parser.parse_args()

# test = "text #link *italics **bold text #eof-before-space"
# text = test
text = args.input


new_text = ""
i = 0
while i < len(text):
    # Turn tags into links
    if text[i] == '#':
        i += 1
        if text[i] == " " or text[i] == "\n":
            # A hashtag followed by a space indicates a heading not a link
            new_text += "#"
            continue

        new_text += "[["
        while i < len(text) and text[i] != " " and text[i] != "\n":
            new_text += text[i]
            i += 1
        new_text += "]]"
    # Automatically close bold and italics
    elif text[i] == '*':
        new_text += '*'
        suffix = '*'
        i += 1
        if text[i] == '*':
            new_text += '*'
            suffix += '*'
            i += 1
        while i < len(text) and text[i] != " " and text[i] != "\n":
            new_text += text[i]
            i += 1
        new_text += suffix
    else:
        new_text += text[i]
        i += 1

sys.stdout.write(new_text)
sys.exit(0)
