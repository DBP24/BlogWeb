from django.contrib import admin
from .models import ProfessionalProfile, SocialMedia

@admin.register(ProfessionalProfile)
class ProfessionalProfileAdmin(admin.ModelAdmin):
    # Define cómo se mostrarán los datos en el panel de administración
    list_display = ('name', 'title', 'email', 'phone', 'address')

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    # Define cómo se mostrarán los datos en el panel de administración
    list_display = ('profile', 'facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url', 'github_url')

