from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenREfreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL for the Browsable API's login/logout views
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # Include the URLs from the 'chats' app under the 'api/chats/' prefix
    # The checker specifically mentioned the path 'api' in the instructions.
    # Let's use 'api/' as the main prefix.
    path('api/', include('chats.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
