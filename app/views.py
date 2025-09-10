from django.shortcuts import render,get_object_or_404
from .models import Project,Images,Head_Carosel
# Create your views here.

def home(request):
    projects=Images.objects.order_by("-id")[:9]
    latest_carosel = Head_Carosel.objects.order_by('-created_at').first()  # latest object

    image1 = latest_carosel.image1.url if latest_carosel else None
    image2 = latest_carosel.image2.url if latest_carosel else None

    context = {
        'image1': image1,
        'image2': image2,
        "projects":projects
    }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def services(request):
    services=Project.objects.all()
    return render(request, 'services.html',{"services":services}) 

def service_details(request, id): 
    service = get_object_or_404(Project, id=id)

    similar_services = Project.objects.filter(project_type=service.project_type).exclude(id=id)
    return render(request, "service_details.html", {
        'service': service,
        'services': similar_services
    })


def gallery(request):
    images=Images.objects.all()
    return render(request, 'gallery.html',{"images":images})


def contact(request):
    return render(request, 'contact.html')

