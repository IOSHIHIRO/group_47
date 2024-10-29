import sqlite3

conn = sqlite3.connect('ДЗ.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS countries(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Name NOT NULL,
rover_level REAL DEFAULT 0
)
''')


cursor.execute ('''
    INSERT INTO countries (Name,rover_level) VALUES
('Фезарин Августус Аврора',100),('Алукард',89),('Гильгамеш',98)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Capabilities(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title_Capabi NOT NULL,
Rarity NOT NULL
)
''')

cursor.execute('''
INSERT INTO Capabilities (title_Capabi,Rarity) VALUES
 ('Внепричинность','(S)-Ранг'),('Манипуляции реальностью','(A)-Ранг')
 ,('Отражение','(B)-Ранг'),('Анти-регенерация','(A)Ранг')

''')

conn.commit()

def countries_ger():
    print("Вы можете отобразить список героев по выбранному id"
          " способности из перечня ниже, для выхода из программы введите 0:")


    cursor.execute('SELECT id,title_Capabi FROM Capabilities GROUP BY title_Capabi;')
    cities = cursor.fetchall()
    for city in cities:
        print(f'{city[0]}: {city[1]}')

    title_Capabi = input('Введите id способности')
    if title_Capabi == '0':
        print('Выход из программы.')
        conn.close()
        return

    cursor.execute('''
    SELECT countries.Name, countries.rover_level, Capabilities.title_Capabi,Capabilities.Rarity
    FROM Capabilities JOIN countries ON countries.id = Capabilities.id
    JOIN countries ON countries.id = countries.id
    WHERE Capabilities.id = ?
    GROUP BY countries.Name, countries.rover_level;
    ''', (title_Capabi,))

    rows = cursor.fetchall()

    # Вывод информации об учениках
    if rows:
        print("\nИнформация об учениках:")
        for row in rows:
            print(f"Имя: {row[0]}, Фамилия: {row[1]}, Страна: {row[2]}, Город: {row[3]}, Площадь: {row[4]} км²")
    else:
        print("Нет учеников в данном городе.")

    conn.close()


if __name__ == '__main__':
    countries_ger()

conn.close()
