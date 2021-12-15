from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include
from directory import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('directory.api.urls.users_urls')),
    path('api/', include('directory.api.urls.login_urls')),

]
