from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('', views.userhome, name='userhome'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project_details/<int:project_id>/', views.project_details_from_work, name='project_details_from_work'),
    path('moreworks/<int:bottom_id>/', views.moreworks, name='moreworks'),
    path('worklist/', views.worklist, name='worklist'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('submit-contact-form/', views.contact_form_submit, name='submit_contact_form'),


]
