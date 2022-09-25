# Вам нужно написать функцию top3, 
# которая на вход принимает строку и 
# возвращает 3 наиболее повторяющихся элемента из входной строки.
from collections import Counter
from operator import itemgetter


def top3(input_str):
    counter = Counter(input_str)
    return list(map(itemgetter(0), counter.most_common(3)))


if __name__ == "__main__":
    print(top3('11111111222222223333333344444444555555'))
