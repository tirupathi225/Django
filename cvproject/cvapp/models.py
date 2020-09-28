from django.db import models
from django.utils import timezone
import uuid

class AbstractBaseClass(models.Model):
	id= models.UUIDField(
		primary_key=True,
		default=uuid.uuid4,
		editable=False
	)
	created_at= models.DateTimeField(default=timezone.now)
	updated_at= models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

class User(AbstractBaseClass):
	username= models.CharField(
		max_length=255,
		unique=True
	)
	password= models.TextField()
	email= models.EmailField(unique=True)
	reset_code= models.TextField(null=True)
	is_active= models.BooleanField(default=False)
	is_blocked= models.BooleanField(default=True)

	class Meta:
		db_table='users'
		ordering=['-updated_at']

class Requirement(AbstractBaseClass):
	skills= models.TextField()
	designation= models.CharField(max_length=255)
	experience= models.DecimalField(decimal_places=2, max_digits=3)
	location= models.TextField(null=True)
	profile_type= models.CharField(max_length=255)
	actor= models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='requirement_actor',
	)

	class Meta:
		db_table='requirements'
		ordering=['-updated_at']

class Upload(AbstractBaseClass):
	system_name= models.CharField(max_length=255)
	original_name= models.CharField(max_length=255)
	filepath= models.FileField(upload_to='media/')
	extension= models.CharField(max_length=255)
	filesize= models.CharField(max_length=255)
	score= models.DecimalField(decimal_places=2, max_digits=3, default=0)
	actor= models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='uploads_actor'
	)

	class Meta:
		db_table='uploads'
		ordering=['-updated_at']

class UserCredit(AbstractBaseClass):
	user= models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		related_name='user_credit_user'
	)
	available_credit= models.DecimalField(decimal_places=2, max_digits=3, default=0)
	used_credit= models.DecimalField(decimal_places=2, max_digits=3, default=0)
	total_earned_credit= models.DecimalField(decimal_places=2, max_digits=3, default=0)

	class Meta:
		db_table='user_credit'
		ordering=['-updated_at']