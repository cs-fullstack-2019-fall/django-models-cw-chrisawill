# Generated by Django 2.2 on 2019-09-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Breed', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
            ],
        ),
    ]
