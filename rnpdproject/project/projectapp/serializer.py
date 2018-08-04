from rest_framework import serializers
from projectapp.models import UploadMedia
from projectapp.models import NumplateResult

class UploadMediaSerializer(serializers.ModelSerializer):
     class Meta:
          model=UploadMedia
          fields=('id','created','payload','file_name')  

class NumplateResultSerializer(serializers.ModelSerializer):
     class Meta:
          model=NumplateResult
          fields=('id','created','plate_result','payload','result','image_id')
