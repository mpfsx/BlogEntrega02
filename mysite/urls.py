from django.contrib import admin
from django.urls import path, include
from app.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', index, name='index'),
    path('<int:post_id>/', detail, name='detail'),
]
