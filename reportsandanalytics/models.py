from django.db import models

# Create your models here.
from django.db import models

class Report(models.Model):
    REPORT_TYPES = (
        ('Patient_demographics', 'Patient Demographics'),
        ('Appointments', 'Appointments'),
        ('Revenue', 'Revenue'),
        ('Expenses', 'Expenses'),
    )

    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"{self.report_type} Report generated at {self.generated_at}"

