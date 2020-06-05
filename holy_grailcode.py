import matplotlib.pyplot as plt
import re
from nltk.tokenize import word_tokenize,regexp_tokenize
f=open("holy_grail.txt", "r")
contents =f.read()
# Split the script into lines: lines
lines = re.split('\n',contents)

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s,"\w+") for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)

# S0how the plot
plt.show()
