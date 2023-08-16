from django.contrib import admin
from .models import ValueModel


class ValueModelAdmin(admin.ModelAdmin):
	readonly_fields = ('timestamp',)

admin.site.register(ValueModel,ValueModelAdmin)