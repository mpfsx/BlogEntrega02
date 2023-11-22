from django.urls import path
from .views import index, detail, post_list, post_detail, post_create, post_edit, post_delete, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('<int:post_id>/', detail, name='detail'),
    path('post_list/', post_list, name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
