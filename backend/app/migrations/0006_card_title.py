# Generated by Django 3.1.5 on 2021-11-29 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211116_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]