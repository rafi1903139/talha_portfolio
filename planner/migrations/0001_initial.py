# Generated by Django 5.0 on 2023-12-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('job_position', models.CharField(max_length=100)),
                ('work_field', models.CharField(max_length=100)),
                ('starting_date', models.DateField()),
                ('duration', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('achievement', models.TextField()),
                ('responsibilities', models.TextField()),
                ('organization_info', models.TextField()),
                ('skills', models.TextField()),
                ('training', models.TextField()),
                ('knowledge', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('event_type', models.CharField(max_length=100)),
                ('purpose', models.TextField()),
                ('organized_by', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
