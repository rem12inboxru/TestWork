import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()
'''
Создание базы данных для хранения информации о состоянии загруженности системы
'''
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Data(
    id INTEGER PRIMARY KEY,
    centprocessor REAL,
    ramfree REAL,
    ram REAL,
    hddfree REAL,
    hdd REAL)''')
'''
Метод для записи данных в базу
'''
def recording(x1, x2, x3, x4, x5 ):
    cursor.execute("INSERT INTO Data (centprocessor, ramfree, "
                   "ram, hddfree, hdd) VALUES (?, ?, ?, ?, ?)", (x1, x2, x3, x4, x5))
    con.commit()