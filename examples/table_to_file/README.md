# Описание

Данный пример позволяет парсить данные из защищеной паролем базы в тектовый файл.

## Пример: 

1. Сначала выведим все таблицы:

`python table2csv.py -f test_protected.mdb -c`

2. Теперь спарсим данные из таблицы *ClarotyTable*:

`python table2csv.py -f test_protected.mdb -t ClarotyTable -o`

> Рядом с базой будeт файл *ClarotyTable.csv*

# Зависимости

`pip install pandas`

> Пароль к базе "CgUsiNnGB~0Tukm?8gli" для сверки данных.