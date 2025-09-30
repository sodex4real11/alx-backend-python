from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Message
from .serializers import MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # search by conversation title

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'sender']  # search by content or sender
