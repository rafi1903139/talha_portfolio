# Generated by Django 5.0 on 2023-12-22 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0007_areaofexpertise_expertiseitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('working_knowledge', models.TextField(null=True)),
                ('software_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='software_names', to='planner.softwareskill')),
            ],
        ),
    ]
