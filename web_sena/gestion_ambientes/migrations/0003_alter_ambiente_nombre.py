# Generated by Django 4.0.6 on 2022-07-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_ambientes', '0002_alter_ambiente_aforo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
