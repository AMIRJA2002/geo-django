from django.contrib import admin
from .models import Public


@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    list_display = ('ogc_fid', 'navahi', 'area', 'fid1', 'latlon', 'nahieid', 'name', 'population', 'objectid', 'unqid')