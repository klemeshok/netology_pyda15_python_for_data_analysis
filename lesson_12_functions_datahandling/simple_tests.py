# coding: utf-8

from urllib import parse


def word_count(phrase):
    if phrase:
        return len(phrase.split(' '))
    else:
        return 0
word_count('')

# если это файлик для автотестирования, прежде чем тестировать функцию, ее надо импортировать из файла, где она лежит
# например, она лежит в файлике useful_functions.py (при импорте расширение не указываем)

from useful_functions import word_count


def test_word_count():
	assert word_count('мрт менделеевская') == 2
	assert word_count('') == 0

def campaign_name(url):



