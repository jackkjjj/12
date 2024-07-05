from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']     

# 留言檢視
class MessageView(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']     # 僅顯示 user, subject, content 這 3 個欄位
    success_url = reverse_lazy('msg_list') 
    # 刪除留言
class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')      # 刪除成功後，導向留言列表     # 新增成功後，導向留言列表