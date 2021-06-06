# Solving Riddler Classic @ https://fivethirtyeight.com/features/can-you-decipher-the-secret-message/
# Credits: using norvig.com/ngrams/enable1.txt as a list of all English words


import itertools


with open('norvig_dot_com_slash_ngrams_slash_enable1.txt', 'r') as file:
    english_words = set([line.rstrip('\n').upper() for line in file])


# Letters are topologically equivalent if their uppercase forms in the given sans serif font are homeomorphic.
# Reference: https://en.wikipedia.org/wiki/Homeomorphism
homeomorphic_sets = [
    'AR',
    'B',
    'CGIJLMNSUVWZ',
    'EFTY',
    'DO',
    'PQ',
    'HK',
    'X',
]
letters2sets = {}
for hs in homeomorphic_sets:
    for le in hs:
        letters2sets[le] = hs
assert(len(letters2sets) == 26)


def decipher(coded_word):
    print(f'Deciphering {coded_word}...')
    print('--- Start of list of possible words ---')
    for word in itertools.product(*[letters2sets[le] for le in coded_word.upper()]):
        word = ''.join(word)
        if word in english_words:
            print(word)
    print('--- End of list of possible words ---')


decipher('YIRTHA')
