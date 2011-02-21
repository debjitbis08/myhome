
def env(request):
	return {'env':request.GET.get('env','BASE')}	
