# Generated by Django 4.0.4 on 2022-05-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenmodels',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
