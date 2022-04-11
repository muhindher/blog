from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from PIL import Image
from datetime import datetime
# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')
	phone_no=models.CharField(max_length=20,null=True)
	dateofbirth=models.DateField(null=True,default=datetime.now())
	address=models.CharField(max_length=100,null=True)


	@receiver(post_save, sender=User) #add this
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User) #add this
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

	def __str__(self):
		return self.user.username

	#Image Resize to 300 height and 300 width
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args,**kwargs)

		img=Image.open(self.image.path)

		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)










