from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def comma_separated_validator(value):
    if not all(item.strip().isdigit() for item in value.split(',')):
        raise ValidationError('All values in the comma-separated list must be integers.')

class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255,default="ka")
    comma_separated_field = models.CharField(
        validators=[comma_separated_validator],
        max_length=255 , default=[1,2,3]
    )
    # date_time_field = models.DateTimeField(default=)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    # duration_field = models.DurationField()
    email_field = models.EmailField(default='im@gmail.com')
    float_field = models.FloatField(default='4.4')
    integer_field = models.IntegerField(default=345)
    positive_big_integer_field = models.PositiveBigIntegerField(default=4567)
    text_field = models.TextField(default='txt')
    time_field = models.TimeField(default='2:30')

    def __str__(self):
        return f"option {self.auto_field}"
    