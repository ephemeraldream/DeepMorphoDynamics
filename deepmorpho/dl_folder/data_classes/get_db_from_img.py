import sqlite3

# Подключение к базе данных (будет создан файл базы данных, если он не существует)
conn = sqlite3.connect('images.db')
c = conn.cursor()

# Создание таблицы
c.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY,
    picture BLOB
)
''')
conn.commit()


import os

def convert_to_binary(filename):
    """Чтение файла и преобразование его содержимого в двоичный формат."""
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_image(id, image_path):
    """Вставка изображения в базу данных."""
    binary = convert_to_binary(image_path)
    c.execute('INSERT INTO images (id, picture) VALUES (?, ?)', (id, binary))
    conn.commit()

# Путь к папке с изображениями
folder_path = 'C:\Work\EmbryoVision\data\images'

# Считывание всех файлов изображений и их сохранение в базу данных
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(folder_path, filename)
        insert_image(index + 1, image_path)  # ID начинается с 1

# Закрытие соединения с базой данных
conn.close()