from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	name = models.CharField('Nomi',max_length=150,)
	slug = models.SlugField('*',max_length=150, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('main:category_detail', kwargs={'category_slug':self.slug})


class Author(models.Model):
	name = models.CharField('Nomi',max_length=150,)
	slug = models.SlugField('*',max_length=150, unique=True)

	def __str__(self):
		return self.name



class Contact(models.Model):
	name = models.CharField('Toliq Ismingiz',max_length=50)
	tel = models.CharField('Tel',max_length=50)
	message = models.TextField('Xabar',max_length=500)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contactlar'




class Blog(models.Model):
	title = models.CharField('Title',max_length=50,unique=True)
	slug = models.SlugField('*',max_length=50,unique=True)

	category = models.ForeignKey(Category,
		on_delete=models.CASCADE,
		related_name='posts')
	image = models.ImageField('Rasmi', upload_to='post_images/')
	author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author')
	date = models.DateTimeField(auto_now_add=True)
	body = models.TextField('Text')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('main:blog_detail', kwargs={'blog_slug':self.slug})





class Cours(models.Model):
	title = models.CharField('Nomi',max_length=50,)
	muddat = models.CharField("O'qish muddati", max_length=50)
	body = models.TextField('Kurs xaqida qisaqacha malumot')
	slug = models.SlugField('*',max_length=50, unique=True)
	image = models.ImageField('Rasmi', upload_to='post_images/')
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('main:course_detail', kwargs={'course_slug':self.slug})


class Teacher(models.Model):
	name = models.CharField('Name',max_length=50)
	surname = models.CharField('Surname',max_length=50)
	cours = models.ForeignKey(Cours,
		on_delete=models.CASCADE,
		related_name='posts')
	slug = models.SlugField('*',max_length=50,unique=True)
	image = models.ImageField('Rasmi', upload_to='post_images/')
	tajribasi = models.CharField('Ish Tajribasi',max_length=50)
	natijasi = models.CharField('Natijasi',max_length=50)
	body = models.TextField('Qisqacha Malumot')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('main:teacher_detail', kwargs={'teacher_slug':self.slug})


