from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    #re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer)
    re_path(r'^ws/(?P<pk>\d+)/chat/$', consumers.ChatConsumer)
]