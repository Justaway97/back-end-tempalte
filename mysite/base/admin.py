# login songming;songming

from django.contrib import admin

from base.models import TestModel, TestCode, TestTable

class TestModelAdmin(admin.ModelAdmin):
      list_display = [f.name for f in TestModel._meta.fields]
      
class TestCodeAdmin(admin.ModelAdmin):
      list_display = [f.name for f in TestCode._meta.fields]
      
class TestTableAdmin(admin.ModelAdmin):
      list_display = [f.name for f in TestTable._meta.fields]

# Register your models here.
admin.site.register(TestModel, TestModelAdmin)
admin.site.register(TestCode, TestCodeAdmin)
admin.site.register(TestTable, TestTableAdmin)


# real one start here

from base.models import BaseCode, BaseRole, BaseUser

# Register your models here.

class BaseRoleAdmin(admin.ModelAdmin):
      list_display = [f.name for f in BaseRole._meta.fields]
      
class BaseUserAdmin(admin.ModelAdmin):
      list_display = [f.name for f in BaseUser._meta.fields]
      
class BaseCodeAdmin(admin.ModelAdmin):
      list_display = [f.name for f in BaseCode._meta.fields]

# Register your models here.
admin.site.register(BaseRole, BaseRoleAdmin)
admin.site.register(BaseUser, BaseUserAdmin)
admin.site.register(BaseCode, BaseCodeAdmin)

from leave.models import Leave, LeaveSummary

class LeaveAdmin(admin.ModelAdmin):
      list_display = [f.name for f in Leave._meta.fields]
      
class LeaveSummaryAdmin(admin.ModelAdmin):
      list_display = [f.name for f in LeaveSummary._meta.fields]
      
# Register your models here.
admin.site.register(Leave, LeaveAdmin)
admin.site.register(LeaveSummary, LeaveSummaryAdmin)