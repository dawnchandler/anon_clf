'''
Headings: 
comment_author,num_chars,has_digits,num_tokens,has_first_name,has_last_name,num_words
'''
import pandas as pd
import numpy as np
import re

# Returns a ['Camel', 'Case', 'XYZ'] split of a string.
def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

# Make dictionaries of first and last names.
with open('./data/names/first_names.txt', 'r', encoding='utf-8') as f:
    first_names = {} # TODO: This doesn't need to be a dictionary. Change to list?
    for name in f:
        name = name[:-1] # Exclude newline character.
        first_names[name] = 1
with open('./data/names/last_names.txt', 'r', encoding='utf-8') as f:
    last_names = {} # TODO: This doesn't need to be a dictionary. Change to list?
    for name in f:
        name = name[:-1] # Exclude newline character.
        last_names[name] = 1

# Make dictionary of Scrabble words.
with open('./data/words/scrabble_words.txt', 'r', encoding='utf-8') as f:
    scrabble_words = {} # TODO: This doesn't need to be a dictionary. Change to list?
    for word in f:
        word = word[:-1] # Exclude newline character.
        scrabble_words[word] = 1

# Create output file:
path_to_output = './data/output.csv'
with open(path_to_output, 'a', encoding='utf-8') as o: # a is to append to file.

    # Add header to output CSV file:
    path_to_headers = './data/headers.csv'
    with open(path_to_headers, 'r', encoding='utf-8') as h:
        headers = h.readline()
        o.write(headers)
        
# TODO: Create config for file paths.
#path_to_data = './data/comments_1.5k.data'
path_to_data = './data/comments_sample.data'
with open(path_to_data, 'r', encoding='utf-8') as f: 
    for username in f:

        username = username[:-1] # Exclude newline character.

        path_to_output = './data/output.csv'
        with open(path_to_output, 'a', encoding='utf-8') as o: # a is to append to file.

            line = username

            # Add columns for features about the username.
            # TODO: Make each column its own function.
            
            # Add column for num_chars (length of username):
            num_chars = len(username) 
            line += ',' + str(num_chars) 

            # Add column for has_digits (presence of digits in username):
            if re.search(r'\d', username):
                line += ',True'

                # Remove digits:
                ret = []
                for char in username:
                    if not char.isdigit():
                        ret.append(char)
                username = ''.join(ret) 

            else:
                line += ',False'

            # Segmentation:
            if ' ' in username:
                seg = username.split(' ')
            elif '_' in username:
                seg = username.split('_')
            elif '-' in username:
                seg = username.split('-')
            elif '.' in username:
                seg = username.split('.')
            else:
                seg = camel_case_split(username)

            # Change to lowercase.
            ret = []
            for word in seg: # TODO: Rename 'word' to 'token' for anything related to seg.
                ret.append(word.lower())
            seg = ret

            ## Add column for extracted words. # TODO: Remove.
            #seg_str = ' '.join(seg)
            #line += ',' + seg_str

            # Add column for num_tokens (number of tokens in segmentation):
            line += ',' + str(len(seg))

            # Add column for has_first_name (a token in the segmentation is in first names list):
            in_list = False
            for word in seg:
                if word in first_names:
                    line += ',' + 'True'
                    in_list = True
                    break
            if not in_list:
                line += ',' + 'False'

            # Add column for has_last_name (a token in the segmentation is in last names list):
            in_list = False
            for word in seg:
                if word in last_names:
                    line += ',' + 'True'
                    in_list = True
                    break
            if not in_list:
                line += ',' + 'False'

            # Add column for num_words (number of tokens in the segmentation that are in the Scrabble word list):
            count = 0
            for word in seg:
                if word in scrabble_words:
                    count += 1
            line += ',' + str(count)

            # Write to file:
            line += '\n'
            o.write(line)
