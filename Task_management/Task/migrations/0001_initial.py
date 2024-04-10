# Generated by Django 5.0.1 on 2024-04-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'TaskModel',
            },
        ),
    ]
