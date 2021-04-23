from django.urls import path, re_path

from Brobot.users.views import UserCreateView, MessageCreateView, MessageListView

# api for user table
urlpatterns = [
    # Get and post api for 'user' table
    path('register/', UserCreateView.as_view()),
    path('message/', MessageCreateView.as_view()),
    path('message/<str:fk>/', MessageListView.as_view()),
]
