from django.db import models

class ProfessionalProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    profile_photo = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True, default='perfil.jpg')
    brith_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    # Relación uno a uno con ProfessionalProfile
    profile = models.OneToOneField(ProfessionalProfile, on_delete=models.CASCADE, related_name='social_media')

    def __str__(self):
        return f"Redes sociales de {self.profile.name}"