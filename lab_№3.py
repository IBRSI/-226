from collections import Counter

#1
def transpose(mat):

    return list(zip(*mat))


#2
def assignpets(lst):
    pets_dict = {}

    for tup in lst:
        owner = '{0} {1}'.format(tup[2], tup[3])
        pets = '{0}, возраст - {1}'.format(tup[0], tup[1])

        if owner not in pets_dict:
            pets_dict.setdefault(owner, pets)
        else:
            pets_dict.update({owner: pets_dict.get(owner) + '; ' + pets})
    return pets_dict

#3
def rarestword(string):
    if not string or string.isdigit():
        return 'Слов нет'

    nstring = ''
    for i in string:
        if i.isalpha() or i.isspace():
            nstring = nstring + i.lower()


    split_string = nstring.split()


    word_freqs = Counter(split_string)

    if not word_freqs:
        return 'Слов нет'


    words = [i for i in word_freqs if word_freqs.get(i) == min(word_freqs.values())]


    return sorted(words)[0]

#4
def frequentword(string):
    if not string or string.isdigit():
        return 'Букв нет'

    nstring = ''.join(filter(str.isalpha, string.lower()))


    letters = Counter(nstring)

    if not letters:
        return 'Букв нет'


    max_value = max(letters.values())


    max_letters = [i for i in letters if letters[i] == max_value]


    return sorted(max_letters)[0]

#5
def palindrome(string):

    string = string.replace(' ', '')


    result = True
    if len(string) > 1:
        if string[0].lower() == string[-1].lower():
            result = palindrome(string[1:-1])
        else:
            result = False
    return result

#6
def ssort(array):  #
    nums = Counter(array)


    inverse_nums = {}
    for key, value in nums.items():
        inverse_nums.setdefault(value, list()).append(key)

    sorted_nums = dict(sorted(inverse_nums.items()))


    result = []
    for key, value in sorted_nums.items():
        for numbers in value:
            result.extend([numbers for i in range(key)])
    return result

#7
def threewords(string):
    array = string.split()
    count = 0
    for i in range(len(array)):
        count += 1
        if not array[i].isalpha():
            count = 0
        if count == 3:
            return True
    return False

#8
def maxconsequence(string):
    string = string.lower()
    count = 1
    save = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and string[i].isalpha():
            count += 1
            save = count if save < count else save
        else:
            count = 1
    return save

#9
def expression(string):
    try:
        return eval(string)
    except Exception as e:
        return e

#10
def summed_dict(list_of_dicts):
    new_dict = {}


    for dic in list_of_dicts:
        for key in dic.keys():

            if key not in new_dict.keys():
                new_dict.setdefault(key, dic.get(key))

            else:
                new_dict.update({key: new_dict.get(key) + dic.get(key)})
    return new_dict