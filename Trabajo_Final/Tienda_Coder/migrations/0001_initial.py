# Generated by Django 4.1.2 on 2022-12-07 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Perifericos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
