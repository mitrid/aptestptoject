# Тестовое задание для aviapages.com

Это проект Django, который позволяет пройти процесс аутенфикации через facebook.

Ваша задача состоит в том, чтобы добавить в существующий проект следующий функционал:

* Создать модель Post (id, title(charfield), content(textfield), created_at(datetimefield), author(foreignkey(user))) для записей пользователя.
* На страницу профиля (/profile) добавить форму для cоздания записей.
* На главной странице (/) добавить список всех записей (отображать только  title, created_at и author) от всех пользователей в хронологическом порядке
* При клике на заголовок записи - должна открываться страница этой записи со всей информацией, включая content.

Успехов!


## Установка проекта

* Клонировать проект 
* Установить python3
* Установить pip
* Установить virtualenv / virtualenvwrapper

```
cd aptestproject/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
* Перейти в браузере по адресу localhost:8000
