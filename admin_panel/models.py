from django.db import models


# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(verbose_name="Телеграмм ID", primary_key=True)
    username = models.CharField(verbose_name="Имя пользователя", max_length=255)

    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)

    group_number = models.CharField(verbose_name="Номер группы", max_length=10)
    ticket_number = models.CharField(verbose_name="Номер профкома", max_length=255)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    # def __str__(self) -> str:
    #     return str(self.id)



class Query(models.Model):
    text = models.CharField(verbose_name="Текст", max_length=255)
    type = models.CharField(verbose_name="Тип", max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class WorkingDay(models.Model):
    DAYS_OF_WEEK_CHOICES = (
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    )

    OFFICES_ADDRESS_CHOISES = (
        (1, 'Большая морская 67'),
        (2, 'Ленсовета 14'),
        (3, 'Гастелло 14'),
    )

    day_of_week = models.CharField(
        verbose_name='День недели',
        max_length=9,
        choices=DAYS_OF_WEEK_CHOICES,
        default='monday',
    )

    office = models.IntegerField(
        verbose_name='Адрес профкома',
        max_length=40,
        choices=OFFICES_ADDRESS_CHOISES,
        default=1
    )

    start_time = models.TimeField(verbose_name='Начало работы')
    close_time = models.TimeField(verbose_name='Конец работы')

    class Meta:
        verbose_name = 'Рабочий день'
        verbose_name_plural = 'Рабочие дни'
