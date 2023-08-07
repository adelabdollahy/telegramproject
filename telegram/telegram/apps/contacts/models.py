from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    related_account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='related_account',
                                        null=True,blank=True)
    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='owner', null=True, blank=True)


