from django.shortcuts import render_to_response

# Create your views here.
def technologies(request):
    return render_to_response('technologies.html')