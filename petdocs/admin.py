from django.contrib import admin

from .models import *

admin.site.register(
    (Owner)
)

class RegistrationAdmin(admin.ModelAdmin):
    exclude = ["reg_num"]