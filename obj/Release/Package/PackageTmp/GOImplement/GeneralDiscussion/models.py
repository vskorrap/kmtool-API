from django.db import models


class DiscussionForum_Questions(models.Model):
    Question = models.CharField(max_length=4000)
    Subject = models.CharField(max_length=4000,null=True)
    Timestamp = models.DateTimeField(auto_created=True)
    class Meta:
        managed = True
        db_table = 'tblDiscussionsQuestions'

class DiscussionForum_Answers(models.Model):
    fkQuestion = models.ForeignKey(DiscussionForum_Questions,on_delete=models.CASCADE)
    Answer = models.CharField(max_length=4000)
    class Meta:
        managed = False
        db_table = 'tblDiscussionsAnswers'

