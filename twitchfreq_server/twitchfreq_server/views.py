from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse("<bleh bleh bleh>")

def highlight(request,video_id = -1):
    if video_id == -1:
        return JsonResponse({'values':[]})
    return JsonResponse({})