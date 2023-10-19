from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    group_number = models.IntegerField()
    last_name = models.CharField(max_length=255)
    prof_cum_ticket_number = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    telegram_id = models.BigIntegerField()
    user_name = models.CharField(max_length=255)
    current_query_id = models.BigIntegerField()

class Queries(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
