# Generated by Django 3.1.2 on 2021-01-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20210124_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(),
        ),
    ]
