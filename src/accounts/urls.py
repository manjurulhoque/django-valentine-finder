from django.urls import path, include

from src.accounts.views import login_view, register, logout_view, update_profile, upload_profile_picture
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    path('api/', include('accounts.api.urls')),
    path('profile/edit', update_profile, name='profile_edit'),
    path('login', login_view, name='login'),
    path('register', register, name='register'),
    path('logout', logout_view, name='logout'),
    path('profile/upload', upload_profile_picture, name='profile_picture_upload'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
