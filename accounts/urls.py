from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.UpdateProfileView.as_view()), #update and view profile (private)
    path('profile/<user_id>/', views.ProfileView.as_view()), #view profile (public)

    path('user/', views.UserView.as_view()),
    path('users/', views.AllUsersView.as_view()), #for testing

    path('skills/', views.CreateSkillView.as_view()), #view or create own skill (private)
    path('skills/<user_id>', views.SkillView.as_view()), #view user's skill (public)
    path('skills/update/<int:pk>/', views.UpdateSkillView.as_view()), #update and delete own skill (private)

    path('education/', views.CreateEducationView.as_view()), #view or create own Education (private)
    path('education/<user_id>', views.EducationView.as_view()), #view user's Education (public)
    path('education/update/<int:pk>/', views.UpdateEducationView.as_view()), #update and delete own Education (private)

    path('experience/', views.CreateExperienceView.as_view()), #view or create own Experience (private)
    path('experience/<user_id>', views.ExperienceView.as_view()), #view user's Experience (public)
    path('experience/update/<int:pk>/', views.UpdateExperienceView.as_view()), #update and delete own Experience (private)

    # path('experience/', views.ExperienceView.as_view()),
    # path('experience/<int:pk>/', views.UpdateExperienceView.as_view()), #experience pk
]
