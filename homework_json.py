import chardet
import json
from pprint import pprint


def get_rus_json(filename):
        with open('./' + filename, 'rb') as f:
            data = f.read()
            codepage = chardet.detect(data)
            result = data.decode(encoding=codepage['encoding'])
        return json.loads(result)


def print_top_10(file):
    # Получаем русифицированный json в виде строки
    rus_json = get_rus_json(file)
    
    # Разбираем все description на отдельные слова
    words_list = []
    for d in rus_json['rss']['channel']['items']:
    	words_list += d['description'].split(' ')

    # Оставляем только слова, где более 6 символов
    short_list = [s.lower() for s in words_list if len(s) >= 6]

    # Составляем словарь, где ключ - слово, значение - сколько раз оно встретилось
    frequency_dict = dict()
    for word in short_list:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    # Сортировка словаря, подсмотрено тут https://www.python.org/dev/peps/pep-0265/
    items = [(v, k) for k, v in frequency_dict.items()]
    items.sort()
    items.reverse()
    print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов в файле {}:'.format(file))
    print(items[:10])

print_top_10('newsafr.json')
print_top_10('newsit.json')
print_top_10('newsfr.json')
print_top_10('newscy.json')
