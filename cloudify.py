#!/usr/bin/env python3.4
# Scrapes the HTML edition of GG from the Internet
import os

from wordcloud import WordCloud

GG_FILE_NAME = 'gg.txt'
GG_PLOT_NAME = 'gg.png'


def save_wordcloud():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, GG_FILE_NAME)
    text = open(file_path, 'r').read()

    plot_path = os.path.join(file_dir, GG_PLOT_NAME)
    WordCloud().generate(text).to_file(plot_path)

if __name__ == '__main__':
    save_wordcloud()
