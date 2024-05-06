from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from teacher.models import  Teacher, Bia, Tsc,Placements,Course,MenuItem
from teacher.models import Contact,Review



def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "click.html")
def canteen(request):
    menu_items = MenuItem.objects.all()
    return render(request, "canteen.html", {"menu_items": menu_items})

def revi(request, rev):
    return render(request, "review.html")

def contact(request):
    if request.method == "POST":
        language = request.POST.get('language')
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        query = request.POST.get('query')
        
       
        contact = Contact(language=language, name=name, address=address, mobile=mobile, email=email, query=query)
        contact.save()
        
        
        return render(request, "thanks.html")
    
    else:
        
        return render(request, "contact.html")

def course(request):
    Courses = Course.objects.all()
    return render(request, "course.html", {'Course': Courses})





def placement(request):
    placements = Placements.objects.all()
    return render(request, "palcement.html", {'placements': placements})



def review(request):
    if request.method == "POST":
        message = request.POST.get('review_message')
        date = request.POST.get('review_date')
        reviews =Review(review_message=message,review_date=date)
        reviews.save()
        
        return render(request, "reviewsthand.html")
    
    else:
        
        return render(request, "review.html")
def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {'teachers': teachers})
def tsc(request):
    tsc_items = Tsc.objects.all()
    return render(request, "tsc.html", {"tsc": tsc_items})

def bia(request):
    bia_items = Bia.objects.all()
    return render(request, "bia.html", {"bia": bia_items})
def batches(request):
    return render(request, "batches.HTML")




def bt(request, bia):
    return render(request, ["BIA.html", "tsc.html"])




def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            My_user = User.objects.create_user(username=username, email=email, password=password)
            print(My_user)
            return redirect('login')
        except IntegrityError:
            return render(request, "signup.html", {'error_message': 'User with this username or email already exists.'})
    else:
        return render(request, "signup.html")




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return render(request, "index.html")
        else:
            error_message = "Incorrect username or password. Please try again."
            return render(request, "login.html", {'error_message': error_message})
     
    return render(request, "login.html")


def reset(request):
    return render(request, "reset.html")

def forgot(request,forgot):
    return render(request, "reset.html")
    
def logout(request):
    
    auth_logout(request)
    return render(request, "login.html")
def thanks(request):
    return render(request, "thanks.html")    