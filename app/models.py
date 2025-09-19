from django.db import models

# Create your models here.


class Head_Carosel(models.Model):
    image1 = models.ImageField(upload_to="carosel/")
    image2 = models.ImageField(upload_to="carosel/")
    created_at = models.DateTimeField(auto_now_add=True)  # add this for ordering

    def __str__(self):
        return f"Carousel {self.id}"


class Project(models.Model):
    image = models.ImageField(upload_to="project_image/")
    PROJECT_TYPES = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
    ]
    description = models.CharField(max_length=250)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    customer_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    square_feet = models.PositiveIntegerField(null=True, blank=True)

    # New fields for key features
    feature1 = models.CharField(max_length=255, default="Premium Quality Materials")
    feature2 = models.CharField(max_length=255, default="Energy Efficient")
    feature3 = models.CharField(max_length=255, default="Modern Design Concepts")
    feature4 = models.CharField(max_length=255, default="Customizable Options")


    def __str__(self):
        return f"{self.customer_name} - {self.project_type}"



class Images(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery_image/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    
class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    feedback=models.TextField()
    image=models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.phone})"



