from django.conf import settings

def env(request):
    if settings.DEBUG:
        return {'env':'DESIGN'}
    else:
        return {'env':request.GET.get('env','BASE')}    
