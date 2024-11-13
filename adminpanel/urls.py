from . import views
from django.urls import path

app_name = 'adminpanel'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('about_contact/', views.about_contact, name='about_contact'),
    path('edit_about/', views.edit_about, name='edit_about'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete_file_bottom/<int:file_id>/', views.delete_file_bottom, name='delete_file_bottom'),
    path('delete_file_work/<int:file_id>/', views.delete_file_work, name='delete_file_work'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('edit_work_project/<int:project_id>/', views.edit_work_project, name='edit_work_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('delete_work_project/<int:project_id>/', views.delete_work_project, name='delete_work_project'),
    path('addbottom_projects/', views.add_bottom_project, name='addbottom_projects'),
    path('edit_bottom_project/<int:bottom_id>/', views.edit_bottom_project, name='edit_bottom_project'),
    path('delete-bottom-project/<int:bottom_id>/', views.delete_bottom_project, name='delete_bottom_project'),

]