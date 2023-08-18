from django.db import models

# Create your models here.
class Speciallist(models.Model):
    speciallist_name = models.CharField(max_length=50) #전문의 이름
    speciallist_type = models.CharField(max_length=50) #전공
    speciallist_hospital = models.TextField()#병원
    
    def __str__(self):
        return self.speciallist_name