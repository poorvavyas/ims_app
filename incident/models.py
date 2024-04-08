from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices
from datetime import datetime
from .managers import IncidentQuerySet
# Create your models here.
PRIORITY = Choices(('H', 'HIGH'),('M', 'MEDIUM'), ('L', 'LOW'))
INCIDENT_STATUS = Choices(('O', 'OPEN'),('P', 'IN PROGRESS'), ('C', 'CLOSED'))


class Incident(models.Model):
    incident_id = models.CharField(max_length=12, unique=True)
    reporter_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    incident_detail = models.CharField(max_length=5000, null=True, blank=True)
    priority = models.CharField(choices=PRIORITY, default=PRIORITY.L, max_length=6)
    incident_status = models.CharField(choices=INCIDENT_STATUS, default=INCIDENT_STATUS.O, max_length=15)
    report_date = models.DateTimeField(default=datetime.now, blank=True)

    objects = IncidentQuerySet.as_manager()
