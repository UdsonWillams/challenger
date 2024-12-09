from django.contrib import admin

# Register your models here.
from careers.models import Careers


class CareersAdmin(admin.ModelAdmin): ...


admin.site.register(Careers)
