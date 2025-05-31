from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm  # We'll create this form to handle ticket input

# Home page
def home(request):
    return render(request, 'home.html')


# Sign In View
def signin_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Received login:", username)

        if not User.objects.filter(username=username).exists():
            print("User does not exist")
            return render(request, 'authentication/signin.html', {
                'error': 'User does not exist. Please signup.'
            })

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login successful")
            return redirect('home')  # Redirect to your home/dashboard page
        else:
            print("Incorrect password")
            return render(request, 'authentication/signin.html', {
                'error': 'Incorrect password. Please try again.'
            })

    return render(request, 'authentication/signin.html')


# Sign Up View
def signup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print("Signup attempt:", username, email)

        if User.objects.filter(username=username).exists():
            print("Username already exists")
            return render(request, 'authentication/signup.html', {
                'error': 'Username already exists. Please login.'
            })

        if User.objects.filter(email=email).exists():
            print("Email already exists")
            return render(request, 'authentication/signup.html', {
                'error': 'Email already exists. Please login.'
            })

        if password1 != password2:
            print("Passwords do not match")
            return render(request, 'authentication/signup.html', {
                'error': 'Passwords do not match.'
            })

        User.objects.create_user(username=username, email=email, password=password1)
        print("User created successfully:", username)
        return redirect('signin_page')

    return render(request, 'authentication/signup.html')


# Raise Ticket View
@login_required
def raise_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user      # Auto-assign logged-in user
            ticket.status = 'Open'                 # Auto-set status to Open on creation
            ticket.save()
            return redirect('ticket_history')     # Redirect to ticket history after successful creation
    else:
        form = TicketForm()

    return render(request, 'tickets/raise_ticket.html', {'form': form})


# Ticket History View - list all tickets created by the logged-in user
@login_required
def ticket_history(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'tickets/ticket_history.html', {'tickets': tickets})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def dashboard_view(request):
    user = request.user
    tickets = Ticket.objects.filter(created_by=user).order_by('-created_at')
    return render(request, 'dashboard.html', {'tickets': tickets})
