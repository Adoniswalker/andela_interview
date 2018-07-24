import re


def pig_latin_fun(word):
    word = word.lower()
    if not word.isalpha():
        return
    if word.startswith(('a','e','i','o','u')):
        return word+ 'way'
    re_obj = re.compile('[a,e,i,o,u]')
    first_vowel = re_obj.search(word)
    if not first_vowel:
        return word
    first_vowel = first_vowel.group()
    before_vowel, after_vowel = word.split(first_vowel, 1)
    return first_vowel + after_vowel+before_vowel +'ay'