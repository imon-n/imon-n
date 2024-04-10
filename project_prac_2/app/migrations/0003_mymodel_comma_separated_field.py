# Generated by Django 5.0.1 on 2024-03-26 12:11

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mymodel_char_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='comma_separated_field',
            field=models.CharField(default=[1, 2, 3], max_length=255, validators=[app.models.comma_separated_validator]),
        ),
    ]