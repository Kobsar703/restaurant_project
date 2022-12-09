from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Ingredient, DishType, Dish, Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + ((("Additional info",), {"fields": ("years_of_experience",)}),)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type"]
    list_filter = ["price"]
    search_fields = ["name"]


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name"]