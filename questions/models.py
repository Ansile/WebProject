# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from questions.managers import QuestionVoteManager, QuestionManager


class Question(models.Model):
	title = models.CharField(max_length=255, verbose_name="заголовок")
	text = models.TextField(verbose_name="текст")
	author = models.ForeignKey(User, verbose_name="автор")
	tags = models.ManyToManyField("Tag")
	rating_num = models.IntegerField(verbose_name='рейтинг', default=0)
	added_on = models.DateTimeField(verbose_name='дата и время добавления', auto_now_add=True)

	objects = QuestionManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'вопрос'
		verbose_name_plural = 'вопросы'


class Profile(models.Model):
	user = models.OneToOneField(User, verbose_name="пользователь", 
		on_delete=models.CASCADE, primary_key=True)
	avatar = models.ImageField(verbose_name="аватар")

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
	rating_num = models.IntegerField(verbose_name='рейтинг', default=0)
	added_on = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='дата и время добавления')

	def __str__(self):
		return 'Comment №{number} by {user}'.format(number=self.pk, user='Username')

	class Meta:
		verbose_name = 'ответ'
		verbose_name_plural = 'ответы'


class Vote (models.Model):
	voted_by = models.ForeignKey(User, verbose_name='оценено пользователем')
	is_like = models.BooleanField(verbose_name='верный', default=True)

	def __str__(self):
		return ("дизлайк", "лайк")[self.is_like] + "пользователя" + self.voted_by.username

	class Meta:
		abstract = True
		verbose_name = "оценка"
		verbose_name_plural = "оценки"


class QuestionVote (Vote):
	question = models.ForeignKey(Question, verbose_name='оцененный вопрос')

	objects = QuestionVoteManager()

	class Meta:
		unique_together = ("question", "voted_by")
	

class AnswerVote (Vote):
	answer = models.ForeignKey(Answer, verbose_name='оцененный ответ')
	
	class Meta:
		unique_together = ("answer", "voted_by")