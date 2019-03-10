from django.http import HttpResponse,JsonResponse
from django.template import Context,loader
def index(request):
    templ = loader.get_template('index.html')
    return HttpResponse(templ.render())
    #return render_to_response('templates/index.html')

def highlight(request,video_id = -1):
    if video_id == -1:
        return JsonResponse({'values':[]})
    return JsonResponse({'values':[]})
