# Архиватор строк

Программа для сжатия и распаковки строк.

## Установка

1. Установите [Python 3.7](https://www.python.org/downloads/) или выше.
2. Установите [git](https://git-scm.com/downloads).
3. Клонируйте репозиторий ```git clone https://github.com/WorldPillar/ufanet.git```.
4. Создайте и активируйте виртуальное окружение.

## Функции

- Кодирование строки как с числами, так и без них с помощью [Run-Length Encoding](https://en.wikipedia.org/wiki/Run-length_encoding).  
__Пример:__  
Вызов ```Archiver.archiver('baannaaana', bwt=False)``` вернёт '*ba2n2a3na*'. 
- Предварительное преобразование строки с помощью [Burrows-Wheeler transform](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform).  
__Пример:__  
Вызов ```Archiver.archiver('bananabanana', bwt=True)``` вернёт '*8an4b2a a4*'.  
Первое число необходимо для обратного преобразования BWT.
- Декодирование 'сжатых' строк.

## Тесты

Тесты реализованы с помощью модуля unittest. 

- Запуск тестов функции-архиватора и функции-разархивирования  
```python -m unittest test.test_archiver```
- Запуск тестов RLE ```python -m unittest test.test_rle```
- Запуск тестов BWT ```python -m unittest test.test_bwt```