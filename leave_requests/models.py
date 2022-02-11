from datetime import date

import numpy as np

from django.db import models


LEAVE_CHOICES = [
    ('SICK', 'sick leave'),
    ('NORMAL', 'normal leave'),
]

class User(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    leave_type = models.CharField(max_length=10, choices=LEAVE_CHOICES, default='NORMAL')
    start_date = models.DateField('leave start date', default=date.today)
    end_date = models.DateField('leave end date')
    created_at = models.DateTimeField(auto_now=True)

    @property
    def leave_days(self):
        """
        return the total number of leave days less weekends
        """
        leave_days = np.busday_count(self.start_date, self.end_date)
        return leave_days


