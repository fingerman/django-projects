# Generated by Django 3.1.2 on 2020-12-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20201207_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(upload_to='pets/'),
        ),
    ]
