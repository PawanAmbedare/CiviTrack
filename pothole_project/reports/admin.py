from django.contrib import admin
from .models import PotholeReport

@admin.register(PotholeReport)
class PotholeReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'status', 'created_at')
    list_filter = ('severity', 'status')
    search_fields = ('title', 'description')
