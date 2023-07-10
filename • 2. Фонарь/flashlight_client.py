import asyncio
import json


async def receive_commands(reader):
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            command = json.loads(data.decode('utf-8'))
            if 'command' in command:
                handle_command(command)

    except ConnectionError as e:
        print(f'Ошибка при получении данных от сервера: {str(e)}')


def handle_command(command):
    comm = command.get('command', None)
    if comm == 'ON':
        turn_on_lamp()
    elif comm == 'OFF':
        turn_off_lamp()
    elif comm == 'COLOR':
        color = command.get('metadata', 'Поле "metadata" с цветом не передано')
        change_color(color)


def turn_on_lamp():
    print('Фонарь включен')


def turn_off_lamp():
    print('Фонарь выключен')


def change_color(color):
    print(f'Фонарь изменяет цвет на {color}')


async def main():
    host = input("Введите хост (по умолчанию 127.0.0.1): ") or '127.0.0.1'
    port = int(input("Введите порт (по умолчанию 9999): ") or 9999)

    reader, _ = await asyncio.open_connection(host, port)
    print('Подключено к серверу фонаря')

    await receive_commands(reader)


if __name__ == '__main__':
    asyncio.run(main())
