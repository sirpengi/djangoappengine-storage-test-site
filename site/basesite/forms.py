from django.forms import ModelForm
from django.forms.forms import Form
from django.forms import fields

from .models import File


class FileForm(ModelForm):
	
	class Meta:
		model = File
		fields = [ 'file', 'title' ]
