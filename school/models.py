from django.db import models

# Create your models here.

class Pupil(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    age=models.BigIntegerField(default=6)
    class_name=models.CharField(max_length=6,default='1A')
    monday=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    tuesday=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    thursday=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    wednesday=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    friday=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    saturday=models.PositiveBigIntegerField(null=True,blank=True,default=0)

    weekly=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    monthly=models.PositiveBigIntegerField(null=True,blank=True,default=0)
    year=models.PositiveBigIntegerField(null=True,blank=True,default=0)


   


    class Meta:
        ordering=['id']
        verbose_name="Maktab o'quvchilari"
        verbose_name_plural="Maktab o'quvchilari"

    def __str__(self):
        return f"{self.name} {self.surname} {self.class_name}" 
    
    def get_week(self):
        return self.monday+self.tuesday+self.thursday+self.wednesday+self.friday+self.saturday
    
    def get_month(self):
        return self.get_week()*4+ self.monday+self.tuesday+self.thursday
    
    def get_year(self):
        return self.get_week()*51+ self.monday+self.tuesday+self.thursday
    
