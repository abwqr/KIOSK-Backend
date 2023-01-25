from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/<user_id>', views.ProfileView.as_view()),
    path('user/<int:pk>', views.UserView.as_view()),
    path('users/', views.AllUsersView.as_view()),
    path('user/skills', views.SkillView.as_view()),
    path('user/skills/update/<int:pk>', views.SkillModifyView.as_view()),

]
