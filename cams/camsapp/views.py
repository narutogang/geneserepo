from django.shortcuts import render
#from django.http import HttpResponse
#from camsapp.models import AccessRecord,Webpage,Topic,User
#from . import forms
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout
from camsapp.forms import UserForm,UserProfileInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView,View
from .models import *
from django.urls import reverse,reverse_lazy

def index(request):
    context_dict={'text':'hello world','number':100}
    return render(request, "index.html",context_dict)

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()


            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'registration.html',{'user_form':user_form,
                                                'profile_form':profile_form,'registered':registered})


@login_required
def special(request):
    return HttpResponse("you are logged in")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        member=request.POST.get('member')


        user=authenticate(username=username,password=password,member=member)
        if user:
            if user.is_active:
                auth_login(request,user)
                print("Someone tried to login and failed")
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password: {} and member: {}".format(username,password,member))
            return HttpResponse("Username:{} and password: {} and member: {}".format(username,password,member))
    else:


        return render(request,'login.html',{})


    return render()


def base(request):
    return render(request, "base.html")
def form_name_view(request):
    form=forms.FormName()
    if request.method =='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            #Do something
            print("validation success !")
            print("NAME:"+form.cleaned_data['name'])
            print("EMAIL:"+form.cleaned_data['email'])
            print("NAME:"+form.cleaned_data['member'])
            print("TEXT:"+form.cleaned_data['text'])

    return render(request,'form_page.html',{'form':form})

def home(request):
    return render(request, "home.html",{})

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form= NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')
    return render(request,'registration/users.html',{'form':form})


class FacultyUpdate(UpdateView):
    model = Faculty

    fields = ['specialization','photo']
    template_name = 'update_form.html'
    success_url = reverse_lazy('profile')
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object == request.user.faculty
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('profile')
        return super(FacultyUpdate, self).dispatch(
            request, *args, **kwargs)

class StudentUpdate(UpdateView):
    model = Student
    fields = ['photo','DOB','branch','year','tenth_marks','inter_marks','current_marks']
    template_name = 'update_form.html'
    success_url = reverse_lazy('profile')
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object == request.user.student
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('profile')
        return super(StudentUpdate, self).dispatch(
            request, *args, **kwargs)



class UserUpdate(UpdateView):
    model = User
    slug_field = 'username'
    fields = ['first_name','last_name','email']
    template_name = 'update_form.html'
    success_url = reverse_lazy('index')
    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect('profile')
        return super(UserUpdate, self).dispatch(
            request, *args, **kwargs)

def other(request):
    return render(request,"other.html",{})

def relative(request):
    return render(request,'relative_url_template.html',{})

def about(request):
    return render(request, "about.html",{})

def contact(request):
    return render(request, "contact.html",{})
