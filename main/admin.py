from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Contact)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
	list_display = ['title','id']
	list_display_links = ['title',]
	prepopulated_fields = {'slug':('title',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'category','id']
	list_display_links = ['title', ]
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Blog

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name', ]
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = Teacher