from django.contrib import admin
from .models import Department,Employee
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dname','d_location']
    ordering = ['id']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','ename','age','salary','email','address','dept']
    ordering = ['id']

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)