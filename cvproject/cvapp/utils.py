from django.core.files.storage import FileSystemStorage
from os.path import splitext
import datetime
from cvapp.models import Upload
import os
from datetime import datetime
import random
from django.conf import settings

def save(uploaded_file):
	fs=FileSystemStorage()
	data= fs.save(
		uploaded_file.name,
		uploaded_file
	)
	return True
def file_path(uploaded_file):
	return settings.MEDIA_ROOT+'/'+str(uploaded_file)
def file_size(uploaded_file):
	return os.path.getsize(settings.MEDIA_ROOT+'/'+str(uploaded_file))
def file_name(uploaded_file):
	# print(uploaded_file,'-----uplodaed file',type(uploaded_file),'---')
	file_name= (uploaded_file.split('/')[-1]).split('.')[0]

	return file_name
def file_extension(uploaded_file):
	file_extension= uploaded_file.split('/')[-1]
	return file_extension
def assigned_name():
	now = datetime.now()
	timestamp = datetime.timestamp(now)
	date_time = datetime.fromtimestamp(timestamp)
	assigned_name = date_time.strftime("%c")
	return assigned_name