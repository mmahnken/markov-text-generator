#!/usr/bin/env python
from sys import argv
import re #regular expressions, used to remove symbols
import random #allows to select random elements of markov_dict

script, filename = argv

f = open(filename)
new_text = f.read()

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""


    #new_text = re.sub(r'[^a-z ]', "", pre_text.lower())
    #set up the dictionary, split the words into individual strings
    markov_dict = {}
    new_list = new_text.split(" ")

    #loop through the list of words
    #take word and the word after that and make it the markov_dict's keys
    #take word #3 and make it the value
    for index, word in enumerate(new_list):
        word1 = new_list[index]
        word2 = new_list[index + 1]
        word3 = new_list[index + 2]

        #check if at the end of the word list
        if index == len(new_list) - 3:
            break
        #set the key of the markov_dict to the first two items in the list
        mkey = word1 + " " + word2
        #check if the key is not in the dictionary already, if it's not
        #add key
        if not mkey in markov_dict:
            markov_dict[mkey] = {}
        #if the key is in the dict, increment the value
        #otherwise, initialize the value at 1
        if word3 in markov_dict[mkey]:
            markov_dict[mkey][word3] += 1
        else:
            markov_dict[mkey][word3] = 1

    return markov_dict


def make_text(markov_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #retrieve a random key from the markov_dict
    #from the key, retrieve a random value
    #print them together
    random_phrase = random.choice(markov_dict.keys())
    print random_phrase
    return "Here's some random text."

# def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()


markov_dict = make_chains(filename)
print make_text(markov_dict)
