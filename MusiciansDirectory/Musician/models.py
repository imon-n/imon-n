from django.db import models

class MusicianModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    INSTRUMENT_CHOICES = [
        ('Flute', 'Flute'),
        ('Violin', 'Violin'),
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Other', 'Other'),
    ]
    instrument_type = models.CharField(max_length=20 , choices=INSTRUMENT_CHOICES, verbose_name='Instrument Type')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
