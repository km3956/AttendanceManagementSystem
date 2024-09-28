from django.contrib import admin

# Register your models here.
from .models import TInformation
admin.site.register(TInformation)

from .models import TLogin
admin.site.register(TLogin)