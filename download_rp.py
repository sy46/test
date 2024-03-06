import os
import requests
import shutil

def download_and_move(url, destination):
    # Создаем папку на рабочем столе, если ее нет
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    os.makedirs(desktop_path, exist_ok=True)
    
    # Получаем имя файла из URL
    filename = url.split('/')[-1]
    
    # Путь к файлу на рабочем столе
    file_path = os.path.join(desktop_path, filename)
    
    # Скачиваем файл
    r = requests.get(url)
    with open(file_path, 'wb') as f:
        f.write(r.content)
    
    # Перемещаем файл в директорию resourcepacks в %appdata%\.minecraft
    minecraft_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'resourcepacks')
    shutil.move(file_path, minecraft_path)
    
    # Получаем новый путь файла после перемещения
    new_file_path = os.path.join(minecraft_path, filename)
    new_file_path_renamed = os.path.join(minecraft_path, '§eУСТАНОВИ.zip')
    
    # Переименовываем файл
    os.rename(new_file_path, new_file_path_renamed)

if __name__ == "__main__":
    # Укажите ссылку на скачиваемый файл
    url = "https://raw.githubusercontent.com/sy46/test/main/%C2%A7e%D0%A3%D0%A1%D0%A2%D0%90%D0%9D%D0%9E%D0%92%D0%98.zip"
    
    # Вызываем функцию download_and_move
    download_and_move(url, '.temp')
