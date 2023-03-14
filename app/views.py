from django.shortcuts import render

# Create your views here.
def csk(request):
    d={'a':1000,'b':2000,'c':3000}
    return render(request,'first.html',context=d)

def gt(request):
    d={'a':'THILAK','b':'CHANDHRA'}
    return render(request,'second.html',context=d)