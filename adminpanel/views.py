from django.shortcuts import render,redirect,get_object_or_404
from .models import About, BottomProject, BottomProjectFile, HomeProjectFile, ProjectFile, UserProfile, WorkpageProject
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .models import HomepageProject
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import SuspiciousFileOperation

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            if user.is_superuser:  
                auth_login(request, user)
                return redirect('adminpanel:index')
            else:
                messages.error(request, 'Access denied. Superuser privileges are required.')
        else:
            messages.error(request, 'Invalid credentials')
            
    return render(request, 'adminpanel/login.html')

@login_required
def index(request):
    return render(request, 'adminpanel/index.html')

@login_required
def home(request):
    last_profile = UserProfile.objects.order_by('-id').first()
    projects = HomepageProject.objects.all().prefetch_related('files')
    bottomprojects = BottomProject.objects.all().prefetch_related('files')

    for project in projects:
        project.keywords_list = [keyword.strip() for keyword in project.keyword.split(',')] if project.keyword else []
        project.files_data = [
            {
                'id': file.id,
                'url': file.file.url if file.file else '',
                'is_video': file.file.url.endswith('.mp4') if file.file else False
            }
            for file in project.files.all()
        ]

    for bottom in bottomprojects:
        bottom.files_data = [
            {
                'id': file.id,
                'url': file.file.url if file.file else '',
                'is_video': file.file.url.endswith('.mp4') if file.file else False
            }
            for file in bottom.files.all()
        ]

    context = {
        'profile': last_profile,
        'projects': projects,
        'bottomprojects': bottomprojects  
    }

    return render(request, 'adminpanel/home.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            profile = UserProfile.objects.get(user=request.user)
            profile.name = request.POST.get('name')
            profile.description = request.POST.get('description')
            if request.FILES.get('image'):
                profile.profile_image = request.FILES['image']
            profile.save()  
            return redirect('adminpanel:home')  


@login_required
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectName')
        keyword = request.POST.get('keyword')
        description = request.POST.get('description')
        year = request.POST.get('year')
        company = request.POST.get('company')
        hover_img = request.FILES.get('image')  
        my_files = request.FILES.getlist('my_files') 
        year_value = int(year) if year else None

        errors = []
        if not project_name:
            errors.append("Project name is required.")
        if not description:
            errors.append("Description is required.")  
        if not hover_img:
            errors.append("Hover image is required.")
        if not my_files:
            errors.append("At least one file must be uploaded.")   
              
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('adminpanel:home')
        
        # Attempt to save the project and files
        try:
            project = HomepageProject(
                project_name=project_name,
                keyword=keyword,
                description=description,
                year=year_value,
                company=company,
                hover_img=hover_img  
            )
            project.save()  

            for file in my_files:
                # Try to create a file entry for each file
                HomeProjectFile.objects.create(
                    project=project,
                    file=file
                )

            messages.success(request, "Project added successfully!")
            return redirect('adminpanel:home')  

        except SuspiciousFileOperation:
            messages.error(request, "One or more files have a filename that is too long. Please rename the files and try again.")
            return redirect('adminpanel:home')

    return render(request, 'adminpanel/home.html')


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(HomepageProject, id=project_id)
    
    if request.method == 'POST':
        project.project_name = request.POST.get('project_name')
        project.keyword = request.POST.get('keyword')
        project.description = request.POST.get('description')
        year = request.POST.get('year')
        project.year = int(year) if year and year.lower() != 'none' else None

        if request.FILES.get('hover_img'):
            project.hover_img = request.FILES.get('hover_img')

        project.save()

        files = request.FILES.getlist('my_files')
        for f in files:
            HomeProjectFile.objects.create(project=project, file=f)

        messages.success(request, 'Project updated successfully!')
        return redirect('adminpanel:home')
    
    return render(request, 'adminpanel/home.html')


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(HomepageProject, id=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('adminpanel:home')


@csrf_exempt 
@login_required
def delete_file(request, file_id):
    if request.method == 'POST':
        file = get_object_or_404(HomeProjectFile, id=file_id)
        file.delete()
        return JsonResponse({"success": True, "message": "File deleted successfully."})
    return JsonResponse({"success": False, "message": "Invalid request method."})

@csrf_exempt 
@login_required
def delete_file_bottom(request, file_id):
    if request.method == 'POST':
        file = get_object_or_404(BottomProjectFile, id=file_id)
        file.delete()
        return JsonResponse({"success": True, "message": "File deleted successfully."})
    return JsonResponse({"success": False, "message": "Invalid request method."})


# starting work page logic

@login_required
def work(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectName')
        keyword = request.POST.get('keyword')
        description = request.POST.get('description')
        year = request.POST.get('year')
        hover_img = request.FILES.get('image')  
        my_files = request.FILES.getlist('my_files') 
        company = request.POST.get('company')
        year_value = int(year) if year else None
        
        errors = []
        if not project_name:
            errors.append("Project name is required.")
        if not description:
            errors.append("Description is required.")  
        if not my_files:
            errors.append("At least one file must be uploaded.")   
              
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('adminpanel:work')
        try:
            project = WorkpageProject(
                project_name=project_name,
                keyword=keyword,
                description=description,
                year=year_value,
                hover_img=hover_img,
                company=company,
    
            )
            project.save()  
            for file in my_files:
                ProjectFile.objects.create(
                    project=project,
                    file=file
                )
            messages.success(request, "Project added successfully!")
            return redirect('adminpanel:work')  
        except SuspiciousFileOperation:
            messages.error(request, "One or more files have a filename that is too long. Please rename the files and try again.")
            return redirect('adminpanel:work')
   
    projects = WorkpageProject.objects.all().prefetch_related('files')

    for project in projects:
        project.keywords_list = [keyword.strip() for keyword in project.keyword.split(',')] if project.keyword else []
        
        project.files_data = [
            {
                'id': file.id,
                'url': file.file.url if file.file else '',
                'is_video': file.file.name.endswith('.mp4') if file.file else False
            }
            for file in project.files.all()
        ]

    context = {
        'projects': projects
    }
    return render(request, 'adminpanel/work.html', context)

@csrf_exempt 
@login_required
def delete_file_work(request, file_id):
    if request.method == 'POST':
        file = get_object_or_404(ProjectFile, id=file_id)
        file.delete()
        return JsonResponse({"success": True, "message": "File deleted successfully."})
    return JsonResponse({"success": False, "message": "Invalid request method."})


@login_required
def edit_work_project(request, project_id):
    project = get_object_or_404(WorkpageProject, id=project_id)
    
    if request.method == 'POST':
        project.project_name = request.POST.get('project_name')
        project.keyword = request.POST.get('keyword')
        project.description = request.POST.get('description')
        project.year = request.POST.get('year')

        if request.FILES.get('hover_img'):
            project.hover_img = request.FILES.get('hover_img')

        project.save() 

        files = request.FILES.getlist('my_files') 
        print(files)
        for f in files:
            # Create HomeProjectFile for each uploaded file
            ProjectFile.objects.create(project=project, file=f)

        messages.success(request, 'Project updated successfully!')
        return redirect('adminpanel:work')
    
    return render(request, 'adminpanel/work.html')



@login_required
def delete_work_project(request, project_id):
    project = get_object_or_404(WorkpageProject, id=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('adminpanel:work')
 
    

def add_bottom_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectName')
        description = request.POST.get('description')

        if not project_name:
            messages.error(request, "Project Name is required.")
            return redirect('adminpanel:home')

        if not description:
            messages.error(request, "Project Description is required.")
            return redirect('adminpanel:home')

        # Create the BottomProject instance
        project = BottomProject.objects.create(name=project_name, description=description)

        # Print out the request.FILES to debug
        print(request.FILES)

        # Get the files uploaded
        files = request.FILES.getlist('my_files')

        if not files:
            messages.error(request, "No files were uploaded.")
            return redirect('adminpanel:home')

        # Create BottomProjectFile instances and save them
        for file in files:
            BottomProjectFile.objects.create(project=project, file=file)

        messages.success(request, 'Project added successfully!')
        return redirect('adminpanel:home')

    return render(request, 'adminpanel/home.html')



@login_required
def edit_bottom_project(request, bottom_id):
    print(bottom_id, 'whtassappp')
    bottom_project = get_object_or_404(BottomProject, id=bottom_id)

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        my_files = request.FILES.getlist('my_files')

        # Debugging: print the received data
        print("Project Name:", project_name)
        print("Description:", description)
        print("Uploaded Files:", my_files)

        # Update project details
        if project_name:
            bottom_project.name = project_name
        if description:
            bottom_project.description = description

        bottom_project.save()

        # Save new files
        for file in my_files:
            BottomProjectFile.objects.create(project=bottom_project, file=file)

        messages.success(request, "Project updated successfully!")
        return redirect('adminpanel:home')  # Redirect to the home page or project list

    return redirect('adminpanel:home')


def delete_bottom_project(request, bottom_id):
    bottom_project = get_object_or_404(BottomProject, id=bottom_id)

    if request.method == 'POST':
        bottom_project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect('adminpanel:home')  # Redirect back to the home page or project list

    return redirect('adminpanel:home')



@login_required
def about_contact(request):
    about = About.objects.order_by('-id').first()
    context = {
        'about': about,
    }
    return render(request, 'adminpanel/about_contact.html',context)
    
    
@login_required
def edit_about(request):
    about = About.objects.get(user=request.user)
    if request.method == 'POST':
        about.name = request.POST.get('name')
        about.subdescription = request.POST.get('subdescription')
        about.maindescription = request.POST.get('maindescription')
        about.references = request.POST.get('references')
        about.email = request.POST.get('email')
        about.whatsapp = request.POST.get('whatsapp')
        if request.FILES.get('image'):
            about.about_image = request.FILES['image']
        if request.FILES.get('contactimage'):
            about.about_image = request.FILES['contactimage']            
        about.save()
        return redirect('adminpanel:about_contact')
    else:
        return render(request, 'about_contact.html', {'about': about})