from django.contrib import admin
from .models import Customer, Survey

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "customer_code")
    search_fields = ("name", "email", "customer_code")


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("customer", "comment", "approved", "created_at")
    list_filter = ("approved", "created_at")
    search_fields = ("customer__name", "comment")
    actions = ["approve_surveys"]

    def approve_surveys(self, request, queryset):
        queryset.update(approved=True)
    approve_surveys.short_description = "Approve selected surveys"
