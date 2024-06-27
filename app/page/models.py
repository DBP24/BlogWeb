from django.db import models

class ProfessionalProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    # profile_photo = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    brith_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

