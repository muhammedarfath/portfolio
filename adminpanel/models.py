# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    work_heading = models.TextField(blank=True, null=True)
    work_description = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    nav_image = models.ImageField(upload_to='nav_images/', blank=True, null=True)
    nav_hover_images1 = models.ImageField(upload_to='nav_hover_images1/', blank=True, null=True)
    nav_hover_images2 = models.ImageField(upload_to='nav_hover_images2/', blank=True, null=True)
    nav_hover_images3 = models.ImageField(upload_to='nav_hover_images3/', blank=True, null=True)
    nav_body_images1 = models.ImageField(upload_to='nav_body_images1/', blank=True, null=True)
    nav_body_images2 = models.ImageField(upload_to='nav_body_images2/', blank=True, null=True)
    nav_body_images3 = models.ImageField(upload_to='nav_body_images3/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
    
class HomepageProject(models.Model):
    project_name = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hover_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True) 
    company = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name    
    
    
    

class HomeProjectFile(models.Model):
    project = models.ForeignKey(HomepageProject, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='homepage_projects/videos/',max_length=500)
    
    def __str__(self):
        return f'File for {self.project.project_name}'    
    


class WorkpageProject(models.Model):
    project_name = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hover_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True) 
    company = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

class ProjectFile(models.Model):
    project = models.ForeignKey(WorkpageProject, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='homepage_projects/videos/')
    
    def __str__(self):
        return f'File for {self.project.project_name}'
    
    
    
class BottomProject(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hover_img = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name    
    
class BottomProjectFile(models.Model):
    project = models.ForeignKey(BottomProject, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='bottom_projects/file/')
    
    def __str__(self):
        return f'File for {self.project.name}'
    
    
class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    about_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    contact_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    name = models.TextField(blank=True, null=True) 
    subdescription = models.TextField(blank=True, null=True)  
    maindescription = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)   
    title_description = models.TextField(blank=True, null=True)   
    references = models.TextField(blank=True, null=True)  
    email = models.EmailField(max_length=100, blank=True, null=True)  
    whatsapp = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name  

    
    