from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def menu(request):
    return render(request, 'menu.html')
def about(request):
    return render(request, 'about.html')
def book(request):
    return render(request, 'book.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def cart(request):
    return render(request, 'cart.html')