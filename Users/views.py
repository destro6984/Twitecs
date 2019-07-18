from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View



from Users.forms import UserRegistryForm


class Registration(View):
    def get(self,request):
        form= UserRegistryForm()
        return render(request,'users/register.html',context={"form":form})

    def post(self, request):
        form = UserRegistryForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Your Account has been created, You are now able to login')
            return redirect('login')
        else:
            form = UserRegistryForm(request.POST)
        return render(request, 'users/register.html', context={'form': form})


