from django.db import models

class PhoneToken(models.Model):
    phone_number = PhoneNumberField(editable=False)
    
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    attempts = models.IntegerField(default=0)
    used = models.BooleanField(default=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    mobile=models.CharField(validators=[phone_regex], blank=True,max_length=10,primary_key=True)

    class Meta:
        unique_together = ('first_name', 'last_name','email','mobile','alt_contact','address','cash_balance','created','updated')
        ordering = ['created']

