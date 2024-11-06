import socket

# Словарь для соответствия фамилий и имен студентов
students = {
    "Бусыгин": "Георгий",
    "Беликов": "Алексей",
    "Сверчков": "Артём",
    "Мамелин": "Дмитрий",
    "Чумазин": "Глеб"
}

def start_server(host='localhost', port=12345):
    # Создаем сокет UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Сервер запущен на {host}:{port}")

        while True:
            # Ожидаем сообщение от клиента
            data, addr = server_socket.recvfrom(1024)
            print(f"Подключено к {addr}")

            # Запрашиваем фамилию у клиента
            server_socket.sendto("Введите вашу фамилию: ".encode('utf-8'), addr)
            surname, _ = server_socket.recvfrom(1024)
            surname = surname.decode('utf-8').strip()

            # Проверяем фамилию в словаре студентов
            if surname in students:
                response = f"Привет, {students[surname]}!".encode('utf-8')
            else:
                response = f"Ошибка: фамилия не найдена."

            # Отправляем ответ клиенту
            server_socket.sendto(response, addr)

if __name__ == "__main__":
    start_server()
