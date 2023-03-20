from django.db import models


class EmployeeDetails(models.Model):
    """Employee Details Model"""

    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name