from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name = 'home'),
    path('allPosts/', views.allPosts, name = 'allPosts'),
    path('register/', views.register, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('user/', views.userPage, name = "user"),
    path('createPost/', views.createPost, name = "createPost"),
    path('deletePost/<str:pk>/', views.deletePost, name = 'deletePost'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name ="accounts/password_reset.html"), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name = "password_reset_complete"),
    path('like', views.like_post, name = "like_post"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)