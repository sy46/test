import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import time

def find_tl_exe():
    # Получаем путь к директории %appdata%
    appdata_path = os.getenv('APPDATA')
    
    # Проходимся по всем папкам и подпапкам в директории %appdata%
    for root, dirs, files in os.walk(appdata_path):
        for file in files:
            # Проверяем, является ли текущий файл TL.exe
            if file.lower() == "tl.exe":
                return os.path.join(root, file)
    
    return None

def run_tl_exe():
    # Ищем файл TL.exe
    tl_exe_path = find_tl_exe()
    
    # Проверяем, найден ли файл
    if tl_exe_path:
        # Запускаем TL.exe
        time.sleep(3)
        subprocess.run(tl_exe_path)
    else:
        print("Ошибка: Файл TL.exe не найден.")

def show_message_box():
    # Создаем главное окно
    root = tk.Tk()
    root.withdraw()  # Прячем главное окно
    
    # Отображаем диалоговое окно с новым сообщением через 7 секунд после запуска TL.exe
    time.sleep(8)
    messagebox.showinfo("♡", "привет, солнце\nзапускай игру на версии 1.20.1 и заходи в одиночку\nтам тебя уже ждет сюрприз\nлюблю ♡\nэто можно закрыть")

if __name__ == "__main__":
    run_tl_exe()
    show_message_box()