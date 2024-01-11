from django.contrib import admin
from .models import Area, TehranArea, Public


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'geo_fance')


@admin.register(TehranArea)
class TehranAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'population', 'navahi', 'section', 'zone')


@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    list_display = ('ogc_fid', 'navahi', 'area', 'fid1', 'latlon', 'nahieid', 'name', 'population', 'objectid', 'unqid')