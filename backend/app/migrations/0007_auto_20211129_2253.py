# Generated by Django 3.1.5 on 2021-11-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_card_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
