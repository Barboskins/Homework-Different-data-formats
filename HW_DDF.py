'''
Взять из папки formats.json.xml файлы с новостями newsafr.json и newsafr.xml

Написать программу, которая будет выводить топ 10 самых часто встречающихся
в новостях слов длиннее 6 символов для каждого файла.

Не забываем про декомпозицию и организацию кода в функции.
В решении домашнего задания вам могут помочь: split(), sort или sorted.
'''

import json
from pprint import pprint
"""Работа с файлом .json"""

with open ('newsafr.json', encoding = 'utf-8') as f:
    json_data = json.load(f)

news = json_data["rss"]["channel"]["items"]

def sort_list(list_):
    return list_[1]

def number_of_repetitions_json():
 results = []
 for new in news:
  results.append(new['description'].split())
 general_list = []
 list_json = []
 for elem in results:
     for el in elem:
         if len(el) > 6:
             general_list.append(el)
 for word in general_list:
     if general_list.count(word) > 1:
         if [word, general_list.count(word)] not in list_json:
             list_json.append([word, general_list.count(word)])
 for elem in list_json:
  list_json.sort(key=sort_list, reverse=True)
 return  list_json

# pprint(number_of_repetitions_json()[0:10])
def popular_words_output_json():
   popular_words =''
   for el in number_of_repetitions_json()[0:10]:
    popular_words +=el[0] +'\n'
   return f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n{popular_words}'

print(popular_words_output_json())

"""Работа с файлом .xml"""

import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

items = root.findall("channel/item")

def sort_list(list_):
 return list_[1]

def number_of_repetitions_xml():
    results = []
    for item in items:
        results.append(item.find('description').text)
        # pprint(item.find('description').text+'\n')
    list_xml = []
    general_list_2 = []
    for str_ in results:
        str_split = str_.split()
        # print(str_split)
        for elem in str_split:
            if len(elem) > 6:
                general_list_2.append(elem)
    for word in general_list_2:
        if general_list_2.count(word) > 1:
            if [word, general_list_2.count(word)] not in list_xml:
                list_xml.append([word, general_list_2.count(word)])
    for elem in list_xml:
     list_xml.sort(key=sort_list, reverse=True)
    return  list_xml

# pprint(number_of_repetitions_xml()[0:10])

def popular_words_output_xml():
   popular_words =''
   for el in number_of_repetitions_xml()[0:10]:
    popular_words +=el[0] +'\n'
   return f'Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n{popular_words}'

print(popular_words_output_xml())



