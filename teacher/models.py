from django.db import models



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='teachers/profiles/')
    
    
    
class Bia(models.Model):
    name = models.CharField(max_length=100)
  
    address = models.CharField(max_length=200)
    email = models.EmailField()
    year = models.IntegerField()
    batch_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='bia/profiles/')  

    def __str__(self):
        return self.name



class Tsc(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='tsc/profiles/')  
 
    address = models.CharField(max_length=200)
    email = models.EmailField()
    year = models.IntegerField()
    batch_name = models.CharField(max_length=100)
   


    def __str__(self):
        return self.name
    
    
    
    
class Placements(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    package = models.CharField(max_length=50)
    email = models.EmailField()
    batch_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')

    def __str__(self):
        return self.name    
    
    
    
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name    
    
   

class MenuItem(models.Model):
    DAY_CHOICES = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    breakfast = models.CharField(max_length=100, blank=True)
    lunch = models.CharField(max_length=100, blank=True)
    tea = models.CharField(max_length=100, blank=True)
    dinner = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.day} Menu"   
    
    
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    query = models.TextField()
    language_choices = [
        ('english', 'English'),
        ('hindi', 'Hindi')
    ]
    language = models.CharField(max_length=10, choices=language_choices)

    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    review_message = models.TextField()
    review_date = models.DateField()

    def __str__(self):
        return self.review_message    
    