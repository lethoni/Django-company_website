from django.shortcuts import render_to_response

# Create your views here.
def about(request):
    return render_to_response("about.html")
