import time
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from djangotoolbox.fields import ListField
from django.utils import text
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError


class File(models.Model):
	
	created_date = models.DateTimeField(auto_now_add=True, editable=False)
	modified_date = models.DateTimeField(auto_now=True, editable=False)
	
	slug = models.SlugField()
	
	title = models.CharField(max_length=50)
	
	file = models.FileField(upload_to='files/')
	
	def __unicode__(self):
		return self.title
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = uuid.uuid4()
		super(File, self).save()
	
	def get_absolute_url(self):
		return reverse('file-download', kwargs={'slug': self.slug})
	
	def admin_image(self):
		return self.thumbnail(None, None)
	admin_image.short_description = 'Image'
	admin_image.allow_tags=True
	
	def thumbnail(self, height=100, width=100):
		try:
			return '<img src="{0}" height={1} width={2}>'.format(
				self.get_absolute_url(),
				height,
				width,
				)
		except Exception as e:
			print e
			return 'ack!'
	thumbnail.short_description = 'Thumbnail'
	thumbnail.allow_tags = True
