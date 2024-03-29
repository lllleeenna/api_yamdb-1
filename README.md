## Групповой проект «API для YaMDb»
Проект YaMDb собирает отзывы пользователей на произведения. 
Произведения делятся на категории. Произведению может быть присвоен жанр.
Добавлять произведения, категории и жанры может только администратор.
Пользователи оставляют к произведениям текстовые отзывы и ставят оценку
в диапазоне от 1 до 10. Из оценок пользователей формируется рейтинг - усредненная
оценка произведений. Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные
пользователи.

### Технологии:
- Python 3.9
- Django 3.2
- djangorestframework 3.12.4

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:lllleeenna/api_yamdb-1.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

```
source venv/bin/activate
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

Описание эндпойнтов доступно по ссылке: http://172.0.0.1:8000/redoc/

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
заполнит тестовыми данными таблицу category.

Если ваша БД содержит тестовые данные и вы действительно хотите их перезаписать
используйте аргумент --overwrite:
```
python manage.py create_reviews --overwrite
```

Для перезаписи данных одной таблицы используйтет команду:
```
python manage.py create_reviews --overwrite --table name_table
```
### Авторы:
1. Лещикова Татьяна (https://github.com/LeschikovaTatyana)
2. Дивногорская Ольга (https://github.com/OlyaDiv)
3. Смурова Елена (https://github.com/lllleeenna)
