# Generated by Django 4.0.6 on 2022-07-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_horarios', '0003_alter_competencia_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
