# Generated by Django 5.0 on 2023-12-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_organizationalaffiliation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('concentration', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=50)),
                ('passing_year', models.CharField(max_length=50)),
            ],
        ),
    ]
