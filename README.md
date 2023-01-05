## Проект «CRUD для Yatube»


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
### Заполнение базы данных контентом из приложенных csv-файлов. 
- Загрузите SQlite на ваше ПО:
https://sqlite.com/download.html
- Введите в терминале:
```
sqlite3
```
- Подключитесь к базе данных:
```
.open db.sqlite3
``` 
- Далее по очереди вводите команды для импорта:
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/category.csv reviews_category
``` 
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/genre.csv reviews_genre
``` 
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/titles.csv reviews_title
``` 
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/genre_title.csv reviews_genretitle
``` 
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/review.csv reviews_review
``` 
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/comments.csv reviews_comment
``` 
```
.import --csv --skip 1 C:/Dev/api_yamdb/api_yamdb/static/data/users.csv users_user
```
