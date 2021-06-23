# Foodgram, Сайт рецептов
[![Actions Status](https://github.com/Galacticboreas/foodgram-project/actions/workflows/yamdb_workflow.yaml/badge.svg)](https://github.com/Galacticboreas/foodgram-project/actions/)

Проект Foodgram создан для хранения рецептов пользователей, созданных на основе списка ингредиентов. Каждый из рецептов имеет своё описание, в т.ч. время приготовления и рекомендуемое время употребления - завтрак, обед и ужин. Можно добавлять каждый из рецептов в список покупок и скачать полный список ингридиентов в удобном формате.

Посмотреть на работу проекта можно по этому адресу: http://www.galacticborey.ml:81

# Запуск проекта в dev-режиме

    миграции приложений docker-compose exec galacticboreas_web_1 python manage.py migrate --noinput

    создание администратора сайта docker-compose exec galacticboreas_web_1 python manage.py createsuperuser

    сбор статических данных docker-compose exec galacticboreas_web_1 python manage.py collectstatic --no-input

    заполнение базы постами пользователей docker-compose exec galacticboreas_web_1 python manage.py loaddata fixtures.json

Автор

Иванов Борис
fixing 1 2 3
