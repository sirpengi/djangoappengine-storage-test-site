import datetime

from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import edit
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.utils import text
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from filetransfers.api import prepare_upload
from filetransfers.api import serve_file

from .models import File

from .forms import FileForm


class FileList(ListView):
	
	model = File
	paginate_by = 20


class FileUpload(edit.View):
	
	template_name = 'basesite/file_upload_form.html'
	view_url = reverse_lazy('file-upload')
	
	def get(self, request):
		upload_url, upload_data = prepare_upload(request, '/files/add/', private=True)
		form = FileForm()
		return render(request, self.template_name,
			{'form': form, 'upload_url': upload_url, 'upload_data': upload_data}
			)
	
	def post(self, request):
		form = FileForm(request.POST, request.FILES)
		file = form.save(commit=False)
		file.owner = request.user
		file.save()
		return HttpResponseRedirect(self.view_url)


class FileInfo(View):

	template_name = 'basesite/file_info.html'

	def get(self, request, slug):
		file = get_object_or_404(File, slug=slug)
		gs_key = file.file.name.split('/', 3)[3]

		return render(request, self.template_name,
			{'file': file, 'gs_key': gs_key}
			)
