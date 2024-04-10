from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'TaskModel'  # Specify the correct table name here

