from django.db import models
from django.utils import timezone
import json

class Students(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    mobile = models.CharField(max_length=12, blank=True)
    dob = models.DateField(null=True,blank=True)

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
