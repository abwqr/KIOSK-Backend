from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path('profile/<user_id>/', login_required(views.ProfileView.as_view())),

    path('user/<int:pk>/', views.UserView.as_view()),
    path('users/', views.AllUsersView.as_view()), #for testing

    path('skills/', views.SkillView.as_view()),
    path('skills/<int:pk>/', views.UpdateSkillView.as_view()), #skill pk

    path('education/', views.EducationView.as_view()),
    path('education/<int:pk>/', views.UpdateEducationView.as_view()), #education pk
]
