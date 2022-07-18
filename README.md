# yamdb_final
![Django-app workflow](https://github.com/Listener430/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Описание/Автор
Калмыкова Надежда
API для проекта Yatube c Django-app workflow

Функционал:
* Просмотр, создание, удаление и редактирование постов
* Подписка на пользователей
* Просмотр групп
* Просмотр, создание, удаление и редактирование комментариев

Workflow:
* автоматический запуск тестов
* обновление образов на Docker Hub
* автоматический деплой на боевой сервер при пуше в главную ветку main

### Запуск контейнера Docker

Если у вас Windows10 ставьте версию Docker Desktop 4.8.1 (более поздние не работают)
команда как проверить версию Docker Desktop в терминале Ubuntu
powershell.exe 'Get-ItemPropertyValue "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\Docker Desktop" DisplayVersion'

### Устанвка Docker-Compose на серевер в Яндекс-облако (версия 1.29.2 compatible)
sudo su
sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
проверка:
docker-compose --version



# Установка локально

Клонируйте репозиторий и перейдите в него в командной строке:
$ git clone git@github.com:Listener430/infra_sp2.git

Перейдите в директорию с файлом docker-compose.yaml и запустите сборку:
$ cd infra
и
$ docker-compose up -d --build

Выполните миграции в проекте:
$ docker-compose exec web python manage.py migrate

Создайте суперпользователя:
$ docker-compose exec web python manage.py createsuperuser

Соберите статику:
$ docker-compose exec web python manage.py collectstatic --no-input

Создайте дамп (резервную копию) базы данных:
$ docker-compose exec web python manage.py dumpdata > fixtures.json


# Установка на сервере
запустите workflow
перейдите на адрес 84.201.140.144/admin
или 84.201.140.144/redoc


# Документация - если развернут локально:

Для просмотра документации перейдите по адресу:
http://localhost/redoc/

# Примеры запросов

**GET**: http://localhost/api/v1/categories/  
Пример ответа:
json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]

**POST**: http://localhost/api/v1/categories/  
Тело запроса:
json
{
  "name": "string",
  "slug": "string"
}
Пример ответа:
json
{
  "name": "string",
  "slug": "string"
}

**GET**: http://localhost/api/v1/users/  
Пример ответа:
json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
