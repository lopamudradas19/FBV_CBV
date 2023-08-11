from django.shortcuts import render

# Create your views here.
#FBV for returning String
from django.http import HttpResponse
from django.views.generic import View,TemplateView
def fbv(request):
    return HttpResponse('This FBV string')

#CBV for returning string as a response

class Cbv(View):
    def get(self,request):
        return HttpResponse('<h1>This is CBV string</h1>')

class Cbv_first(View):
    def get(self,request):
        return render(request,'Cbv_first.html')

class Cbv_Temp(TemplateView):
    template_name='temp.html'
    
