# Generated by Django 5.0.1 on 2024-03-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_mymodel_decimal_field_mymodel_email_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='float_field',
            field=models.FloatField(default='4.4'),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='integer_field',
            field=models.IntegerField(default=345),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='positive_big_integer_field',
            field=models.PositiveBigIntegerField(default=4567),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='text_field',
            field=models.TextField(default='txt'),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='time_field',
            field=models.TimeField(default='2:30'),
        ),
    ]