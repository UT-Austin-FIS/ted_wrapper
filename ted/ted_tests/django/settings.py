from mock import Mock
import os

from django.http import HttpResponse

SECRET_KEY = 'jFnpiAhD6pXvfajZansAZcvatocJGfnIF2Q43XSz5fVfW7Jk'

TED_EID = Mock()
TED_PASSWORD = Mock()
TED_HOSTNAME = Mock()
filepath, extension = os.path.splitext(__file__)
ROOT_URLCONF = os.path.basename(filepath)

urlpatterns = []
