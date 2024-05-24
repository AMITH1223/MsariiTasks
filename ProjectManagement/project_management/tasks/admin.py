from django.contrib import admin
from .models import Task,UserData,StudyGroup,CommunityForum

admin.site.register(Task)
admin.site.register(UserData)
admin.site.register(StudyGroup)
admin.site.register(CommunityForum)