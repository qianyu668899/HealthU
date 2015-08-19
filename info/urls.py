from django.conf.urls import *
from models import *
from views import *
#from djangorestframework.views import ListOrCreateModelView, InstanceModelView
#from resources import *

urlpatterns = patterns('',

    (r'regist/$', info_input_view),

)