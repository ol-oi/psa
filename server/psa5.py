import http.client
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

def fetch_page(url):
    # Разделяем URL на компоненты
    host = url.split("//")[1].split("/")[0]
    path = "/" + "/".join(url.split("//")[1].split("/")[1:])

    # Создаем HTTP соединение
    conn = http.client.HTTPConnection(host)

    try:
        # Отправляем GET запрос
        conn.request("GET", path)
        
        # Получаем ответ
        response = conn.getresponse()
        
        # Проверяем статус ответа
        print(f"Статус: {response.status} {response.reason}")

        # Читаем содержимое страницы
        page_content = response.read().decode('utf-8')
        
        # Парсим HTML с помощью BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')

        # Находим все теги <img>
        img_tags = soup.find_all('img')
        
        # Создаем папку для сохранения изображений
        os.makedirs('images', exist_ok=True)

        for img in img_tags:
            img_url = urljoin(url, img.get('src'))
            download_image(img_url)

        # Находим все теги <a> для перехода по ссылкам
        links = soup.find_all('a', href=True)
        for link in links:
            link_url = urljoin(url, link['href'])
            fetch_page(link_url)  # Рекурсивно вызываем функцию для каждой ссылки

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрываем соединение
        conn.close()

def download_image(img_url):
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            # Получаем имя файла из URL
            filename = os.path.join('images', img_url.split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Сохранено: {filename}")
        else:
            print(f"Не удалось загрузить изображение: {img_url} (статус: {response.status_code})")
    except Exception as e:
        print(f"Ошибка при загрузке изображения {img_url}: {e}")

if __name__ == "__main__":
    url = "http://rokot.ibst.psu/anatoly/"
    fetch_page(url)
