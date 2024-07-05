from django.urls import path
from .views import *

urlpatterns = [
    path('', MessageList.as_view(), name='msg_list'), 
    path('<int:pk>/', MessageView.as_view(), name='msg_view'),
    path('<int:pk>/delete/', MessageDelete.as_view(), name='msg_delete'),
    path('create/', MessageCreate.as_view(), name='msg_create'),
]