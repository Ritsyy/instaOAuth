from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))
	# token= request.backend.do_auth(request.GET.get('access_token'))
	# print token