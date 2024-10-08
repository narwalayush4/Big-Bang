# Generated by Django 4.1.2 on 2022-11-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('year', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('star_cast', models.CharField(max_length=255)),
            ],
        ),
    ]
