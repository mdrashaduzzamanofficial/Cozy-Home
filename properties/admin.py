from django.contrib import admin
from .models import Property, Application, Lease, Payment, UserPreference

admin.site.register(Property)
admin.site.register(Application)
admin.site.register(Lease)
admin.site.register(Payment)
admin.site.register(UserPreference)