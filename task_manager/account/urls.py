from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from account.views import *


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileUpdateView.as_view(), name = 'profile'),
    path('change-password/', ChangePasswordView.as_view(), name = 'change_password'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

    