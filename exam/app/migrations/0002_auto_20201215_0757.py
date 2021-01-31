# Generated by Django 3.1.4 on 2020-12-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default='low', max_length=8),
        ),
    ]
