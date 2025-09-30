from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet

# The main router for the top-level resource (Conversations)
router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet)

# Create a nested router for Messages, registered under Conversations.
# The `lookup='conversation'` tells the router that the URL parameter for the
# conversation's ID will be named 'conversation_pk'.
conversations_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# The API URLs are now nested.
urlpatterns = [
    path('messages/', views.messages_list, name='messages-list'),  # example route
    path('', include(router.urls)
]
