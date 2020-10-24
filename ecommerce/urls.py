from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('', include('user.urls')),
    path('login/', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
