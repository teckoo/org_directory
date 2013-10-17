from django.db import models
import localflavor.us.models as us


class Organization(models.Model):
    primary_name = models.CharField(max_length=256, unique=True, 
        help_text="This name will appear on the directory list.")
    secondary_name = models.CharField(max_length=256, blank=True, null=True)
    phone = us.PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fax = us.PhoneNumberField(blank=True, null=True)
    address_1 = models.CharField(max_length=256, blank=True, null=True)
    address_2 = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    state = us.USStateField(blank=True, null=True)
    def __unicode__(self):
        return self.primary_name


class Person(models.Model):
    primary_name = models.CharField(max_length=256, 
        help_text="This name will appear on the directory list.")
    secondary_name = models.CharField(max_length=256, blank=True, null=True,
        help_text="This name only appears on the detail page.")
    phone = us.PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address_1 = models.CharField(max_length=256, blank=True, null=True)
    address_2 = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    state = us.USStateField(blank=True, null=True)
 
    def __unicode__(self):
        return self.primary_name 


class Group(models.Model):
    primary_name = models.CharField(max_length=256,
        help_text="This name will appear on the directory list.")
    secondary_name = models.CharField(max_length=256, blank=True, null=True,
        help_text="This name only appears on the detail page.")
    parent_group = models.ForeignKey('Group', blank=True, null=True)
    leaders = models.ManyToManyField('Person', related_name="leaders", 
        blank=True, null=True) 
    memebers = models.ManyToManyField('Person', related_name="members", 
        blank=True, null=True)

    def __unicode__(self):
        return self.primary_name

#class Directory(models.Model):
#    """
#
#    """
#    pass
