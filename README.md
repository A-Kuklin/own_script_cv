# Тестовое задание для Own Script

## • 1. Проектирование БД
Решение задачи, описанной в файле `«ТЗ проектирование БД (1)(5)(2).docx»`.<br>
Первая часть — файл `«Схема БД.md»`.<br>
Вторая часть — файл `«SQL запросы.sql»`.<br>

## • 2. Фонарь
Решение задачи, описанной в файле `«фонарик-1.pdf»`.<br>

`test_server.py` — тестовый сервер, который отправляет команды клиенту. Нужен только для тестирования клиента, по условию сервер недоступен.<br>

`flashlight_client.py` — клиент «фонарь».<br>
Подразумевает только `json` формат команд на чтение, если передать, например, строку, число или другой непредусмотренный формат, будет вызвана ошибка.

Для локального тестирования запускается тестовый сервер, потом клиент с хостом и портом по умолчанию. 

Используются только встроенные библиотеки (Python 3.10).