from django.contrib import admin
from .models import Teacher, Bia, Tsc,Placements,Course,MenuItem,Contact,Review

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_image')
    search_fields = ('name',)
    
admin.site.register(Teacher, TeacherAdmin)

class BiaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'year', 'batch_name', 'profile_image')
    search_fields = ('name', 'email', 'batch_name')
    list_filter = ('year',)

admin.site.register(Bia, BiaAdmin)

class TscAdmin(admin.ModelAdmin):
    list_display = ('name','profile_image', 'address', 'email', 'year', 'batch_name')
    search_fields = ('name', 'email', 'batch_name')
    list_filter = ('year',)

admin.site.register(Tsc, TscAdmin)




class PlacementsAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'company_name', 'package', 'email', 'batch_name', 'profile_image']
    search_fields = ['name', 'company_name', 'batch_name']
    list_filter = ['company_name', 'batch_name']
    
    
    

admin.site.register(Placements, PlacementsAdmin)    




class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Course, CourseAdmin)





class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('day', 'breakfast', 'lunch', 'tea', 'dinner')
    list_filter = ('day',)
    search_fields = ('day', 'breakfast', 'lunch', 'tea', 'dinner')
    ordering = ('day',)

admin.site.register(MenuItem, MenuItemAdmin)





class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'mobile', 'email', 'query', 'language') 
    search_fields = ('name', 'mobile', 'email') 

admin.site.register(Contact, ContactAdmin)






class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_message', 'review_date')
    search_fields = ('review_message', 'review_date')

admin.site.register(Review, ReviewAdmin)