# Generated by Django 2.0.3 on 2018-04-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180402_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(blank=True, help_text='Preencha com DDD e o número (sem símbolos especiais)', null=True, verbose_name='Telefone'),
        ),
    ]
