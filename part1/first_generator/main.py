# С помощью функции iter нужно создать итератор,
# затем получить и вывести первые 3 элемента списка arr
# С помощью функции arr_generator нужно создать генератор,
# затем получить и вывести первые 3 элемента списка.
# Просим Вас в этом задании не пользоваться блоком if __name__ == __main__
# чтобы наши тесты могли проверить, на самом ли деле ожидаемые ответы были
# выведены в терминал


def arr_generator(arr):
    for item in arr:
        yield item


arr = [1, 2, 3, 4, 5]

it = iter(arr)
print(next(it))
print(next(it))
print(next(it))

gen = arr_generator(arr)
print(next(gen))
print(next(gen))
print(next(gen))
