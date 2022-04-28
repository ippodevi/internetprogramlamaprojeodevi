from django.contrib import admin
from .models import Course
from import_export.admin import ImportExportModelAdmin

@admin.register(Course)

class examData(ImportExportModelAdmin):
    pass

# Register your models here.
