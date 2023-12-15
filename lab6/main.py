import subprocess

# Вказано місце для введення IP-адреси вашого iperf3-сервера
server_ip = 'localhost'  # Тут потрібно ввести IP-адресу вашого iperf3 сервера

def client(server_ip):
    """
    Підключення до iperf3 сервера і виконання відповідної команди.
    
    :param server_ip: Адреса сервера, до якого буде підключатися клієнт
    :return: Вивід команди та помилку, якщо вона виникла
    """
    try:
        # Виконуємо команду iperf3 для підключення до сервера.
        # Припускаючи, що команда "iperf3" є доступною в системі
        process = subprocess.Popen(['iperf3', '-c', server_ip],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output, error
    except Exception as e:
        # Повертаемо відповідь про помилку, якщо вона виникла
        return None, str(e)

def parser(output):
    """
    Парсинг виводу iperf3 для отримання необхідної інформації.
    
    :param output: Вивід з функції client
    :return: Список з обробленою інформацією про інтервали з iperf
    """
    # Тут має бути ваш парсер, який обробляє 'output' та формує результат
    # Цей приклад припускає, що результат має бути списком словників
    result_list = [
        # Для прикладу ми створюємо один елемент списку 
        {'Interval': '1.00-2.00', 'Transfer': 3.91, 'Bitrate': 32.8, 'Retr': 0.0, 'Cwnd': 320.0}
        # Ви маєте розробити логіку, що дістає подібну інформацію з 'output'
    ]
    return result_list

# Основна частина коду
output, error = client(server_ip)

if error:
    print('Виникла помилка:', error)
else:
    result_list = parser(output)
    # Виводимо тільки ті інтервали, де Transfer > 2 та Bitrate > 20
    for value in result_list:
        if value['Transfer'] > 2 and value['Bitrate'] > 20:
            print(value)
