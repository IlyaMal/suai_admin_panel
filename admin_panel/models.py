from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)

    username = models.CharField(max_length=255)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    group_number = models.IntegerField()
    ticket_number = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()
    current_query_id = models.BigIntegerField()

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



class Query(models.Model):
    id = models.BigIntegerField(primary_key=True)
     
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
