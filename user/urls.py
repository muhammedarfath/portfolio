from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', views.userhome, name='userhome'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('moreworks/<int:bottom_id>/', views.moreworks, name='moreworks'),
    path('worklist/', views.worklist, name='worklist'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_page, name='contact'),


]
