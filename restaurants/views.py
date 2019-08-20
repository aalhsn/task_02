from django.shortcuts import render

# Create your views here.
def restafood(request):
	context = {
		'msg':"Hello World!",
	}
	return render(request, 'foodpage.html',context)