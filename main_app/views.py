from django.shortcuts import render, redirect

# Landing page (first page users see)
def landing(request):
    return render(request, "index.html")  # Your designed landing page

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:  # placeholder check
            return redirect("dashboard")
    return render(request, "login.html")

def signup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        location = request.POST.get("location")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        if first_name and email and password:  # placeholder check
            return redirect("dashboard")
    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")
