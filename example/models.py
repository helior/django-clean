from django.db import models
import uuid

# Create your models here.

class Example(models.Model):
  id = models.UUIDField(
    primary_key = True,
    default = uuid.uuid4,
    editable = False
  )
  name = models.CharField(max_length=200)
  value = models.DecimalField(
    null=True,
    blank=True,
    unique=False,
    max_digits=11,decimal_places=6, 
  )
  isGoodExample = models.BooleanField()
  image = models.ImageField(upload_to='example-images/%Y/%m/%d/', null=True, blank=True)
  created_on = models.DateTimeField(auto_now_add=True, null=False)
  updated_on = models.DateTimeField(auto_now=True, null=False)
  def __str__(self):
    return '{} ({})'.format(self.name, self.id)

  class Meta:
    verbose_name_plural = "Exampli"
