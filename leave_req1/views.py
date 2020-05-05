from django.shortcuts import render,redirect
from .forms import leave_request_form
from .models import leave_request
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.decorators import login_required
@login_required(login_url="/account/login")
def leave_req1(request):
    form = leave_request_form()

    if request.method=='POST':
        form=leave_request_form(data=request.POST)        
        if form.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            start_date=request.POST.get('start_date')
            end_date=request.POST.get('end_date')
            reason=request.POST.get('reason')
            mentor=request.POST.get('mentor')
            mentors=mentor
            subject=username +" wants holiday"
            content="from: "+ start_date +"\nto: "+ end_date +"\nreason: "+reason
            recepient = email
            if mentors=='mentor1':
                send_mail(subject,
                content, 
                recepient,
                ['vimalrajansret@gmail.com'], 
                fail_silently=False)
            elif mentors=="mentor2":
                send_mail(subject,
                content, 
                recepient,
                ['vimalrajan242001@gmail.com'], 
                fail_silently=False)
        msg='mail is sent '+mentors
        messages.info(request,msg)
        return render(request, 'leave.html',{'form':form})


    else:
        return render(request, 'leave.html',{'form':form} )


def homes(request):
    return redirect('/')