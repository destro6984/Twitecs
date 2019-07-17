from django.shortcuts import render

# Create your views here.
from django.views import View


class Homepage(View):
    def get(self,request):
        return render(request, 'tweet/Homepage.html')