#!/usr/bin/env python3.4
# Scrapes the HTML edition of GG from the Internet
import os
import re

from wordcloud import WordCloud

GG_FILE_NAME = 'gg.txt'
GG_PLOT_NAME = 'gg.png'
STOP_WORDS = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
    'ab', 'abs', 'als', 'art', 'auch', 'auf', 'aus',
    'bei', 'bis',
    'das', 'dass', 'daß', 'darf', 'dem', 'den', 'der', 'des',
    'die', 'diese', 'dieser', 'dieses', 'durch',
    'ein', 'eine', 'einer', 'eines', 'er', 'es',
    'für',
    'im', 'in', 'ist',
    'kann',
    'mehrere', 'mit',
    'nach', 'nicht', 'nur',
    'oder',
    'regelt',
    'sich', 'sie', 'sind', 'soweit', 'sowie',
    'über', 'und',
    'vom', 'von',
    'wenn', 'werden',
    'zu', 'zum', 'zur',
]
HEIGHT = 400
WIDTH = 800


def is_noun(word):
    word_re = re.compile(r'^[A-Z]+')
    match = word_re.search(word)
    return match is not None


def remove_stop_words():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, GG_FILE_NAME)
    text = open(file_path, 'r').read()

    words = text.split()
    cleaned_words = []

    for word in words:
        lowercased_word = word.lower().strip()

        if is_noun(word) and lowercased_word not in STOP_WORDS:
            cleaned_words.append(word)
    return " ".join(cleaned_words)


def save_wordcloud(text):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(file_dir, GG_PLOT_NAME)
    WordCloud(width=WIDTH, height=HEIGHT).generate(text).to_file(plot_path)

if __name__ == '__main__':
    text = remove_stop_words()
    save_wordcloud(text)
