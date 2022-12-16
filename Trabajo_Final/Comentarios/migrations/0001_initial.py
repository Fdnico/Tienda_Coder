# Generated by Django 4.1.2 on 2022-12-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30)),
                ('imagen', models.ImageField(blank='True', null='True', upload_to='imagen_periferico')),
                ('comentario', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
