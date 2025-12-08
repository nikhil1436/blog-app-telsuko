from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job),
    path('jobs/', views.list_jobs),
    path('apply/', views.apply_job),
    path('job-summary/', views.job_summary),
]