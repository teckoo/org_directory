__author__ = 'situ'

from django.contrib import admin

from directory.models import Organization,Group,Person


admin.site.register(Organization)
admin.site.register(Group)
admin.site.register(Person)
