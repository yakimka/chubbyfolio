# Chubbyfolio

## Что это?

Chubbyfolio это сайт-визитка для фотографов.

Проект создан с использованием технологий:
* Python 3.6
* Django >=2
* Django Rest Framework
* Vuejs

##  Первый запуск

1. Клонируем репозиторий на сервер
2. Создаем файлы `.env` и `frontend/.env` (за основу берем файлы env.example)
3. Запускаем скрипт `./create_dirs_and_fix_perms.sh` он создаст директории и выставит нужные права
4. Запускаем `CHUBBYFOLIO_IS_STAGING=0 CHUBBYFOLIO_DOMAIN=example.com ./init-letsenctypt.sh` чтобы получить сертификат для сайта.
```
CHUBBYFOLIO_IS_STAGING - 1 или 0
    1 чтобы протестировать конфигурацию и получить сертификат для проверки
    0 чтобы получить боевой сертификат
    
CHUBBYFOLIO_DOMAIN - домен сайта без www
```

В дальнейшем сертификат будет обновляться сам.

## Обновление проекта

1. Стянуть изменения `git pull`
2. Если нужно пересобрать фронтент - удалите содержимое frontend/dist/ `rm -rf frontend/dist/*`
3. Пересобрать образ и запустить:
    - Собрать образ `docker-compose build`
    - Перезапустить образ `docker-compose up`
    
    или одной командой:
    
    - `docker-compose up --build`

## Google Analytics, robots.txt, etc.

Если положить в директорию `frontend/additional_prod_files/static_root` файлы, то при сборке бандла все они будут скопированы в `dist`.
Тоесть это можно использовать для `robots.txt`, файлов подтверждения владения доменом и т.д.

Также, если создать файл `frontend/additional_prod_files/head_content.html` и поместить в него html - содержимое файла будет вставлено в низ секции head сайта. Это удобно использовать для google analytics и подобного.

## Ссылки

1. [Инструкция по созданию "dockerized" веб приложения с использованием DRF и React](https://gist.github.com/genomics-geek/98929a9e7ba9602fed7bfa4a5a1c5c4e)
2. [Настройка Lets Encrypt + Nginx для Docker](https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)

