import json
import sqlite3 as sq

# Создание справочника - файла БД и таблицы справочника
def init_db():
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS phones (
                    surname TEXT NOT NULL ,
                    name TEXT NOT NULL DEFAULT "",
                    middle_name TEXT NOT NULL DEFAULT "",
                    phone INTEGER NOT NULL DEFAULT 0
                    )""")

# Запрос всего справочника
def look_all():
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        sql = "SELECT * FROM phones "
        cur.execute(sql)
        return cur.fetchall()

# Вывод отсортированной таблицы
def look_sort(f):
    st = ""
    if f == ['Фамилия']:
        st = 'surname'
    elif f == ['Имя']:
        st='name'
    elif f == ['Отчество']:
        st='middle_name'
    else:
        st='phone'
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        sql = 'SELECT * FROM phones ORDER BY '+st
        cur.execute(sql)
        return cur.fetchall()

# Преобразование двумерного списка в список строк
def look_array(f):
    list1 = []
    for item in f:
        st = ""
        for k in item:
            j = str(k)
            st = st+" "+j
        list1.append(st)
    return list1

# Поиск контакта по фамилии
def look_surname(f):
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        sql = "SELECT * FROM phones WHERE surname=\""+f+"\""
        print(sql)
        cur.execute(sql)
        return cur.fetchall()

# Добавление контакта в таблицу
def look_add(f):
    print(f)
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        i="\""
        st = i+f[0]+i+", "+i+f[1]+i+", "+i+f[2]+i+", "+f[3]
        sql = "INSERT INTO phones VALUES("+st+")"
        print(sql)
        cur.execute(sql)

# Удаление контакта из таблицы
def look_delete(f):
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        sql = "DELETE FROM phones WHERE surname=\""+f+"\""
        print(sql)
        cur.execute(sql)

# Очистка всего списка контактов
def look_clear():
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM phones")

# Удаление таблицы базы данных
def look_oops():
    with sq.connect("phone.db") as con:
        cur = con.cursor()
        cur.execute("""DROP TABLE IF EXISTS phones""")

# Представление Мануала в виде списка команд
def print_help():
    text = []
    data = open('manual.txt', 'r', encoding='utf-8')
    for line in data:
        text.append(line)
    data.close()
    return text
