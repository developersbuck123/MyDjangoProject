# Generated by Django 3.2.8 on 2021-11-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('rollNo', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]