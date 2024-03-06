import os
import requests
import shutil
import time

def create_temp_folder():
    # Получаем путь к папке .1TEMP в папке .minecraft
    minecraft_temp_path = os.path.join(os.getenv('APPDATA'), '.minecraft', '.1TEMP')
    
    # Создаем папку .1TEMP, если ее нет
    os.makedirs(minecraft_temp_path, exist_ok=True)
    
    return minecraft_temp_path

def download_and_extract(url, extract_to):
    # Создаем папку .1TEMP в .minecraft, если ее нет
    temp_folder_path = create_temp_folder()
    
    # Скачиваем архив
    r = requests.get(url)
    zip_file_path = os.path.join(temp_folder_path, os.path.basename(url))
    with open(zip_file_path, 'wb') as f:
        f.write(r.content)
    
    # Проверяем наличие 7-Zip на компьютере
    if os.system("7z") != 0:
        print("Ошибка: 7-Zip не найден. Пожалуйста, установите 7-Zip и добавьте его в переменную среды PATH.")
        return
    
    # Распаковываем архив
    os.system(f"7z x {zip_file_path} -o{temp_folder_path}")
    
    # Если архив world_part_2, перемещаем только необходимые файлы в папку .minecraft/saves/моей малышке/region
    if "world_part_2" in url:
        # Получаем путь к папке с распакованным содержимым второго архива
        extracted_files = [file for file in os.listdir(temp_folder_path) if file.endswith('.mca')]
        
        # Получаем путь к папке ".minecraft/saves/моей малышке/region"
        final_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'saves', 'моей малышке', 'region')
        
        # Перемещаем необходимые файлы в нужную папку
        for file in extracted_files:
            shutil.move(os.path.join(temp_folder_path, file), final_path)
    else:
        # Получаем путь к папке с распакованным содержимым
        extracted_folder = os.path.join(temp_folder_path, 'моей малышке')
        
        # Получаем путь к папке ".minecraft/saves"
        final_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'saves')
        
        # Перемещаем папку в ".minecraft/saves"
        shutil.move(extracted_folder, final_path)

if __name__ == "__main__":
    # Укажите ссылку на первый архив
    url1 = "https://raw.githubusercontent.com/sy46/test/main/world_part1.7z"
    # Укажите ссылку на второй архив
    url2 = "https://raw.githubusercontent.com/sy46/test/main/world_part_2.7z"
    
    # Запускаем функцию download_and_extract для первого архива
    download_and_extract(url1, '.temp')
    
    # Ждем 2 секунды
    time.sleep(2)
    
    # Запускаем функцию download_and_extract для второго архива
    download_and_extract(url2, '.temp')
    
    print("-----------------------------------SUCCESS")
    
    # Ждем еще 3 секунды
    time.sleep(3)
    
    # Очищаем содержимое папки .1TEMP
    temp_folder_path = create_temp_folder()
    for filename in os.listdir(temp_folder_path):
        file_path = os.path.join(temp_folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Ошибка при удалении {file_path}: {e}")
