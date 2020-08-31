from django.contrib import admin
from .models import Auto, AutoKind, AutoMark, Zayavka, AccountingCars


# Register your models here.
admin.site.register(Auto)
admin.site.register(AutoMark)
admin.site.register(AutoKind)
admin.site.register(Zayavka)
admin.site.register(AccountingCars)
