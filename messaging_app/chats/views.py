from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]  # Require authentication
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]  # Require authentication
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'sender']

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Message.objects.none()  # No messages if not authenticated

        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            # Filter messages by conversation_id
            return Message.objects.filter(conversation_id=conversation_id)
        return Message.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required."},
                status=status.HTTP_403_FORBIDDEN
            )
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required."},
                status=status.HTTP_403_FORBIDDEN
            )
        conversation_id = request.data.get('conversation')
        if not conversation_id:
            return Response(
                {"detail": "Conversation ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
