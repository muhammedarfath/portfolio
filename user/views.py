import random
from django.shortcuts import get_object_or_404, render
from adminpanel.models import About, BottomProject, UserProfile,HomepageProject, WorkpageProject

# Create your views here.


def userhome(request):
    last_profile = UserProfile.objects.order_by('-id').first() 
    projects = HomepageProject.objects.all().prefetch_related('files')
    bottomprojects = BottomProject.objects.all().prefetch_related('files')

    for project in projects:
        project.keywords_list = [keyword.strip() for keyword in project.keyword.split(',')] if project.keyword else []
        project.first_file = project.files.first() 
        
    for bottom in bottomprojects:
        first_file = bottom.files.first()
        if first_file:
            file_url = first_file.file.url
            bottom.first_file = first_file
            bottom.first_file.is_video = file_url.lower().endswith('.mp4')
        else:
            bottom.first_file = None

    
    context = {
        'profile': last_profile,
        'projects': projects,
        'bottomprojects': bottomprojects,
        'nav_hover_images1': last_profile.nav_hover_images1,
        'nav_hover_images2': last_profile.nav_hover_images2,
        'nav_hover_images3': last_profile.nav_hover_images3,  
        
    }
    return render(request, 'user/userhome.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(HomepageProject, id=project_id)
    files = project.files.all()

    project.first_file = files.first() if files else None
    project.other_files = [
        {
            'url': file.file.url if file.file else '', 
            'is_video': file.file.url.endswith('.mp4') if file.file else False
        }
        for file in files[1:] 
    ]

        
    
    project.keywords_list = [keyword.strip() for keyword in project.keyword.split(',')] if project.keyword else []

    return render(request, 'user/project_detail.html', {'project': project, 'files': files})


def project_details_from_work(request, project_id):
    project = get_object_or_404(WorkpageProject, id=project_id)
    files = project.files.all()

    project.first_file = files.first() if files else None
    project.other_files = [
        {
            'url': file.file.url if file.file else '', 
            'is_video': file.file.url.endswith('.mp4') if file.file else False
        }
        for file in files[1:] 
    ]

        
    
    project.keywords_list = [keyword.strip() for keyword in project.keyword.split(',')] if project.keyword else []

    return render(request, 'user/project_detail.html', {'project': project, 'files': files})

def worklist(request):
    projects = WorkpageProject.objects.all().prefetch_related('files')
    bottomprojects = BottomProject.objects.all().prefetch_related('files')

    for project in projects:
        project.keywords_list = [keyword.strip() for keyword in project.keyword.split(',')] if project.keyword else []
        project.first_file = project.files.first() 
    for bottom in bottomprojects:
            first_file = bottom.files.first()
            if first_file:
                file_url = first_file.file.url
                bottom.first_file = first_file
                bottom.first_file.is_video = file_url.lower().endswith('.mp4')
            else:
                bottom.first_file = None        
    context = {
        'projects': projects,
        'bottomprojects': bottomprojects  

    }
    return render(request, 'user/worklist.html',context)




    

def about(request):
    about = About.objects.order_by('-id').first() 
    references_list = [ref.strip() for ref in about.references.split(',')] if about.references else []
    projects = WorkpageProject.objects.all().prefetch_related('files')

    context = {
        'about': about,
        'references_list': references_list,
        'projects':projects,
    }
    return render(request, 'user/about.html', context)


def error_404_view(request, exception):
    return render(request, 'user/404.html')



def contact_page(request):
    contact = About.objects.order_by('-id').first() 
    context = {
        'contact': contact,
    }
    return render(request, 'user/contact.html',context)



def moreworks(request, bottom_id):
    project = get_object_or_404(BottomProject, id=bottom_id)
    files = project.files.all()

    project.first_file = files.first() if files else None
    project.first_file_is_video = project.first_file and project.first_file.file.url.endswith('.mp4')
    project.first_file_is_image = project.first_file and project.first_file.file.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))
    second_project = BottomProject.objects.all()
    second_project = random.choice(second_project)
    second_project_first_file = second_project.files.first() 
    if second_project_first_file:
        second_project_first_file_info = {
            'url': second_project_first_file.file.url if second_project_first_file.file else '',
            'is_video': second_project_first_file.file.url.endswith('.mp4') if second_project_first_file.file else False,
            'is_image': second_project_first_file.file.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')) if second_project_first_file.file else False
        }
    else:
        second_project_first_file_info = None
    project.other_files = [
        {
            'url': file.file.url if file.file else '', 
            'is_video': file.file.url.endswith('.mp4') if file.file else False,
            'is_image': file.file.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')) if file.file else False
        }
        for file in files[1:] 
    ]

    return render(
        request, 
        'user/more-works.html', 
        {'project': project, 'files': files, 'second_project': second_project, 'second_project_first_file_info': second_project_first_file_info}
    )
    
    

    
    
    
    
