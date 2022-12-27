# nu-django-blog
nu-django-blog

#### Установка



 - Для работы сервиса необходимо поставить зависимости
```curl   
pip3 install -r requirements.txt
```

 - в iot_apartments создать файл .env c ключом:
```curl 
SECRET_KEY = 'django-insecure-1234567890'
 ```

 - сбросить все миграции:
```curl 
python manage.py migrate iotapp zero --fake
```
 - удалить файлы миграции в каталоге migrations:
```curl 
0001_initial.py и др. 000...
```
 - создать файлы миграции командой:
```curl 
python manage.py makemigrations
```
 - сделать миграции в базу командой:
```curl 
python manage.py migrate
```
 - создать суперпользователя:
```curl 
python manage.py createsuperuser
```
## Пример использования
Чтобы протестировать веб-сервис необходимо:
 - загрузить данные в базу:
```curl 
python manage.py fill_***
```
 - запустить сервер:
```curl 
python manage.py runserver
```
 - перейти по адресу и посмотреть данные через админку:
```curl 
http://127.0.0.1:8000/admin/
```
если порт забился:
```curl 
sudo fuser -k 8000/tcp
```
