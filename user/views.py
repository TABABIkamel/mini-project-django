from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
#from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from user.models import Formation
from .filters import FormationFilter


'''class formation_ListView(ListView):
    model = Formation
    template_name = 'ListeFormation.html'
    #Template par defaut: App/projet_list.html
    context_object_name = 'f' '''
@login_required(login_url='login')
def Get_List(request):
    list = Formation.objects.all()
    myFilter=FormationFilter(request.GET,queryset=list)
    list=myFilter.qs
    context = {'f': list,'myFilter':myFilter,'path':"./user/static/"}
    return render(request, 'ListeFormation.html',context)



def login_user(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None and user.is_superuser==False:
            login(request, user)
            return redirect('/user/ListView/')
        elif user is not None and user.is_superuser==True:
            login(request, user)
            return redirect('/admin/user/formation/')
        else:
            messages.info(request,'Username Or Password is incorrect')
            return redirect('login')
    else:
        return render(request,'auth/login.html')
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'auth/signup.html',{'f':form})
def logout_user(request):
    logout(request)
    return redirect('login')


