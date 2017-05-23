import string
import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from questions.models import Question


class Command(BaseCommand):
    help = 'Adds a question with a random title and text'

    def handle(self, *args, **options):
        question = Question(title=self.text_gen(), text=self.text_gen(40)+"?", author=User.objects.get(id=1))
        question.save()
        self.stdout.write(self.style.SUCCESS('Successfully created question ' + question.title
                                             + ' with text ' + question.text))

    @staticmethod
    def text_gen(size=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))
