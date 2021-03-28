# Title
# # Hour of Code HK - Python Lesson 8
# Author: Anson
# Date: 28 March, 2021

import random
import string

# Banner
print('Hour of Code Hong Kong')
print('Welcome to Sentence Generator')

# Noun list
noun_list = ['apple', 'dinosaur', 'ball', 'goat']


# Adjective list
adjective_list = ['sleepy', 'slow', 'smeely', 'wet']

# Adverb list
adverb_list = ['slowly', 'bravely', 'angryly', 'sadly']

# Verb list
verb_list = ['runing', 'eating', 'flying', 'walking']

for i in range(len(noun_list)):
  print(noun_list[i])

noun = random.choice(noun_list)
verb = random.choice(verb_list)
adj = random.choice(adjective_list)
adv = random.choice(adverb_list)



my_sentence = 'a' + adj + noun + verb + adv 
print(my_sentence)

