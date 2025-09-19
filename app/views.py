from django.shortcuts import render,get_object_or_404,redirect
from .models import Project,Images,Head_Carosel,Testimonials,Contact
# Create your views here.

def home(request):
    projects=Images.objects.order_by("-id")[:9]
    latest_carosel = Head_Carosel.objects.order_by('-created_at').first()  # latest object
    testimonials = Testimonials.objects.all()

    image1 = latest_carosel.image1.url if latest_carosel else None
    image2 = latest_carosel.image2.url if latest_carosel else None

    context = {
        'image1': image1,
        'image2': image2,
        "projects":projects,
        'testimonials': testimonials,
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


from django.core.paginator import Paginator


def gallery(request):
    images = Images.objects.all().order_by('-id')  # latest first
    paginator = Paginator(images, 9)  # 9 images per page (3x3 grid)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'gallery.html', {"page_obj": page_obj})


from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Create and save contact entry
        Contact.objects.create(
            name=name,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # redirect to clear form after POST

    return render(request, 'contact.html')


