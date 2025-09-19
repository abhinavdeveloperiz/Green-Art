from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from datetime import timedelta

from .models import Project, Images, Head_Carosel, Testimonials, Contact




# ---------- PROJECT ADMIN ----------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "project_type", "location", "square_feet", "image_preview")
    search_fields = ("customer_name", "project_type", "location")
    list_filter = ("project_type",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 60px; border-radius: 5px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


# ---------- IMAGES ADMIN ----------
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image_preview")
    search_fields = ("title",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 60px; border-radius: 5px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


# ---------- HEAD_CAROUSEL ADMIN ----------
@admin.register(Head_Carosel)
class HeadCaroselAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "image1_preview", "image2_preview")
    readonly_fields = ("image1_preview", "image2_preview")

    def image1_preview(self, obj):
        if obj.image1:
            return format_html('<img src="{}" style="height: 60px; border-radius: 5px;" />', obj.image1.url)
        return "-"
    image1_preview.short_description = "Image 1"

    def image2_preview(self, obj):
        if obj.image2:
            return format_html('<img src="{}" style="height: 60px; border-radius: 5px;" />', obj.image2.url)
        return "-"
    image2_preview.short_description = "Image 2"


# ---------- TESTIMONIALS ADMIN ----------
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "feedback_short", "image_preview")
    search_fields = ("name", "feedback")
    readonly_fields = ("image_preview",)

    def feedback_short(self, obj):
        return obj.feedback[:50] + "..." if len(obj.feedback) > 50 else obj.feedback
    feedback_short.short_description = "Feedback"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 60px; border-radius: 5px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"


# ---------- CONTACT ADMIN ----------
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "subject", "message_short")
    search_fields = ("name", "phone", "subject", "message")

    def message_short(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_short.short_description = "Message"


# ---------- CUSTOMIZE ADMIN HEADER ----------
admin.site.site_header = "Green Art Admin"
admin.site.site_title = "Green Art Admin Portal"
admin.site.index_title = "Welcome to Green Art Admin Portal"
