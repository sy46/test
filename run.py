import os
import requests
import subprocess
import time
import shutil

def run_script(script_url):
    # Загружаем содержимое скрипта по его URL
    response = requests.get(script_url)
    
    # Сохраняем содержимое скрипта во временном файле
    temp_file_path = 'temp_script.py'
    with open(temp_file_path, 'wb') as f:
        f.write(response.content)
    
    # Запускаем скрипт
    subprocess.run(['python', temp_file_path], check=True)
    
    # Удаляем временный файл скрипта
    os.remove(temp_file_path)

if __name__ == "__main__":
    # Список прямых облачных ссылок на скрипты для запуска
    script_urls = [
        "https://raw.githubusercontent.com/sy46/test/main/download_world.py",
        "https://raw.githubusercontent.com/sy46/test/main/say_and_rungame.py",
        "https://raw.githubusercontent.com/sy46/test/main/download_shader.py",
        "https://raw.githubusercontent.com/sy46/test/main/download_rp.py"
    ]
    
    # Запускаем каждый скрипт по очереди
    for url in script_urls:
        run_script(url)
        
        # Пауза между запусками скриптов (например, 5 секунд)
        time.sleep(3)

    # Удаляем папку %appdata%\.minecraft\.1TEMP
    shutil.rmtree(os.path.join(os.getenv('APPDATA'), '.minecraft', '.1TEMP'))
