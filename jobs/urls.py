from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [

    path('projects/test/', views.TestProjectView.as_view()), #testing
    path('projects/all/', views.AllProjectView.as_view()), #get all projects based on user's type


    path('projects/', views.ProjectView.as_view()), #to create new or view all owned projects (private)
    path('projects/<user_id>/', views.ListProjectView.as_view()), #to view user's projects (public)
    path('projects/update/<int:pk>/', views.UpdateProjectView.as_view()), #to update or delete specific own project (private)
    
    path('skills/', views.TestProjectSkillView.as_view()), #testing
    path('projects/<project_id>/skills/', views.ProjectSkillView.as_view()), #to view and create skills for owned projects (private)
    path('projects/<project_id>/skills/<int:pk>/', views.Update_Project_Skill_View.as_view()), #to update and delete skills of specific owned projects (private)
    path('projects/view/<project_id>/skills/', views.ListProjectSkillView.as_view()), #to view skills of user's projects
]
