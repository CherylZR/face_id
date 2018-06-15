# -*- coding: UTF-8 -*-

from googletrans import Translator
from wikiapi import WikiApi
import unidecode
import csv

i = 0
# with open('e:\datasets\id\checked_entity_list_20180612.csv', 'r', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        i += 1
        if i > 5:
            break
        print(row)

# translator = Translator()
# # unidecode.unidecode
# name = translator.translate(u'Kelly A. O\'Leary \'la\'')
# name = translator.translate(u'瑞恩·奥南').text
# name = name.replace('-','').replace(' ','_').replace('.','_').replace('__','_')
# print(name)
# print(u'哈')


# i = 0
# with open('e:\datasets\id\checked_entity_list_20180612.csv', 'r', encoding="utf8") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
#     for row in spamreader:
#         i+=1
#         if i>3:
#             break
#         name = row[0].strip()[10:].replace('.','._').replace('__','_')
#         if name == 'a._proper_name':
#             continue
#         print(name)
#         if not check_english(name):
#             # If half of the names are regular English characters, see it as an accent.
#             if non_english_character_count(name) < len(name) / 2:
#                 name = unidecode.unidecode(name)
#             # Or, take it as a foreign language.
#             else:
#                 name = translator.translate(name.replace('_', ' ')).text.replace(' ', '_')
#             row[1] = ' "' + name + '"'
#             print(row)