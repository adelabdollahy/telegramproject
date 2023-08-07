from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    reference_id = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    bio = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.reference_id



