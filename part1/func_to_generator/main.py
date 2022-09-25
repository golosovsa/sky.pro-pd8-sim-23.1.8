# Есть файл логов, нужно найти в нем строки,
# которые содержат подстроку. На вход функция
# принимает путь к файлу (file_path) и подстроку (txt),
# которую нужно найти. На выходе функция возвращает
# строки из файла file_path, которые содержат подстроку txt.
# Нужно переписать код на генератор, чтобы не сохранять
# все строки из файла в переменную res.
from pathlib import Path


def find(file_path, txt):
    with open(file_path, "rt", encoding="utf-8") as fin:
        for line in fin:
            if txt in line:
                yield line


if __name__ == "__main__":
    # Попробуем сделать генератор, логов с текстом, содержащим images
    path = Path(__file__).parent
    path = path.joinpath("apache_logs.txt")
    f = find(path, "image")
    for row in f:
        print(row)
