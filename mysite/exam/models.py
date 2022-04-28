from django.db import models

class Course(models.Model):
    
    ogretmen_adi = models.CharField(max_length=100)
    ders_kodu = models.CharField(max_length=30, unique=True)
    ders_adi = models.CharField(max_length=100)
    birim_adi = models.CharField(max_length=50, blank=True, null=True)
    ogrenci_sayisi = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ders_kodu

# Create your models here.
