import http.client

def fetch_page(url):
    # Разделяем URL на компоненты
    host = url.split("//")[1].split("/")[0]
    path = "/" + "/".join(url.split("//")[1].split("/")[1:])
import http.client

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

        # Читаем и выводим содержимое страницы
        page_content = response.read()
        print(page_content.decode('utf-8'))
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрываем соединение
        conn.close()

if __name__ == "__main__":
    url = "http://rokot.ibst.psu/anatoly/"
    fetch_page(url)
    # Создаем HTTP соединение
    conn = http.client.HTTPConnection(host)

    try:
        # Отправляем GET запрос
        conn.request("GET", path)
        
        # Получаем ответ
        response = conn.getresponse()
        
        # Проверяем статус ответа
        print(f"Статус: {response.status} {response.reason}")

        # Читаем и выводим содержимое страницы
        page_content = response.read()
        print(page_content.decode('utf-8'))
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    finally:
        # Закрываем соединение
        conn.close()

if __name__ == "__main__":
    url = "http://rokot.ibst.psu/anatoly/"
    fetch_page(url)
