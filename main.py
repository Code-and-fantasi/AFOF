import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Глобальная переменная для хранения пути к папке
folder_path = ""

# Создание окна
root = tk.Tk()
root.title("Ввод пути к папке")

# Переменная для выбора наличия последней директории
use_last_directory = tk.BooleanVar(value=True)  # Переменная для выбора наличия последней директории

# Функция для получения пути к папке от пользователя
def get_folder_path():
    global folder_path
    folderpath = filedialog.askdirectory(initialdir="/", title="Выбрать папку")
    if folderpath:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, folderpath)
        folder_path = folderpath

# Функция для закрытия окна программы
def close_window():
    root.destroy()

# Функция для категоризации файлов в директории
def categorize_files_in_directory(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Ошибка", f"Каталог {directory} не существует.")
        return

    file_categories = {}
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            extension = item.split('.')[-1] if '.' in item else 'no_extension'
            if extension not in file_categories:
                file_categories[extension] = []
            file_categories[extension].append(item)

    result = ""
    for ext, files in file_categories.items():
        result += f"Тип файла: {ext} - Количество файлов: {len(files)}\n"
        for file in files:
            result += f"  - {file}\n"

    messagebox.showinfo("Результаты категоризации", result)

    # Запускаем функцию для создания папок и перемещения файлов
    create_folders_and_move_files(directory)

# Функция для перемещения файлов в папки на основе их имен (без расширения)
def create_folders_and_move_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Извлекаем имя файла без расширения
            name_without_extension = os.path.splitext(filename)[0]
            parts = name_without_extension.split('_')  # Разделяем имя по символу '_'
            current_path = folder_path
            
            # Создаем папки на основе частей имени файла
            for part in parts[:-1]:  # Создаем папки для всех частей, кроме последней
                current_path = os.path.join(current_path, part)
                if not os.path.exists(current_path):
                    os.makedirs(current_path)

            # Если пользователь выбрал создание последней директории, добавляем ее
            if use_last_directory.get():
                last_part = parts[-1]
                current_path = os.path.join(current_path, last_part)
                if not os.path.exists(current_path):
                    os.makedirs(current_path)

            # Перемещаем файл в конечную папку
            try:
                shutil.move(file_path, current_path)
                print(f"Файл '{filename}' перемещен в '{current_path}'.")
            except Exception as e:
                print(f"Ошибка при перемещении файла '{filename}': {e}")

# Текстовая метка
label = tk.Label(root, text="Введите путь к папке:")
label.pack(pady=10)

# Поле ввода
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

# Кнопка выбора папки
button = tk.Button(root, text="Выбрать папку", command=get_folder_path)
button.pack(pady=5)

# Переключатель для выбора наличия последней директории
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

radio_button1 = tk.Radiobutton(radio_frame, text="Создать последнюю директорию", variable=use_last_directory, value=True)
radio_button1.pack(side=tk.LEFT, padx=5)

radio_button2 = tk.Radiobutton(radio_frame, text="Не создавать последнюю директорию", variable=use_last_directory, value=False)
radio_button2.pack(side=tk.LEFT, padx=5)

# Кнопка "Готово"
done_button = tk.Button(root, text="Готово", command=lambda: [close_window(), categorize_files_in_directory(folder_path)])
done_button.pack(pady=5)

# Запуск окна
root.mainloop()
