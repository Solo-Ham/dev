from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from .utils import verify_user
from .models import StoreOTP
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            verify_user(user.email)
            #login(request, user)
            #return redirect('vaccines:vacs')
            return redirect('registration:confirm')

    return render(request, 'registration/regform.html', {'form': form})

@csrf_exempt
def confirm_email(request):
    if request.method == 'POST':
        sent_code = request.POST.get('code')
        try:
            stored = StoreOTP.objects.get(code=sent_code)
            #print(stored.owner)
            print(sent_code)
            user = User.objects.get(username=stored.owner)
            print(user.email)
            if not user.is_active:
                user.is_active = True
                user.save()
            #stored.owner.is_active = True
            #print(stored.owner.email)

            login(request, user)
            return redirect('registration:login')
        except StoreOTP.DoesNotExist:
            print('Try again')

    return render(request, 'registration\confirm.html', {})