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
2. Создаем файл `.env` (за основу берем файл env.example)
3. Запускаем скрипт `./create_dirs_and_fix_perms.sh` он создаст директории и выставит нужные права
4. Запускаем `./init-letsenctypt.sh DOMAIN EMAIL STAGING(1 или 0)` чтобы получить сертификат для сайта.

```
DOMAIN - домен сайта без www

EMAIL -  E-mail который будет использован при генерации сертификата

STAGING - 1 или 0
    1 чтобы протестировать конфигурацию и получить сертификат для проверки
    0 чтобы получить боевой сертификат
    
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

## Переменные окружения и sudo docker

При запуске docker с помощью sudo не будут переданы переменные окружения. Поэтому поднимать контейнеры нужно так:

```
sudo CHUBBYFOLIO_DOMAIN=example.com docker-compose up --build
```

## Создание учетной записи администратора

После старта контейнеров:

Заходим в django контейнер:
```
docker exec -it django_server bash
```
И создаем администратора:
```
python manage.py createsuperuser
``` 

## Local https (staging image)

1. Устанавливаем `mkcert`
2. Устанавливаем сертификаты в систему `mkcert -install` (понадобится перезапуск браузера)
3. Создаем сертификаты `mkcert foo.test`
4. Копируем их в `data/ssl/conf/live/foo.test/{fullchain.pem,privkey.pem}`
5. Создаем пустой файл в `data/ssl/conf/options-ssl-nginx.conf` 
6. Создаем ключ Диффи Хеллмана `openssl dhparam -out data/ssl/conf/ssl-dhparams.pem 2048`
7. Делаем запись в `/etc/hosts` `127.0.0.1 foo.test`
8. Не забываем задать в переменные среды домен

## Ссылки

1. [Инструкция по созданию "dockerized" веб приложения с использованием DRF и React](https://gist.github.com/genomics-geek/98929a9e7ba9602fed7bfa4a5a1c5c4e)
2. [Настройка Lets Encrypt + Nginx для Docker](https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)
3. [Миграция с vue-cli 2 на 3](https://medium.com/jinweijie/migrate-from-vue-cli-2-to-3-16f14e7febdc)
4. [Удаление контейнеров, образов и т.д.](https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/)
5. [Docker Compose Local HTTPS with nginx or Caddy and mkcert](https://codewithhugo.com/docker-compose-local-https/)
