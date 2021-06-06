# Solving Riddler Classic @ https://fivethirtyeight.com/features/can-you-decipher-the-secret-message/
# Credits: using norvig.com/ngrams/enable1.txt as a list of all English words

import time


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
base = len(homeomorphic_sets) + 1
base_squared = base ** 2
letters2sets = {}
letters2indexes = {}
for index, hs in enumerate(homeomorphic_sets, 1):
    for letter in hs:
        letters2sets[letter] = hs
        letters2indexes[letter] = index
assert(len(letters2sets) == 26)
assert(len(letters2indexes) == 26)

english_words = []
max_length = 0
with open('norvig_dot_com_slash_ngrams_slash_enable1.txt', 'r') as file:
    for line in file:
        word = line.rstrip('\n').upper()
        english_words.append(word)
        length = len(word)
        if length > max_length:
            max_length = length
n_words = len(english_words)

letter_factors = [base ** i for i in range(0, max_length)]


def word_perfect_hash(word):
    return sum([letters2indexes[letter] * letter_factors[i] for i, letter in enumerate(word)])


word_hash_table = {}
for word in english_words:
    hash = word_perfect_hash(word)
    if hash not in word_hash_table:
        word_hash_table[hash] = []
    word_hash_table[hash].append(word)
word_groups_by_size = {}
for words in word_hash_table.values():
    size = len(words)
    if size not in word_groups_by_size:
        word_groups_by_size[size] = []
    word_groups_by_size[size].append(words)


def get_possible_words(word):
    return word_hash_table[word_perfect_hash(word)]


def is_unique(word):
    return len(get_possible_words(word)) == 1


def decipher(coded_word):
    print(f'Deciphering {coded_word}...')
    print('--- Start of list of possible words ---')
    for word in get_possible_words(coded_word):
        print(word)
    print('--- End of list of possible words ---')


time0 = time.time()
decipher('YIRTHA')
print()
print()
print('--- STATS ON GROUPS OF TOPOLOGICALLY EQUIVALENT ENGLISH N-GRAMS ---')
for size, word_groups in sorted(word_groups_by_size.items()):
    n_groups = len(word_groups)
    word_count = n_groups * size
    percentage = word_count * 100 / n_words
    print()
    if size == 1:
        print(f'Found {word_count} / {n_words} topologically unique English n-grams,'
              f' i.e. {percentage:.2f}% of all English n-grams.')
        print(f'The{" first such" if n_groups > 1 else ""}'
              f' word is: {sorted(sorted(word_groups, key=lambda x: (len(x[0]), x))[0])}')
    else:
        print(f'Found {n_groups} group{"s" if n_groups > 1 else ""} of {size} topologically equivalent English n-grams,'
              f' for a total of {word_count} / {n_words} n-grams, i.e. {percentage:.2f}% of all English n-grams.')
        print(f'The{" first such" if n_groups > 1 else ""}'
              f' group is: {sorted(sorted(word_groups, key=lambda x: (len(x[0]), x))[0])}')
time1 = time.time()
print(f'\nThe total run time was {time1 - time0:.2f} seconds.')
