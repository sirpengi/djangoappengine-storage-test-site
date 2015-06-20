from django.conf import settings
from djangoappengine.storage import BlobstoreStorage
from google.appengine.ext.blobstore import create_upload_url


def prepare_upload(request, url, **kwargs):
	return create_upload_url(
		url,
		gs_bucket_name = settings.GOOGLE_CLOUD_STORAGE_BUCKET
	), {}


class GoogleCloudStorage(BlobstoreStorage):
	pass
