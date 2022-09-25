# Напишите, свой собственный итератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Для решения задачи нужно дополнить класс Fib
# Достаточно будет сделать итератор только для положительных чисел


class Fib:
    def __init__(self, n):
        self.n = n
        self.current_index = 0
        self.prev = 0
        self.value = 0
        self.seq_start = [0, 1, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.n:
            raise StopIteration
        if self.current_index < len(self.seq_start):
            ret = self.seq_start[self.current_index]
        else:
            ret = self.prev + self.value

        self.prev, self.value = self.value, ret
        self.current_index += 1
        return ret



fib = Fib(15)

if __name__ == "__main__":
    print([x for x in fib])
