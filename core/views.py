from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")
    
    
def past_questions(request):
    return render(request, "pastquestions.html")
