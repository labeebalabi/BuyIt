from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Property(models.Model):
    place=models.CharField(max_length=200)
    opt = (
        ('kasarkode','kasarkode'),
        ('kannur','kannur'),
        ('kozhikode','kozhikode'),
        ('malappuram','malappuram'),
        ('wayanad','wayanad'),
        ('palakkad','palakkad'),
        ('idukki','idukki'),
        ('thrissur','thrissur'),
        ('eranakulam','eranakulam'),
        ('alappuzha','alappuzha'),
        ('pathanamthitta','pathanamthitta'),
        ('kollam','kollam'),
        ('kottayam','kottayam'),
        ('thiruvananthapuram','thiruvananthapuram')

    )
    district = models.CharField(max_length=100,choices=opt,default='kannur')
    cent=models.IntegerField()
    building = models.BooleanField()
    img=models.ImageField(upload_to="property_image",verbose_name="Property Image_1",default=None)
    img2=models.ImageField(upload_to="property_image",null=True,verbose_name="Property Image_2")
    img3=models.ImageField(upload_to="property_image",null=True,verbose_name="Property Image_3")
    price = models.IntegerField(default=1000)
    date = models.DateField(auto_now_add=True)
    descripton=models.CharField(max_length=500)
    


class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    propery=models.ForeignKey(Property,on_delete=models.CASCADE)
    # class Meta:
    #     unique_together=('user','propery')


class Booking(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     propery=models.ForeignKey(Property,on_delete=models.CASCADE)
     phone=models.IntegerField(null=True)
     price=models.IntegerField(null=True)
     date=models.DateField(auto_now_add=True)

class Broker(models.Model):
    Bname=models.CharField(max_length=100)
    Bplace=models.CharField(max_length=100)
    # img=models.ImageField()
    option = (
        ('kasarkode','kasarkode'),
        ('kannur','kannur'),
        ('kozhikode','kozhikode'),
        ('malappuram','malappuram'),
        ('wayanad','wayanad'),
        ('palakkad','palakkad'),
        ('idukki','idukki'),
        ('thrissur','thrissur'),
        ('eranakulam','eranakulam'),
        ('alappuzha','alappuzha'),
        ('pathanamthitta','pathanamthitta'),
        ('kollam','kollam'),
        ('kottayam','kottayam'),
        ('thiruvananthapuram','thiruvananthapuram')

    )
    Bdistrict = models.CharField(max_length=100,choices=option,default='kannur')
    # Bdistrict=models.CharField(max_length=100)
    Bphone=models.IntegerField(null=True)
    Bage=models.IntegerField(null=True)
    status=models.BooleanField(default=0)