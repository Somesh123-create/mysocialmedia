from django.contrib import admin
from .models import Groups, GroupMember
# Register your models here.


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('groups_name',)}

admin.site.register(Groups, GroupAdmin)

admin.site.register(GroupMember)
