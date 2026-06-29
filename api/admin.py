from django.contrib import admin

# Register your models 

from api.models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location' , 'type')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email' , 'position')
    list_filter=('phone',)

admin.site.register(Company , CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)