from django.urls import path
from . import views

urlpatterns = [
    #Home page URL
    path('', views.HomePageView.as_view(), name='home_page'),

    #Authentication URLs
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
    #Task navigation URLs
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', views.TaskDescriptionView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='edit_task'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
]