from django.db import models

class UploadMedia(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      payload = models.CharField(max_length=10, blank=True,default='')
      file_name = models.FileField(upload_to='documents/')
      
      
      class Meta:
            ordering = ('created',)

class NumplateResult(models.Model):
      plate_result = models.TextField (blank=True,null=True)
      created = models.DateTimeField(auto_now_add=True)
      payload = models.CharField(max_length=10, blank=True,default='')
      result = models.CharField(max_length=100, blank=True, null=True)
      image_id = models.CharField(max_length=300, blank=True, null=True)


      class Meta:
            ordering = ('created',)



