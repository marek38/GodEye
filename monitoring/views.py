from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import subprocess
import os

def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

# @login_required
# def dashboard_view(request):
#     # Spusti shell skript ak ešte nebeží
#     script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'start_streams.py')
#     try:
#         subprocess.Popen(['bash', script_path])
#     except Exception as e:
#         print("Chyba pri spúšťaní skriptu:", e)

#     return render(request, 'dashboard.html')
