# Generated by Django 4.1 on 2022-09-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mundial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecciones',
            name='palmares',
            field=models.CharField(max_length=50),
        ),
    ]
