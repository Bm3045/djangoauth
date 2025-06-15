from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout



from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile'):
                if user.profile.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                else:
                    return redirect('patient_dashboard')
            else:
                messages.error(request, "User has no profile.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')



@login_required
def doctor_dashboard(request):
    user = request.user
    profile = user.profile  # Access extended profile fields
    return render(request, 'doctor_dashboard.html', {'user': user, 'profile': profile})

@login_required
def patient_dashboard(request):
    try:
        profile = request.user.profile
        return render(request, 'patient_dashboard.html', {
            'user': request.user,
            'profile': profile
        })
    except Profile.DoesNotExist:
        return render(request, 'error.html', {'message': 'Profile not found.'})


def logout_view(request):
    logout(request)
    return redirect('login')

    








