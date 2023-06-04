from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from contacts.models import Contact
from cars.models import Cars
from django.contrib.auth.decorators import login_required
# Create your views here.


def LogIn(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('accounts:DashBoard')
        else:
            messages.error(request, 'Invalid email or password!')
            return redirect('accounts:LogIn')
    return render(request, 'accounts/login.html')


def SignUp(request):

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Password doesn't match!")
            return redirect('accounts:SignUp')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('accounts:SignUp')
            else:

                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('accounts:SignUp')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, email=email)
                    user.save()
                    messages.success(request, 'Successfully registered!')
                    return redirect('accounts:LogIn')
    return render(request, 'accounts/signup.html')

def LogOut(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, 'Successfully logged out.')
		return redirect('accounts:LogIn')
	else:
		return redirect('accounts:LogIn')
	return redirect('accounts:LogIn')
    
@login_required(login_url='accounts:LogIn')
def DashBoard(request):

    user = User.objects.get(id=request.user.id)
    inquiry = Contact.objects.filter(user_id=request.user.id)
    
    context = {
        'user':user,
        'inquiry' : inquiry,
    }
    return render(request, 'accounts/dashboard.html', context)