from django.contrib import admin
from silc.models import SILCGroup,Member

# Register your models here.
admin.site.register(SILCGroup)
admin.site.register(Member)