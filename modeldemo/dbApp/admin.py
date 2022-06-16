from django.contrib import admin
from dbApp.models import employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_details=['empNo','empName','empSalary','empAddress']
admin.site.register(employee,EmployeeAdmin)


