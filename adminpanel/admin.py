from django.contrib import admin

from .models import UserProfile,HomepageProject,WorkpageProject,ProjectFile,HomeProjectFile,BottomProject,BottomProjectFile,About

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(HomepageProject)
admin.site.register(WorkpageProject)
admin.site.register(ProjectFile)
admin.site.register(HomeProjectFile)
admin.site.register(BottomProject)
admin.site.register(BottomProjectFile)
admin.site.register(About)