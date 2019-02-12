from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

# Для создания миграций БД
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

# Создание миграции
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

