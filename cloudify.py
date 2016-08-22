#!/usr/bin/env python3.4
# Scrapes the HTML edition of GG from the Internet
import os

from wordcloud import WordCloud

GG_FILE_NAME = 'gg.txt'
GG_PLOT_NAME = 'gg.png'
STOP_WORDS = [
    'ab', 'als', 'auch', 'auf',
    'bei', 'bis',
    'das', 'dass', 'daß', 'darf', 'dem', 'den', 'der', 'des',
    'die', 'diese', 'dieser', 'dieses', 'durch',
    'ein', 'eine', 'einer', 'eines', 'es',
    'für',
    'im', 'ist',
    'mit',
    'nach', 'nicht', 'nur',
    'oder',
    'regelt',
    'sich', 'sie', 'sind', 'soweit',
    'über', 'und',
    'vom', 'von',
    'wenn', 'werden',
    'zu', 'zum', 'zur',
]


def remove_stop_words():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, GG_FILE_NAME)
    text = open(file_path, 'r').read()
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in STOP_WORDS]
    print('Cleaned words')
    return " ".join(cleaned_words)


def save_wordcloud(text):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(file_dir, GG_PLOT_NAME)
    WordCloud().generate(text).to_file(plot_path)

if __name__ == '__main__':
    text = remove_stop_words()
    save_wordcloud(text)
