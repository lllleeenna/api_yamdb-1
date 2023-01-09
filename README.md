## Проект «CRUD для YaMDb»
Проект YaMDb собирает отзывы пользователей на произведения. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:LeschikovaTatyana/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

```
cd api_yamdb
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Заполнение базы данных контентом с использованием manage.py
В папке /static/data/ находятся csv файлы с тестовыми данными для проекта YaMDb.

Для заполнения пустой БД введите команду:
```
python manage.py create_reviews
```

Для заполнения одной таблицы, используйте аргумент -t(--table)
Команда:
```
python manage.py create_reviews --table category
```
заполнить тестовыми данными таблицу category.

Если ваша БД содержит тестовые данные и вы действительно хотите их перезаписать
используйте аргумент --overwrite:
```
python manage.py create_reviews --overwrite
```

Для перезаписи данных одной таблицы используйтет команду:
```
python manage.py create_reviews --overwrite --table name_table
```
