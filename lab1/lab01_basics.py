import numpy as np
import fileinput, pathlib


class Crawler:
    pth = 'C:\\Users\\nick-\\hello\\lab1'
    pattern = '*.txt'
    files_path = pathlib.Path(pth)
    list_files = files_path.glob(pattern)
    new_file = 'new_file.all'
    if list_files:
        with fileinput.FileInput(files=list_files) as fr, open(new_file, 'w') as fw:
            for line in fr:
                if fr.isfirstline():
                    file_name = fr.filename()
                fw.write(line)
    text = open('new_file.all', encoding='utf-8').read()
pass

class Generator:
    deep = Crawler.text.split()

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

    first_word = np.random.choice(deep)

    while first_word.islower():
        first_word = np.random.choice(deep)

    chain = [first_word]

    n_words = 146

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
pass

class saver:
    text =(' '.join(Generator.chain))
    new_file = 'new_text.txt'
    dungeon = open('new_text.txt', 'w')
    print(text.encode("utf-8"), file = dungeon)
    dungeon.close()
pass

