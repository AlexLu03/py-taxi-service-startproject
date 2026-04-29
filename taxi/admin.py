from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car


admin.site.register(Manufacturer)

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Добавляем license_number в список отображения
    list_display = ("license_number",)
    
    # Редактирование существующего пользователя
    fieldsets = (
        ("Additional info", {"fields": ("license_number",)}),
    )

    # Создание нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("license_number",)
        }),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)
