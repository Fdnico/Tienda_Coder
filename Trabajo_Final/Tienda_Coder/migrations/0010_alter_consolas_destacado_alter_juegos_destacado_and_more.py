# Generated by Django 4.1.2 on 2022-12-18 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda_Coder', '0009_consolas_destacado_juegos_destacado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consolas',
            name='destacado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='juegos',
            name='destacado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='perifericos',
            name='destacado',
            field=models.IntegerField(),
        ),
    ]