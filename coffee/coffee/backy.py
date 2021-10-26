from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request , 'index.html')

def getvalue(request):
    text1 =request.GET.get('a1', 'default')
    text2 = request.GET.get('a2','default')
    if text1 in "sakshamvedi@gmail.com" and text2 in "vishuindian":
        return render(request , 'homr.html')
    else:
        return HttpResponse("Invalid Login")

def setvalue(request):
    n1 = int(request.GET.get('n1','0'))
    n2 = int(request.GET.get('n2','0'))
    n3 = int(request.GET.get('n3', '0'))
    n4 = int(request.GET.get('n4', '0'))
    n5 = int(request.GET.get('n5', '0'))
    n6 = int(request.GET.get('n6', '0'))
    n7 = int(request.GET.get('n7', '0'))
    n8 = int(request.GET.get('n8', '0'))
    res = n1+n2+n3+n4+n5+n6+n7+n8
    return HttpResponse(res)
