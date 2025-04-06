# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


from student_management_app.EmailBackEnd import EmailBackEnd

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Require at least 1 uppercase, 1 lowercase, 1 digit, 1 special char
        if not any(c.isupper() for c in password):
            raise ValidationError(_("Password must contain at least 1 uppercase letter."))
        if not any(c.islower() for c in password):
            raise ValidationError(_("Password must contain at least 1 lowercase letter."))
        if not any(c.isdigit() for c in password):
            raise ValidationError(_("Password must contain at least 1 digit."))
        if not any(c in '!@#$%^&*()_+' for c in password):
            raise ValidationError(_("Password must contain at least 1 special character (!@#$%^&*)."))

def get_help_text(self):
        return _("Your password must contain 1 uppercase, 1 lowercase, 1 digit, and 1 special character.")

def anomaly_detect(request):
    return render(request, 'detect_anomalies.html')

def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'login.html')



def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


