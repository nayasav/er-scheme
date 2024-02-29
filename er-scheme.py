import sqlite3


def create_connection():
    try:
        connection = sqlite3.connect('my_database.db')
        return connection
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.executescript(query)
        connection.commit()
        print("Query executed successfully.")
    except sqlite3.Error as e:
        print(f"Error: {e}")


create_tables_query = 
CREATE TABLE IF NOT EXISTS `Спiвробiтники`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `iм'я` TEXT NOT NULL,
    `прiзвище` TEXT NOT NULL,
    `посада` TEXT NOT NULL,
    `вiддiл` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Контракти`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `сумма` INTEGER NOT NULL,
    `дата заключення` TEXT NOT NULL,
    `проєкт` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Вiддiли`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `назва` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Клієнти`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `контактнi данi` TEXT NOT NULL,
    `iм'я` TEXT NOT NULL,
    `контракт` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Задачi`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `опис` TEXT NOT NULL,
    `проєкт` INTEGER NOT NULL,
    `cпiвробiтник` INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `Проєкт`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `назва` TEXT NOT NULL,
    `дата початку` TEXT NOT NULL,
    `дата завершення` TEXT NOT NULL
);



insert_data_query = 
INSERT INTO `Спiвробiтники` (`iм'я`, `прiзвище`, `посада`, `вiддiл`) VALUES
    ('Анна', 'Колько', 'Розробник', 1),
    ('Борис', 'Ватаманюк', 'Mенеджер', 2);

INSERT INTO `Контракти` (`сумма`, `дата заключення`, `проєкт`) VALUES
    (15000, '2024-02-29', 1),
    (8000, '2024-02-28', 2);

INSERT INTO `Вiддiли` (`назва`) VALUES
    ('IT вiддiл'),
    ('Вiддiл продажу');

INSERT INTO `Клієнти` (`контактнi данi`, `iм'я`, `контракт`) VALUES
    ('client1@email.com', 'Клієнт 1', 1),
    ('client2@email.com', 'Клієнт 2', 2);

INSERT INTO `Задачi` (`опис`, `проєкт`, `cпiвробiтник`) VALUES
    ('Подзвонити клієнту', 1, 1),
    ('Виставлення рахунків', 2, 2);

INSERT INTO `Проєкт` (`назва`, `дата початку`, `дата завершення`) VALUES
    ('Проєкт A', '2024-01-01', '2024-03-01'),
    ('Проєкт B', '2024-02-01', '2024-04-01');


connection = create_connection()
if connection:
    execute_query(connection, create_tables_query)
    execute_query(connection, insert_data_query)

# Close connection
if connection:
    connection.close()
