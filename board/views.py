from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def boardlist(request):
    print(request.user)
    return render(request,'boardlist.html')