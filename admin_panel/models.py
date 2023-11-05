from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name="Имя пользователя", max_length=255)

    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)

    group_number = models.CharField(verbose_name="Номер группы", max_length=10)
    ticket_number = models.CharField(verbose_name="Номер профкома", max_length=255)
    telegram_id = models.BigIntegerField(verbose_name="Телеграмм ID")

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self) -> str:
        return self.username



class Query(models.Model):
    text = models.CharField(verbose_name="Текст", max_length=255)
    type = models.CharField(verbose_name="Тип", max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'