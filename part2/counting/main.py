# Вам нужно написать функцию counter, 
# которая должна подсчитать количество городов в регионах. 
# На вход функция принимает towns - список объектов Town, 
# на выходе должна возвращать словарь, 
# где ключ - регион, значение - количество городов в этом регионе. 
# Для решения задачи следует применить defaultdict.
from collections import namedtuple, Counter, defaultdict
from operator import itemgetter
from typing import Any

Town = namedtuple('Town', ['name', 'region'])
 
towns = [Town('балашиха', 'мо'), Town('химки', 'мо'), Town('тула', 'тульская область')]


def counter(towns):
    def_dict = defaultdict(lambda: 0)
    for region in map(itemgetter(1), towns):
        def_dict[region] += 1
    return def_dict

    # _counter = Counter(map(itemgetter(1), towns))
    # return _counter


if __name__ == "__main__":
    print(counter(towns))
