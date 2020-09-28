# from django.shortcuts import render

# Create your views here.

from . import models
from cvapp.models import Requirement
from rest_framework import response, decorators
from rest_framework import viewsets
from cvapp.serializers import RequirementSerializer
from cvapp.models import Upload
from cvapp.serializers import UploadSerializer
from cvapp import utils
# from rest_framework.serializers import ValidationError


# class UserAuthViewSet(viewsets.GenericViewSet):
#     queryset = User.objects.filter()
#     serializer_class = UserSerializer











class RequirementViewSet(viewsets.GenericViewSet):
    queryset = Requirement.objects.filter() 
    serializer_class = RequirementSerializer
    

    def list(self, request, *args, **kwargs):
        '''
            list works as GET method
        '''
        queryset = self.get_queryset()
        serializer = RequirementSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwargs):
        '''
            create works as POST method
        '''
        user_queryset = self.get_serializer(data=request.data)
        user_queryset.is_valid(raise_exception=True)
        user_queryset.save()
        return response.Response(user_queryset.data)

    def update(self, request, *args, **kwargs):
        '''
            update works as PUT method
        '''
        queryset = self.get_object()
        need_to_save = False

        if 'skills' in request.data:
            queryset.skills = request.data['skills']
            need_to_save = True
        if 'designation' in request.data:
            queryset.designation = request.data['designation']
            need_to_save = True
        if 'experience' in request.data:
            queryset.experience = request.data['experience']
            need_to_save = True
        if 'location' in request.data:
            queryset.location = request.data['location']
            need_to_save = True
        if 'profile_type' in request.data:
            queryset.profile_type = request.data['profile_type']
            need_to_save = True
        if 'actor' in request.data :
            queryset.actor_id = request.data['actor']
            need_to_save = True
        # if 'credits' in request.data:
        #     queryset.credits = request.data['credits']
        #     need_to_save = True
        if need_to_save:
            queryset.save()

        serializer = self.get_serializer(queryset)
        return response.Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        '''
            retrieve works as GET method but it retrieves required data
        '''

        queryset = self.get_object()
        self.serializer_class = RequirementSerializer

        serializer = self.get_serializer(queryset)
        return response.Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        '''
            delete works as DELETE method
        '''
        self.queryset = Requirement.objects.filter()
        queryset = self.get_object()
        queryset.delete()
        serializer = self.get_serializer(queryset)
        return response.Response(serializer.data)

class UploadDetails(viewsets.GenericViewSet):
    queryset = Upload.objects.filter()
    serializer_class = UploadSerializer

    def list(self, request,*args, **kwargs):
        queryset = self.get_queryset()
        serializer = UploadSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request,*args, **kwargs):
        uploaded_file = request.FILES['files[]']
        utils.save(uploaded_file)
        uploaded_file= str(uploaded_file)
        file_path = utils.file_path(uploaded_file)
        file_name = utils.file_name(uploaded_file)
        # file_extension=utils.file_name(uploaded_file)
        file_size = utils.file_size(uploaded_file)
        file_extension = utils.file_extension(uploaded_file)
        assigned_name = utils.assigned_name()
        data={'actor_id':1,'filepath':file_path,'original_name':file_name,'filesize':file_size,'extension':file_extension,'system_name':assigned_name}
        user_queryset = self.get_serializer(data=data)
        user_queryset.is_valid(raise_exception=True)
        user_queryset.save()
        return Response(user_queryset.data)
    















































    # def requirement(request):
    #   actor_id = [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
    #   credits = [2,3,4,5,6,7,8,9,10,11]
    #   if str(request.method) == 'POST':

    #       data = request.data
    #   # for val in range(1000,1050):

    #       req = requirements.objects.create(skills=data['skills'],designation=data['designation'],experience=data['experience'],location=data['location'],profile_type=data['profile_type'],actor_id=random.choice(actor_id),credits=random.choice(credits))
    #   return response.Response('success')





    
#