from django.conf import settings
from django.db import models
from django.utils import timezone


# Single answer
class SubpartAns(models.Model):
    subpart = models.ForeignKey('Subpart', on_delete=models.CASCADE, related_name='answers')
    score = models.IntegerField(default=0)
    ans = models.ForeignKey('Ans', on_delete=models.CASCADE, related_name='subpart_answers')

    def __str__(self):
        return self.subpart.text

class Ans(models.Model):
    CHOICES = [(10, 'HIGH'),
                (5, 'MEDIUM'),
                (1, 'LOW')]
    ques = models.ForeignKey('Ques', on_delete=models.CASCADE, related_name='choice_answers')
    # score = models.IntegerField(choices=CHOICES, default=0)
    bunch = models.ForeignKey('AnsBunch', on_delete=models.CASCADE, related_name='choice_answers')

    def tot_score(self):
        tot = 0
        for ans in self.subpart_answers.all():
            tot += ans.score
        return tot

    def avg_score(self):
        tot = self.tot_score()
        if self.subpart_answers.all().count()==0:
            return "NaN"
        else:
            return tot/self.subpart_answers.all().count()

# Set of answers
class AnsBunch(models.Model):
    # answers = models.ManyToManyField(Ans, related_name='choice_bunch')
    created_at = models.DateTimeField(default=timezone.now())

    def avg(self):
        tot = 0
        for ans in self.choice_answers.all():
            tot += ans.avg_score()
        if(self.choice_answers.all().count()==0):
            return "NaN"
        else:
            # average = tot/self.choice_answers.all().count()
            return tot/self.choice_answers.all().count()






class Subpart(models.Model):
    CHOICES = [(10, 'HIGH'),
                (5, 'MEDIUM'),
                (1, 'LOW')]
    text = models.TextField()
    score = models.IntegerField(default=0)
    ques = models.ForeignKey('Ques', on_delete=models.CASCADE, related_name='choice_subparts')

    def __str__(self):
        return self.text

class Ques(models.Model):
    ques = models.TextField()
    ques_num = models.IntegerField(default=0)
    section = models.CharField(max_length=200)
    # sub_part = models.CharField(max_length=200, default="NULL")

    CHOICES = [(10, 'HIGH'),
                (5, 'MEDIUM'),
                (1, 'LOW')]
    # score_for_subpart = models.IntegerField(choices=CHOICES, default=0)
    def __str__(self):
        return self.ques


class Score(models.Model):
    ques_num = models.ForeignKey(Ques, on_delete=models.CASCADE, default=0)
    # choice_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.score