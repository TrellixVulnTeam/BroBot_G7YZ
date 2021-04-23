# Create your views here.
from rest_framework import generics

from Brobot.users.models import User, Message
from Brobot.users.serializers import UserSerializer, MessageListSerializer, \
    MessageCreateSerializer


# functionality to call when api is hit
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        fk = self.kwargs['fk']
        user_obj = User.objects.get(user_hash=fk)
        return Message.objects.filter(user=user_obj)
