# Generated by Django 5.0.1 on 2024-03-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='char_field',
            field=models.CharField(default='ka', max_length=255),
        ),
    ]
