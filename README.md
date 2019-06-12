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
3. Запускаем скрипт `./create_dirs_and_fix_perms.sh`
4. Запускаем `CHUBBYFOLIO_IS_STAGING=0 CHUBBYFOLIO_DOMAIN=example.com ./init-letsenctypt.sh` чтобы получить сертификат для сайта.
```
CHUBBYFOLIO_IS_STAGING - 1 чтобы протестировать конфигурацию и получить сертификат для проверки, 0 чтобы получить сертификат
CHUBBYFOLIO_DOMAIN - домен сайта без www
```

В дальнейшем сертификат будет обновляться сам.

## Обновление проекта

1. Стянуть изменения `git pull`
2. Если нужно пересобрать фронтент - удалите содержимое frontend/dist/ `rm -rf frontend/dist/*`
3. Собрать образ `docker-compose build`
4. Перезапустить образ `docker-compose up`
5. Или одной командой `docker-compose up --build`
