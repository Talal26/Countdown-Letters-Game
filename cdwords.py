import re
from itertools import permutations as perm

# converting txt file of english words to set
with open('cdwords.txt', 'r') as cdwords:
    cdwords = cdwords.read()
    wordregex = re.compile('\w+')
    cdwords = wordregex.findall(cdwords)
    cdwords = set(cdwords)


#                  123456789
characters = list('ACESPANK'.lower())
length = len(characters)
words = set()
alphabet = set('abcdefghijklmnopqrstuvwxyz')
not_alpha = alphabet.difference(set(characters))

possible = set()

# Ruling out words which contain letters not in 'characters'
for word in cdwords:
    for letter in not_alpha:
        if letter in word:
            break
    else:
        possible.add(word)

# Finding every permutation of 'characters' for each length from 1 to how many letters there are
for l in range(1, length + 1):
    for subset in perm(characters, l):
        word = ''.join(subset)
        words.add(word)

print(f'{len(words)} permutations possible')

words = list(words)
words.sort()

results = []

# Checking which words can be created from the characters
for w in words:
    if w in possible:
        results.append(w)

d = {}
total = 0

# Placing all possible words in dictionary according to their length
for l in range(1, length + 1):
    d[l] = []
    for word in results:
        if len(word) == l:
            d[l].append(word)
    total += len(d[l])

for l in range(length, 0, -1):
    print(f'{l} letter words: {d[l]}')

print(f'{total} words found')
