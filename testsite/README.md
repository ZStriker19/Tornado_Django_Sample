 curl http://localhost:8080/hello-tornado

 curl http://localhost:8080/hello-other-tornado

this one creates the tornado -> django trace 
 curl http://localhost:8080/hello-django


run it with:
PYTHONPATH=. DJANGO_SETTINGS_MODULE=testsite.settings DATADOG_TRACE_DEBUG=true DD_LOGGING_RATE_LIMIT=0 testsite/tornado_main.py