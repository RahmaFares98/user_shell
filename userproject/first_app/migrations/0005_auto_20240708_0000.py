# Generated by Django 2.2.4 on 2024-07-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=25),
        ),
    ]
