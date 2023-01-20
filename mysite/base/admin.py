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
