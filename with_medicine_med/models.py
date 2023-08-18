from django.db import models

# Create your models here.
class Med_info(models.Model):
    med_name = models.CharField(max_length=50) #제품명
    med_type = models.CharField(max_length=50) #해열,진통,소염제
    med_content = models.TextField()#효능 효과
    take_medicine = models.TextField()#효능 효과

    def __str__(self):
        return self.med_name