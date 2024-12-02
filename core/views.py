from django.shortcuts import render
from django.http import HttpResponse
from .models import AlumniModel, StudentModel, Both
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def signup(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect(home)
    
    if request.method == 'POST':
        userType = request.POST['userType']
        fullname = request.POST['fullname']
        university = request.POST['university']
        dept = request.POST['dept']
        student_id = request.POST['student_id']
        email = request.POST['email']
        if userType == 'alumni':
            graduation_year = request.POST['graduation_year']
            company = request.POST['company']
            job_title = request.POST['job_title']
            linkedin = request.POST['linkedin']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if not email or not pass1 or not pass2:
            messages.warning(request, 'Please fill in all the fields.')
            return redirect('signup')
        
        if pass1 != pass2:
            messages.warning(request, 'Passwords do not match.')
            return redirect('signup')
        elif len(pass1) < 8:
            messages.warning(request, 'Password must be at least 8 characters long.')
            return redirect('signup')
        elif Both.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists.')
            return redirect('signup')
        else:
            both = Both.objects.create(email=email, password=pass1)
            both.save()

            user = User.objects.create_user(username=email, email=email, password=pass1)
            user.save()

            if userType == 'alumni':
                AlumniModel.objects.using('alumni').create(full_name=fullname, university=university, dept=dept, student_id=student_id, email=email, graduation_year=graduation_year, company=company, job_title=job_title, linkedin=linkedin)
            elif userType == 'student':
                StudentModel.objects.using('student').create(full_name=fullname, university=university, dept=dept, student_id=student_id, email=email)
            
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('signin')
    return render(request, 'authentication/signup.html')

def signin(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect(home)
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        if not email or not password:
            messages.warning(request, 'Please fill in all the fields.')
            return redirect('signin')
        
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect(home)
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('signin')
    return render(request, 'authentication/login.html')

def signout(request):
    logout(request)
    return redirect(signin)

def search_alumni(request):
    if request.method == 'GET':
        university = request.GET.get('university')
        dept = request.GET.get('dept')
        company = request.GET.get('company')
        job_title = request.GET.get('job_title')
        randomKey = request.GET.get('randomKey')
        
        alumni = AlumniModel.objects.using('alumni').all()
        
        if university:
            alumni = alumni.filter(university__icontains=university)
        
        if dept:
            alumni = alumni.filter(dept__icontains=dept)
        
        if company:
            alumni = alumni.filter(company__icontains=company)
        
        if job_title:
            alumni = alumni.filter(job_title__icontains=job_title)

        if randomKey:
            if alumni.filter(university__icontains=randomKey).exists():
                alumni = alumni.filter(university__icontains=randomKey)
            
            if alumni.filter(dept__icontains=randomKey).exists():
                alumni = alumni.filter(dept__icontains=randomKey)
            
            if alumni.filter(company__icontains=randomKey).exists():
                alumni = alumni.filter(company__icontains=randomKey)

            if alumni.filter(job_title__icontains=randomKey).exists():
                alumni = alumni.filter(job_title__icontains=randomKey)
        
        return render(request, 'core/alumni_list.html', {'alumni_list': alumni})
    return render(request, 'core/find_alumni.html')

def find_alumni(request):
    return render(request, 'core/find_alumni.html')
        

def gallery(request):
    return render(request, 'core/gallery.html')

def view_events(request):
    # all_events = events.objects.all()
    # return render(request, 'core/event.html', {'events': all_events})
    return

def add_event(request):
    # if request.method == 'POST':
    #     title = request.POST.get('eventTitle')
    #     description = request.POST.get('eventDes')
    #     date = request.POST.get('eventDate')
    #     time = request.POST.get('eventTime')
    #     regLink = request.POST.get('eventRegLink')
    #     location = request.POST.get('eventLocation')
    #     image = request.FILES.get('eventImage')
        
    #     event = events(user=request.user, title=title, description=description, date=date, time=time, regLink=regLink ,location=location, image=image)
    #     event.save()
    #     messages.success(request, 'Event added successfully.')
        
    #     return redirect('profile')
    # return render(request, 'core/create_event.html')
    return

def edit_event(request, id):
    # event = events.objects.get(id=id)
    # if request.method == 'POST':
    #     title = request.POST.get('eventTitle')
    #     description = request.POST.get('eventDes')
    #     date = request.POST.get('eventDate')
    #     time = request.POST.get('eventTime')
    #     regLink = request.POST.get('eventRegLink')
    #     location = request.POST.get('eventLocation')
        
    #     if 'eventImage' in request.FILES:
    #         # Delete the old image
    #         if event.image:
    #             old_image_path = os.path.join(settings.MEDIA_ROOT, event.image.name)
    #             if os.path.exists(old_image_path):
    #                 os.remove(old_image_path)

    #         # Save the new image
    #         event.image = request.FILES['eventImage']
        
    #     event.title = title
    #     event.description = description
    #     event.date = date
    #     event.time = time
    #     event.regLink = regLink
    #     event.location = location
    #     event.save()
    #     messages.success(request, 'Event updated successfully.')
        
    #     return redirect('profile')
    # return render(request, 'core/edit_event.html', {'event': event})
    return

def delete_event(request, id):
    # event = events.objects.get(id=id)
    # event.delete()
    # messages.success(request, 'Event deleted successfully.')
    # return redirect('profile')
    return

def event_detail(request, id):
    # event = events.objects.get(id=id)
    # return render(request, 'core/event_details.html', {'event': event})
    return

def alumni_list(request):
    return render(request, 'core/alumni_list.html')

def profile(request):
    user = request.user
    email = user.email

    # Get events associated with the user
    # my_event = events.objects.filter(user=user)

    isAlumni = False
    details = None  # Initialize details

    if user.is_superuser:
        # Superuser case: fetch superuser details
        details = User.objects.get(username=user)
        return render(request, 'core/user_profile.html', {'details': details})

    try:
        # Check if the user is in the Alumni database
        details = AlumniModel.objects.using('alumni').get(user=user)
        isAlumni = True
    except AlumniModel.DoesNotExist:
        try:
            # If not an alumni, check if the user is a student
            details = StudentModel.objects.using('student').get(user=user)
        except StudentModel.DoesNotExist:
            # If no record exists, handle it appropriately (perhaps show a message)
            details = None

    # Render the profile page with the fetched details
    if details:
        return render(request, 'core/user_profile.html', {'details': details, 'isAlumni': isAlumni, 'events': my_event})
    else:
        # Handle case when no details are found (if necessary)
        return render(request, 'core/user_profile.html', {'message': "User details not found"})
    

def update_profile(request):
    user = request.user
    email = user.email
    isAlumni = False
    if AlumniModel.objects.user('alumni').filter(email=email).exists():
        isAlumni = True
        details = AlumniModel.objects.user('alumni').get(user=user)
        if request.method == 'POST':
            details.full_name = request.POST.get('full_name')
            details.university = request.POST.get('university') 
            details.dept = request.POST.get('dept')
            details.student_id = request.POST.get('student_id')
            details.email = details.email
            details.graduation_year = request.POST.get('graduation_year')
            details.company = request.POST.get('company')
            details.job_title = request.POST.get('job_title')
            details.linkedin = request.POST.get('linkedin')
            user.first_name = details.full_name
            
            if 'image' in request.FILES:
                old_image_path = os.path.join(settings.MEDIA_ROOT, details.image.name)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
                details.image = request.FILES.get('image')
            details.save()
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        return render(request, 'core/update_profile.html', {'details': details, 'isAlumni': isAlumni})
    else:
        details = StudentModel.objects.using('student').get(user=user)
        if request.method == 'POST':
            details.full_name = request.POST.get('full_name')
            details.university = request.POST.get('university') 
            details.dept = request.POST.get('dept')
            details.student_id = request.POST.get('student_id')
            details.email = details.email
            if 'image' in request.FILES:
                old_image_path = os.path.join(settings.MEDIA_ROOT, details.image.name)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
                details.image = request.FILES.get('image')
            details.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        return render(request, 'core/update_profile.html', {'details': details, 'isAlumni': isAlumni})
    
    return render(request, 'core/update_profile.html')
