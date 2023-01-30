from django.db import models
from datetime import datetime
import uuid
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=200)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=200, blank=True)
    is_deleted = models.CharField(max_length=1, default=0)

    def soft_delete(self):
        self.deleted_at = datetime.utcnow()
        self.isdeleted = True
        self.save()

    def deserialize(self):
        fields = [f.name for f in self._meta.fields]
        result = {}
        for f in fields:
            result[f] = getattr(self, f)
        return result

    def update(self, newValue):
        fields = [f.name for f in self._meta.fields]
        for f in fields:
            if f != 'uuid' and f in newValue:
                setattr(self, f, newValue[f])
        self.save()

    def saveNew(self, newValue):
        fields = [f.name for f in self._meta.fields]
        for f in fields:
            if f != 'uuid' and f in newValue:
                setattr(self, f, newValue[f])
        self.save()

class BaseCode(BaseModel):
    class Meta:
        abstract = True

    app = models.CharField(max_length=200)
    code_description = models.CharField(max_length=200)
    code_type = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True)

class BaseRole(BaseModel):
    class Meta:
        abstract = True

    app = models.CharField(max_length=200)
    role_description = models.CharField(max_length=200)
    role_type = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)

class User(BaseModel):
    class Meta:
        abstract = True
    username = models.CharField(max_length=200)
    role_type = models.CharField(max_length=200, blank=True, null=True)