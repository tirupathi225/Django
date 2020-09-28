from rest_framework import serializers
from . models import Requirement
from rest_framework.serializers import ValidationError
from cvapp import utils
from .models import Upload





#class UserSerializer(serializers.ModelSerializer):
	#class Meta:
		#model = UserSerializer
		#fields = '__all__'




class RequirementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Requirement
		fields = ('id','skills','designation','experience','location','profile_type','actor')


	# def validate_skills(self,value):
	# 	skill = ['python','java','ruby']
	# 	for skills in skill:
	# 		if skills == skill:
	# 			print(skill)
	# 	return value 
	# 
	# 

class UploadSerializer(serializers.ModelSerializer):
	# files=serializers.(max_length=None, allow_empty_file=False, use_url=True)
	# uploaded_file=request.FILES['files[]']
	# UploadHandler(uploaded_file)
	class Meta:
		model = Upload
		# fields=['id','actor_id','assigned_name','original_name','file_path','file_size','extension','created_at','updated_at']
		fields='__all__'
