from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name="id")
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    group_number = models.IntegerField(verbose_name="Номер группы")
    ticket_number = models.BigIntegerField(verbose_name="Номер проф. билета")
    state = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField(verbose_name="Telegram id")

class Queries(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name="id")
    text = models.CharField(verbose_name="Сообщение", max_length=255)
    type = models.CharField(max_length=255)
    user_id_id = models.CharField(max_length=255)
