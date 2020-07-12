from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm
from .models import Report
from .forms import ReportForm
from django.contrib import messages

# from .forms import CompanyForm


def home(request):
    return render(request, 'sale/home.html', {'title':'Home' })

def about(request):
    return render(request, 'sale/about.html', {'title':'About' })

def contact(request):
    return render(request, 'sale/contact.html', {'title':'Contact Us'})
    
def completed(request):
    return render(request, 'sale/completed.html')

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST or None)
        if form.is_valid():
            form.save()
            rep = Report.objects.all()
            messages.success(request, ('Your report has been submitted to Debfocus successfully. Thank you for your feedack. We will get back to you shortly'))
            return render(request, 'sale/completed.html', {'rep':rep} )

    else:
        rep = Report.objects.all()
    return render(request, 'sale/report.html', {'rep':rep, 'title':'Report'} )

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            info = Profile.objects.all()
            messages.success(request, ('Account has been created You will soon hear from us. Thank you'))
            return render(request, 'sale/completed.html', {'info':info } )

    else:
        info = Profile.objects.all()
    return render(request, 'sale/register.html', {'info':info, 'title':'Register'} )

# def get_name(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = (request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return render(request, 'sale/completed.html')

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = NameForm()

    # return render(request, 'sale/register.html', {'form': form})