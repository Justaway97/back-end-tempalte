from django.db import models
from base.share.models import BaseModel
# Create your models here.

# if not able to generate table can follow here https://www.pythonanywhere.com/forums/topic/15000/

class TestModel(BaseModel):
    test_options = models.TextField(blank=True, null=True)
    auto_complete = models.CharField(max_length=200, blank=True, null=True)
    button_toggle = models.CharField(max_length=200, blank=True, null=True)
    checkbox = models.TextField(blank=True, null=True)
    date_picker= models.DateTimeField(null=True, blank=True)
    multi_auto_complete = models.TextField(blank=True, null=True)
    input = models.CharField(max_length=200, blank=True, null=True)
    radio = models.CharField(max_length=200, blank=True, null=True)

class TestCode(BaseModel):
    code_description = models.CharField(max_length=200)
    code_type = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)

class TestTable(BaseModel):
    checkbox = models.IntegerField(default=0)
    input = models.CharField(max_length=200, blank=True, null=True)
    auto_complete = models.CharField(max_length=200, blank=True, null=True)
    button_toggle = models.CharField(max_length=200, blank=True, null=True)
    multi_auto_complete = models.TextField(blank=True, null=True)
    date_picker = models.DateTimeField(null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    symbol = models.CharField(max_length=200, blank=True, null=True)
