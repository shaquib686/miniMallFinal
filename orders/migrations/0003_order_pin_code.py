# Generated by Django 3.2.9 on 2021-11-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211117_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pin_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]