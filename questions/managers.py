from django.db import models


class QuestionManager(models.Manager):
    def hot(self):
        return self.order_by('-rating_num')[:10]

    def new(self):
        return self.order_by('-date')

    def by_tag(self, tag):
    	return self.filter(tags__name__iexact=tag).order_by('-date')


class QuestionVoteManager(models.Manager):
    def by_question(self, question_id):
        return self.filter(question__id=question_id)

    def get_rating(self, question_id):
        rating = 0
        votes = self.filter(question__id=question_id).all()
        for vote in votes:
            if vote.is_like:
                rating += 1
            else:
                rating -= 1 
        return rating

    def add_vote(self, question, vote):
        self.create(question=question)
        question.rating = self.get_rating(question.id)
        question.save()