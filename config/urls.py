from django.contrib import admin
from django.urls import path, include
from blog.views import HomeView, AboutPageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),  # Bosh sahifa
    path('post/', include('blog.urls')),        # post/<int:pk>/ va h.k.
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout va h.k.
    path('accounts/', include('accounts.urls')),  
    path('about/', AboutPageView.as_view(), name='about'),  
    path('login/', auth_views.LoginView.as_view(), name='login'),    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
