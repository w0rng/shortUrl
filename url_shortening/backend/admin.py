from django.contrib import admin
import backend.models as models


@admin.register(models.Link)
class TimetableGroupAdmin(admin.ModelAdmin):
    list_display = ('long_link', 'short_link', 'number_clicks')