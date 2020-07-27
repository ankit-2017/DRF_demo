from django.db import models
import random

def file_dir(instance, filename):
	num = random.randint(0, 100000)
	return '/'.join([str(num)+'_'+filename])

class DetectedFile(models.Model):
	file = models.ImageField(upload_to=file_dir, max_length=255, blank=True, null=True)
	count = models.IntegerField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.file)

# Create your models here.
