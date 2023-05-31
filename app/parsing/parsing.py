import requests
from typing import Any
from ..schemas import ParsingElementData, ParsingElement

def parse_html(url: str):
    res = requests.get(url)
    return res.text


def refactor_data(url):
    if url:
        data = sorted(parse_html(url).split())
    count_data = {}
    for word in data:
        if word in count_data:
            count_data[word] += 1
        else:
            count_data[word] = 1
    print(count_data)
    return count_data


def filter_and_sorting_data(url):
    data = refactor_data(url)
    list_of_data = sorted(data.items(), key=lambda item: -item[1])[:10]
    first = ParsingElement(word=list_of_data[0][0], value=list_of_data[0][1])
    second = ParsingElement(word=list_of_data[1][0], value=list_of_data[1][1])
    third = ParsingElement(word=list_of_data[2][0], value=list_of_data[2][1])
    fourth = ParsingElement(word=list_of_data[3][0], value=list_of_data[3][1])
    fifth = ParsingElement(word=list_of_data[4][0], value=list_of_data[4][1])
    sixth = ParsingElement(word=list_of_data[5][0], value=list_of_data[5][1])
    seventh = ParsingElement(word=list_of_data[6][0], value=list_of_data[6][1])
    eighth = ParsingElement(word=list_of_data[7][0], value=list_of_data[7][1])
    ninth = ParsingElement(word=list_of_data[8][0], value=list_of_data[8][1])
    tenth = ParsingElement(word=list_of_data[9][0], value=list_of_data[9][1])
    list_of_data = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
    return ParsingElementData(elements=list_of_data)


def organize_from_db_data(data):
    first = ParsingElement(word=data[3], value=data[4])
    second = ParsingElement(word=data[5], value=data[6])
    third = ParsingElement(word=data[7], value=data[8])
    fourth = ParsingElement(word=data[9], value=data[10])
    fifth = ParsingElement(word=data[11], value=data[12])
    sixth = ParsingElement(word=data[13], value=data[14])
    seventh = ParsingElement(word=data[15], value=data[16])
    eighth = ParsingElement(word=data[17], value=data[18])
    ninth = ParsingElement(word=data[19], value=data[20])
    tenth = ParsingElement(word=data[21], value=data[22])
    list_of_data = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
    return ParsingElementData(elements=list_of_data)
