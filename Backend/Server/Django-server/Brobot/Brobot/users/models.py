from django.db import models


# Required tables for a user

# User table
class User(models.Model):
    user_hash = models.CharField('user_hash', max_length=128, unique=True)
    avg_mood_score = models.FloatField('avg_mood_score', default=0)

    # str object for user
    def __str__(self):
        return '{}'.format(self.user_hash)


# A chat history contains multiple messages
class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    msg_text = models.CharField('msg_text', max_length=1028)
    timestamp = models.IntegerField('timestamp')
    is_bot = models.BooleanField('is_sender', null=False, blank=False)
    compound_score = models.FloatField('compound_score', default=-6.0)
    neg_score = models.FloatField('neg_score', default=-6.0)
    neu_score = models.FloatField('neu_score', default=-6.0)
    pos_score = models.FloatField('pos_score', default=-6.0)
