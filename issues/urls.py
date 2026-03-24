from django.urls import path
from . import views

urlpatterns = [
    path('reporters/', views.reporter_list_create, name='reporter-list-create'),
    path('issues/', views.issue_list_create, name='issue-list-create'),
]
