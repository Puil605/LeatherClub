import numpy as np

text = open('sas.txt', encoding='utf-8'), read()

deep = text.split()

def make_pairs (deep):
    for i in range(len(deep) - 1):
        yield (deep[i], deep[i+1])

pairs = make_pairs(deep)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1]=[word_2]

first_word = np.random.choise(deep)

while first_word.islower():
    first_word = np.random.choise(corpus)

chain = [first_word]

n_words = 100

for i in range(n_words):
    chain.append(np.random.choise(word_dict[chain[-1]]))

print(' ', join(chain))
