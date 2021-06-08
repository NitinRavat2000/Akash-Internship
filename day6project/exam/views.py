from django.shortcuts import render
from django.http import HttpResponse

def showTest(request):
    que="Who devloed c language"
    a="Ken thompson"
    b="Nitin Ravat"
    c="Ravi Chavada"
    d="Chirag Prajapati"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/test.html',data)
    return res


def showResult(request):
    s="<h1> this is showResult  Page</h1>"
    return HttpResponse(s)



    # Create your views here.
