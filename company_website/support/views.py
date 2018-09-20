from django.shortcuts import render_to_response

# Create your views here.

def support(request):
    return render_to_response("support.html")
