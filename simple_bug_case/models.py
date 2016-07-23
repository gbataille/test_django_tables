from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TestModels(models.Model):

  dummy_attribute = models.CharField(max_length=100, default='foo')

  def dummy_method(self):
    print("I don't want to see that")
    return 'bar'
