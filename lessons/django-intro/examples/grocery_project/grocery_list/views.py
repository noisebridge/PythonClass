from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime

def extreme_basic_view_function(request):   
     return HttpResponse('<html><body>Hello,World!</body></html>')

def better_view_function(request):
    template = loader.get_template('main_list.html')
    context = Context({'current_time': datetime.now(),})
    return HttpResponse(template.render(context))