from django.db import models

class HourlyIntegratedLMP(models.Model):
  name = models.CharField(max_length=50, unique=True)
  LMP = models.DecimalField(max_digits=4,decimal_places=2)
  MCC = models.DecimalField(max_digits=4,decimal_places=2)
  MLC = models.DecimalField(max_digits=4,decimal_places=2)

class DayAheadLMP(models.Model):
  name = models.CharField(max_length=50, unique=True)
  LMP = models.DecimalField(max_digits=4,decimal_places=2)
  MCC = models.DecimalField(max_digits=4,decimal_places=2)
  MLC = models.DecimalField(max_digits=4,decimal_places=2)