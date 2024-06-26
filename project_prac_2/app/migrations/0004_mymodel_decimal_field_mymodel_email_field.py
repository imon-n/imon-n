# Generated by Django 5.0.1 on 2024-03-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mymodel_comma_separated_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='decimal_field',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='email_field',
            field=models.EmailField(default='im@gmail.com', max_length=254),
        ),
    ]
