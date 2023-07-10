import json
import asyncio


async def send_command_to_client(client_writer):
    command = {'command': 'ON'}
    await send_command(client_writer, command)
    command = {'command': 'COLOR', 'metadata': 'red'}
    await send_command(client_writer, command)
    command = {'command': 'COLOR', 'metadatas': 'yellow'}
    await send_command(client_writer, command)
    command = {'command': 'asdf'}
    await send_command(client_writer, command)
    command = {'command': 'COLOR'}
    await send_command(client_writer, command)
    command = {'comm': 'COLOR'}
    await send_command(client_writer, command)
    command = {'command': 'OFF'}
    await send_command(client_writer, command)


async def send_command(client_writer, command):
    await asyncio.sleep(1)
    data = json.dumps(command).encode('utf-8')
    client_writer.write(data)
    await client_writer.drain()


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Установлено соединение с клиентом: {addr[0]}:{addr[1]}')
    await send_command_to_client(writer)
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            # Обработка команды от клиента (в данном случае не используется)
            command = json.loads(data.decode('utf-8'))
            print(f'Получена команда от клиента: {command}')

    except ConnectionError as e:
        print(f'Ошибка при получении данных от клиента: {str(e)}')
    finally:
        writer.close()
        print(f'Соединение с клиентом {addr[0]}:{addr[1]} закрыто')


async def main():
    host = '127.0.0.1'
    port = 9999

    server = await asyncio.start_server(handle_client, host, port)
    print(f'Сервер фонаря запущен на {host}:{port}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())

