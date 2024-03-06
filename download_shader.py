import os
import requests
import zipfile

def download_and_extract(url, extract_to):
    # Создаем папку, если ее нет
    os.makedirs(extract_to, exist_ok=True)
    
    # Получаем имя файла из URL
    filename = url.split('/')[-1]
    
    # Скачиваем файл
    r = requests.get(url)
    zip_file_path = os.path.join(extract_to, filename)
    with open(zip_file_path, 'wb') as f:
        f.write(r.content)
    
    # Распаковываем архив
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(os.getenv('APPDATA'), '.minecraft', 'shaderpacks'))
    
    # Удаляем архив после распаковки
    os.remove(zip_file_path)

if __name__ == "__main__":
    # Укажите ссылку на скачиваемый архив
    url = "https://raw.githubusercontent.com/sy46/test/main/shaders.zip"
    
    # Распаковываем в папку %appdata%\.minecraft\shaderpacks
    download_and_extract(url, os.path.join(os.getenv('APPDATA'), '.minecraft', 'shaderpacks'))
