import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_site.settings')

import django
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@mail.com', 'admin123')
    print("Админ создан!")
else:
    u = User.objects.get(username='admin')
    u.set_password('admin123')
    u.save()
    print("Пароль сброшен!")