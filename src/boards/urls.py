from django.urls import path, re_path, include
from boards import views

urlpatterns = [
    path('', views.home, name="home"),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name="board-topics"),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name="new-topic"),
]
