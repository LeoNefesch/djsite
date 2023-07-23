# Проект djsite
### О чём проект?
Перед Вами учебный django-проект, построенный с применением архитектуры MVT. Содержит информацию об известных учёных.

**Стэк технологий:**
- Python 3.9
- django 4.0.5
- black
- Pillow
- django-debug-toolbar
- django-simple-captcha

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:LeoNefesch/djsite.git
```

```
cd djsite
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source v venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать пользователя с правами администратора (логин и пароль запомните, эти данные ещё понадобятся):

```
python manage.py createsuperuser
```

Запустить тестовый сервер:

```
python3 manage.py runserver
```

В браузере по адресу `http://127.0.0.1:8000/admin/` авторизоваться по логину и паролю суперпользователя.
