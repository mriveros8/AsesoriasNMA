from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Usuario

# Register your models here.

#admin.site.register(Cliente)
#admin.site.register(Profesional)
admin.site.register(Usuario)

#class ProfesionalInline(admin.StackedInline):
#    model = Profesional
#    can_delete: False
#    verbose_name_plural = 'profesional'

#class UserAdmin(BaseUserAdmin):
#    inlines = (ProfesionalInline,)

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)


