from django.db import models

# Create your models here.

class Emergency(models.Model):
    patient_name = models.CharField(max_length=100)
    condition = models.TextField()
    triage_level = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency for {self.patient_name}"
