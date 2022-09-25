# Напишите, свой собственный генератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Дополните функцию fib


def fib(n):
    seq_start = [0, 1, 1]
    value, prev = 0, 0
    for index in range(n):

        if index < len(seq_start):
            ret = seq_start[index]
        else:
            ret = value + prev

        prev, value = value, ret
        yield ret


fib_gen = fib(15)

if __name__ == "__main__":
    print([x for x in fib_gen])
