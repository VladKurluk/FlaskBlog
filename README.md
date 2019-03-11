# Первый блог на Flask

main.py - это точка входа в Flask приложение;

Активация виртульной среды.
В корне проекта выполнить команду:
* source venv/bin/activate

Запуск проекта в терминале:
* export FLASK_APP=main.py
* export FLASK_DEBUG=1
* flask run

Папка templates зарезирвированая для Flask, Flask знает что в ней храняться шаблоны.

Файл manage.py - отвечает за управление миграциями базы данных

В папке приложения, в моем случае app.

Команда "python manage.py db init" создаст папку migrations где будут храниться миграции.

Команда "python manage.py db migrate" - создает файл миграции

Команда "python manage.py db upgrade" - обновлят базу данных в соответствии миграции.

