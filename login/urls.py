from django.conf.urls import *
from models import *
from views import *
from resources import *

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
)