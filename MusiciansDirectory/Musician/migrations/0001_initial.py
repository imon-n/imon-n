# Generated by Django 5.0.2 on 2024-03-29 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('instrument_type', models.CharField(choices=[('Flute', 'Flute'), ('Violin', 'Violin'), ('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Other', 'Other')], max_length=20, verbose_name='Instrument Type')),
            ],
        ),
    ]