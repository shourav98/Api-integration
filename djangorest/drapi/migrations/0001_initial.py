# Generated by Django 4.2.7 on 2023-11-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=20)),
                ('course_duration', models.IntegerField()),
                ('seat', models.IntegerField()),
            ],
        ),
    ]
