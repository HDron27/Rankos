from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы")
    curator = models.CharField(max_length=100, verbose_name="Куратор")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название кружка")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кружок"
        verbose_name_plural = "Кружки"


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.IntegerField(verbose_name="Возраст")
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="students", verbose_name="Группа"
    )
    clubs = models.ManyToManyField(Club, blank=True, related_name="students", verbose_name="Кружки")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Profile(models.Model):
    from django.contrib.auth.models import User
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE,
        related_name='profile', verbose_name="Пользователь"
    )
    avatar = models.ImageField(
        upload_to='avatars/', null=True, blank=True, verbose_name="Фото профиля"
    )
    display_name = models.CharField(max_length=100, blank=True, verbose_name="Отображаемое имя")

    def __str__(self):
        return f"Профиль: {self.user.username}"

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return None

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
