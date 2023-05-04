from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# class sign_form(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     c_password = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username

class add(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image')
    description = models.TextField()
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.created_by

class contact_us(models.Model):
      First_name = models.CharField(max_length=255)
      Last_name = models.CharField(max_length=255)
      Contact_no = models.IntegerField()
      Email_id = models.EmailField()
      Message = models.TextField()

      def __str__(self):
          return self.First_name
      
class profileimage(models.Model):
     image = CloudinaryField('image')
     nimg  = models.CharField(max_length=266)



