from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import Company, Shipment

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name_plural = 'companies'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CompanyInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Shipment)
admin.site.register(Company)