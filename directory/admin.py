__author__ = 'situ'

from django.contrib import admin

from directory.models import Organization,Group,Person, Directory


admin.site.register(Organization)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Directory)
