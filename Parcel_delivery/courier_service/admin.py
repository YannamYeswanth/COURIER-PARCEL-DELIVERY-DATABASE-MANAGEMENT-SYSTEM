from django.contrib import admin
from courier_service.models import user_details,Branches,Department,Employees,Orders
# Register your models here.
admin.site.register(user_details)
admin.site.register(Branches)
admin.site.register(Department)
admin.site.register(Employees)
admin.site.register(Orders)
