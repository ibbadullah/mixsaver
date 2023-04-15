from django.contrib import admin
from django.contrib.auth.models import Group

# Changing the django admin template admin title
admin.site.site_header = 'MixSaver Dashboard'



# Unregistering group model in the admin
admin.site.unregister(Group)
