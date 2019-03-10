from django.http import HttpResponse,JsonResponse
from django.template import Context,loader
from .lib.algo_plus_chat.main import get_vid_data

def index(request):
    templ = loader.get_template('index.html')
    return HttpResponse(templ.render(request=request))
    #return render_to_response('templates/index.html')

def highlight(request,video_id = -1):
    if video_id == -1:
        return JsonResponse({'values':[]})
    print("OBTAINING INFO FOR "+str(video_id))
    timestamps = get_vid_data(str(video_id))
    return JsonResponse(timestamps)