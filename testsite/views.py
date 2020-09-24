from django.http import HttpResponse
from ddtrace import tracer
@tracer.wrap()
def hello(request):
  return HttpResponse("Hello from django")
