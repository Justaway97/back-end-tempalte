
from mysite.share.models import BaseCode, BaseModel, User, BaseRole
from django.db import models

# Create your models here.
class LeaveSummary(BaseModel):
    username = models.CharField(max_length=200, blank=True, null=True)
    leave_type = models.CharField(max_length=200, blank=True, null=True)
    leave_balance = models.FloatField()

class Leave(BaseModel):
    username = models.CharField(max_length=200, blank=True, null=True)
    leave_type = models.CharField(max_length=200, blank=True, null=True)
    leave_date = models.DateTimeField(null=True, blank=True)
    leave_date_time = models.CharField(max_length=1, blank=True, null=True)
    approved_by = models.CharField(max_length=200, blank=True, null=True)
    approver = models.CharField(max_length=200, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    rejected_remark = models.TextField(blank=True, null=True)
