# Generated by Django 3.1.4 on 2020-12-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201212_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task1',
            new_name='Задание 1',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task2',
            new_name='Задание 2',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task4',
            new_name='Задание 4',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task5',
            new_name='Задание 5',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='subject',
            new_name='Предмет',
        ),
    ]