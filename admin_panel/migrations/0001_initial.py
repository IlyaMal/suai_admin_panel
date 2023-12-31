# Generated by Django 4.2.6 on 2023-11-05 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Телеграмм ID')),
                ('username', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('group_number', models.CharField(max_length=10, verbose_name='Номер группы')),
                ('ticket_number', models.CharField(max_length=255, verbose_name='Номер профкома')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('type', models.CharField(max_length=255, verbose_name='Тип')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.user')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]
