# библиотека для работы с файлами
import os
# не хард кодить пути
# rsync python поможет при сетевом
# библиотека для работы с всплывающими окнами
import tkinter as tk
from tkinter import filedialog

#Функция для получения пути к папке от пользователя
def get_folder_path():
    global folder_path # путь к папке который вводит пользователь
    folderpath = filedialog.askdirectory(
        initialdir="/",
        title="Select Folder"
    )
    if folderpath:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, folderpath)
        folder_path = folderpath
#Функция для закрытия окна программы
def close_window():
   
    global folder_path
    root.destroy()

# Создание окна
root = tk.Tk()
root.title("Ввод пути к папке")

# Текстовая метка
label = tk.Label(root, text="Введите путь к папке:")
label.pack(pady=10)

# Поле ввода
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)
input_entry.config(state="normal") # Разрешить вставку текста

# Кнопка выбора папки
button = tk.Button(root, text="Выбрать папку", command=get_folder_path)
button.pack(pady=5)

# Кнопка "Готово"
done_button = tk.Button(root, text="Готово", command=close_window)
done_button.pack(pady=5)

# Запуск окна
root.mainloop()

a  = 0
def get_file_names(folder_path):
    # Получаем список файлов в указанной папке
    try:
        file_names = os.listdir(folder_path)
        # Фильтруем только файлы (если нужно)
        files = [f for f in file_names if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except FileNotFoundError:
        global a
        a = 1
        print("Указанная папка не найдена.")
        return
    except PermissionError:
        a = 1
        print("Нет доступа к указанной папке.")
        return
if __name__ == "__main__":
    files = get_file_names(folder_path)
    
    if files:
        print("Список файлов в указанной папке:")
        for file in files:
            print(file)
    elif a == 0:
        print("Папка пуста или не содержит файлов.")