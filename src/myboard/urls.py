from boards import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include("accounts.urls")),
    path('boards/', include("boards.urls")),
    path('admin/', admin.site.urls),
]
