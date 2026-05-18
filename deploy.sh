#!/bin/bash
echo "=== Деплой KontPortal ==="
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo "=== Готово! Запускайте: gunicorn college_site.wsgi:application ==="
