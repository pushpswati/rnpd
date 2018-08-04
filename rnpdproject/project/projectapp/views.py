from django.shortcuts import render

from projectapp.models import UploadMedia
from projectapp.serializer import UploadMediaSerializer

from projectapp.serializer import UploadMediaSerializer
from django.http import Http404
from projectapp.models import NumplateResult
from projectapp.models import UploadMedia
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework import generics
from rest_framework.parsers import FileUploadParser, MultiPartParser,JSONParser

from rest_framework import status
import requests
import django_keyerror

class Rnpd_upload(APIView):
    parser_classes = (JSONParser,MultiPartParser,)
    
    def post(self, request, format=None):
        file_obj = request.data['file_name']
        db_obj=UploadMedia.objects.create(file_name=file_obj)
        fi_path=str(db_obj.file_name)
        print("file_name: ",fi_path)
        image_path="/home/sss/Documents/rnpdproject/project/"+fi_path
        files = {'media_file': open(image_path,'rb')}
        url="http://35.227.148.145:8890/api/v1/rnpd"
        payload={"email":"visionrival.ai@gmail.com"}
        r = requests.post(url, files=files,data=payload)
          
        plate_resultdb=NumplateResult.objects.create(image_id=db_obj.id,plate_result=str(r.json()))
        
        print(r.text) 
        print("number palet",plate_resultdb)


        db_obj=UploadMedia.objects.all()
        serializer_data=UploadMediaSerializer(db_obj,many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)

class NumplateResultImageUpload(APIView):
    parser_classes = (JSONParser,MultiPartParser,)
    
    def get(self,request, format=None):
         try:

            image_id=request.query_params["image_id"]
         except:   
            return Response("please send result  or image id")
         
         Response_result=[]
         for upload_numberplate in r.json():
             plate_result={}
             plate_result['result']=upload_numberplate['result']
             plate_result['image_id']=upload_numberplate['image_id']
             print(upload_numberplate['created'])
             
             if not upload_numberplate['requested_reviewers']:
                 plate_result['plate_result']='up12av1234'
             else:
                 plate_result['plate_result']='pendinng'
             if upload_numberplate['created']:
                 plate_result['created_status']='created'
             else:
                 plate_result['created_status']='created_pending'
             Response_result.append(plate_result)
         final_response={"Response_result":Response_result}
          
         return Response_result(final_response)










                          

























