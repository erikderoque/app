# Generated by Django 3.1.2 on 2020-11-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('precio', models.CharField(max_length=50, verbose_name='Precio')),
                ('tipo_variedad', models.CharField(max_length=100, verbose_name='Tipo_variedad')),
                ('altura', models.CharField(max_length=50, verbose_name='Altura')),
            ],
        ),
    ]
