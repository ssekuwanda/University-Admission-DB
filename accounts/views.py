from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, TemplateView, View
from .models import Profile, Apply
from django.contrib.auth.models  import User

from .forms import SignUpForm, UserInformationUpdateForm, ProfileForm, ApplyForm
from .pdf import render_to_pdf
from django.http import HttpResponse
from django.template.loader import get_template


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserInformationUpdateForm
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

class FrontTemplateView(TemplateView):
    template_name = 'front/frontpage.html'

# @login_required
def profile(request):
    form = ProfileForm(request.POST)
    if request.method == 'POST':
        form = ProfileForm(request.POST, files=request.FILES)
        if form.is_valid:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/home')
    return render(request, 'front/profile.html', {'form':form})

def home(request):
    user_name = request.user
    courses = Apply.objects.filter(user=user_name)
    return render(request, 'home.html', {'user_name':user_name, 'courses':courses})

def apply(request):
    form = ApplyForm(request.POST)
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/home')
    return render(request, 'apply.html', {'form':form})
    

def generate_pdf(request, id):
    course = Apply.objects.filter(pk=id)
    import datetime
    today = datetime.datetime.today().strftime('%d-%B-%Y')
    template = get_template('letter.html')
    context = {
        'courses':course,
        'today':today,
    }
    html = template.render(context)
    pdf = render_to_pdf('letter.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")