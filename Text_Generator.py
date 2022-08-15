from nltk.tokenize import regexp_tokenize
from nltk import trigrams
from collections import Counter
import random


def tokenize(path):
    corpus = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            corpus += regexp_tokenize(line, r"[^\s]+")
    return corpus


def chain_create():
    file = input()
    corpus = tokenize(file)
    trigram = list(trigrams(corpus))
    trigrams_dict = {}
    for head_1, head_2, tail in trigram:
        trigrams_dict.setdefault((head_1, head_2), []).append(tail)
    result = {}
    for word in trigrams_dict:
        result[word] = Counter(trigrams_dict[word])
    return result


def main():
    min_word_number = 5
    number_of_sentences = 10
    chain = chain_create()
    end_symbols = '.?!'
    for i in range(number_of_sentences):
        while True:
            sentence = []
            word = random.choice(list(chain.keys()))
            if not word[0][0].isupper() or end_symbols.count(word[0][-1]) or end_symbols.count(word[1][-1]):
                continue
            sentence.append(' '.join(word))
            while True:
                keys = [x[0] for x in chain[word].most_common()]
                values = [x[1] for x in chain[word].most_common()]
                word = word[1], random.choices(keys, values)[0]
                sentence.append(word[1])
                if end_symbols.count(word[1][-1]):
                    break
            if len(sentence) < min_word_number:
                continue
            break
        print(' '.join(sentence))


if __name__ == '__main__':
    main()
