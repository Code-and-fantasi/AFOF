# библиотека для работы с файлами
import os
# не хард кодить пути
# rsync python поможет при сетевом
# библиотека для работы с всплывающими окнами
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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



def categorize_files_in_directory(directory):
    # Проверяем, существует ли указанный каталог
    if not os.path.exists(directory):
        messagebox.showerror("Ошибка", f"Каталог {directory} не существует.")
        return

    # Создаем словарь для хранения файлов по типам
    file_categories = {}

    # Получаем список всех файлов в указанной директории
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Проверяем, является ли это файлом
        if os.path.isfile(item_path):
            # Получаем расширение файла
            extension = item.split('.')[-1] if '.' in item else 'no_extension'
            
            # Добавляем файл в соответствующую категорию
            if extension not in file_categories:
                file_categories[extension] = []
            file_categories[extension].append(item)

    # Формируем строку для отображения
    result = ""
    for ext, files in file_categories.items():
        result += f"Тип файла: {ext} - Количество файлов: {len(files)}\n"
        for file in files:
            result += f"  - {file}\n"

    # Отображаем результаты во всплывающем окне
    messagebox.showinfo("Результаты категоризации", result)

# Функция для запуска программы с графическим интерфейсом
def run_gui():
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    # Здесь вы можете указать путь к директории
    categorize_files_in_directory(folder_path)

    root.mainloop()

# Запуск программы
run_gui()
def select_files_with_extensions(directory, extensions):
    # Проверяем, существует ли указанный каталог
    if not os.path.exists(directory):
        messagebox.showerror("Ошибка", f"Каталог {directory} не существует.")
        return

    # Получаем список всех файлов в указанной директории
    files_to_select = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Проверяем, является ли это файлом и имеет ли он нужное расширение
        if os.path.isfile(item_path):
            extension = item.split('.')[-1] if '.' in item else 'no_extension'
            if extension in extensions:
                files_to_select.append(item_path)

    # Если нет файлов с нужными расширениями
    if not files_to_select:
        messagebox.showinfo("Информация", "Нет файлов с выбранными расширениями.")
        return

    # Позволяем пользователю выбрать файлы
    selected_files = filedialog.askopenfilenames(title="Выберите файлы", initialdir=directory, filetypes=[(ext, f"*.{ext}") for ext in extensions])
    
    # Выводим выбранные файлы
    if selected_files:
        result = "Выбранные файлы:\n" + "\n".join(selected_files)
        messagebox.showinfo("Результаты выбора", result)
    else:
        messagebox.showinfo("Информация", "Файлы не выбраны.")

# Функция для запуска программы с графическим интерфейсом
def run_gui():
    root = tk.Tk()
    root.withdraw()  # Скрываем главное окно

    # Здесь вы можете указать путь к директории и расширения
    directory = 'path/to/your/directory'  # Замените на нужный путь
    extensions = ['txt', 'jpg', 'png']  # Замените на нужные расширения дописать пред. функцию чтобы она записывала расширение в список

    select_files_with_extensions(directory, extensions)

    root.mainloop()

# Запуск программы
run_gui()
   
       
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



