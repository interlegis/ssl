# Generated by Django 2.0.3 on 2018-04-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(blank=True, help_text='Preencha com DDD e o número (sem símbolos especiais', null=True, verbose_name='Telefone'),
        ),
    ]
