from django.contrib import admin

from camsapp.models import Topic,Webpage, AccessRecord,UserProfileInfo,Faculty,Student

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(UserProfileInfo)
admin.site.register(Faculty)
admin.site.register(Student)
