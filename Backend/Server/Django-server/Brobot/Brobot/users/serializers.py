from rest_framework import serializers
from Brobot.users.models import User, Message
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from statistics import mean
import requests, json
from time import time
import re
from better_profanity import profanity


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:
        model = Message
        fields = [
            'user',
            'msg_text',
            'is_bot',
            'timestamp',
        ]

    def create(self, validated_data):
        user_hash = validated_data.pop('user')
        msg_text = validated_data.pop('msg_text')
        is_bot = validated_data.pop('is_bot')
        timestamp = validated_data.pop('timestamp')

        # Evaluate and store mood scores and user message
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(msg_text)
        comp_score = vs['compound']
        neu_score = vs['neu']
        neg_score = vs['neg']
        pos_score = vs['pos']
        messages = Message.objects.all()
        scores = [m.compound_score for m in messages if not m.is_bot]
        user_obj = User.objects.get(user_hash=user_hash)
        user_obj.avg_mood_score = mean(scores) if len(scores) > 0 else 0
        user_obj.save()
        Message.objects.create(user=user_obj, msg_text=msg_text, is_bot=is_bot, timestamp=timestamp,
                               compound_score=comp_score, neg_score=neg_score, neu_score=neu_score,
                               pos_score=pos_score)

        # Retrieve response from rasa, create instance and return
        url = "http://localhost:5005/webhooks/rest/webhook"
        obj = {
            "sender": user_hash,
            "message": msg_text,
        }
        x = requests.post(url, data=json.dumps(obj))
        bot_obj = x.json()
        bot_said = bot_obj[0]['text']
        bot_said = ".".join(sent.capitalize() for sent in bot_said.split('.'))
        bot_said = re.sub(r'((\b\w+\b.{1,2}\w+\b)+).+\1', r'\1', bot_said, flags=re.I)
        profanity.load_censor_words()
        bot_said = profanity.censor(bot_said)
        return Message.objects.create(user=user_obj, msg_text=bot_said, is_bot=True, timestamp=int(time()))

    # generates 'user' table queries


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_hash',
        ]
