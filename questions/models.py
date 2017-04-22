# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
	title = models.CharField(max_length=255, verbose_name="заголовок")
	text = models.TextField(verbose_name="текст")
	#is_published = models.BooleanField(default=False, blank=True, verbose_name="Публик")
	author = models.ForeignKey(User, verbose_name="автор")
	tags = models.ManyToManyField(u"Tag")
	rating = models.IntegerField(verbose_name='рейтинг', default=0)
	added_on=models.DateField(verbose_name='дата добавления')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'вопрос'
		verbose_name_plural = 'вопросы'


class Profile(models.Model):
	name = models.OneToOneField(User, verbose_name="пользователь", 
		on_delete=models.CASCADE, primary_key=True)
	avatar = models.FileField(verbose_name="аватар")

	def __str__(self):
		return self.user.name

	class Meta:
		verbose_name = 'профиль'
		verbose_name_plural = 'профили'


class Tag(models.Model):
	name = models.CharField(max_length=255, verbose_name="имя")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'тег'
		verbose_name_plural = 'теги'


class Answer(models.Model):
	content = models.TextField(verbose_name='текст ответа')
	author = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)
	question = models.ForeignKey(Question, verbose_name='связанный вопрос',
	 on_delete=models.CASCADE)
	is_correct = models.BooleanField(verbose_name='верный?', default=False)

	def __str__(self):
		return 'Comment №{number} by {user}'.format(number=self.pk, user='Username')

	class Meta:
		verbose_name = 'ответ'
		verbose_name_plural = 'ответы'
