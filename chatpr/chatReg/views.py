from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from chatReg.forms import UserCreationForm ,SignupForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.contrib.auth import logout

from django.utils.safestring import mark_safe
import json


from django.http import HttpResponse

from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


from django.template.loader import render_to_string
from .tokens import account_activation_token


from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib.auth.models import auth, User
from chatReg.models import DB,Author
from chatReg.forms import TextArea,AuthorTextArea

from django.core import serializers

from django.forms.models import model_to_dict


 
def index(request):
    if  request.user.is_authenticated:
        logout(request)
    
    return render (request,'index.html')

@cache_control(no_cache=True, must_revalidate=True)
def dashboard(request):
    
    return render (request,'dashboard.html')


@login_required
def chat_index(request):
    return render(request, 'chat/chat_index.html', {})

@login_required
def chat_room(request, room_name):
    form = AuthorTextArea(request.POST)
    def saving_data(request,form):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            
            # check whether it's valid:
            if form.is_valid():
                
                
                # process the data in form.cleaned_data as required
                msg=form.cleaned_data['text']
                print(msg)
                mg = Author(msg=msg,name=request.user.username)
                mg.save()
                print("------------------------------------:",mg)
                # redirect to a new URL:
                
            # if a GET (or any other method) we'll create a blank form
            else:
                form = AuthorTextArea()

    saving_data(request,form)
    
    cUsername= request.user.username
    #db_id=Author.objects.latest('id')
    db_id=Author.objects.all()
   
    db_id=list(db_id)
    print(type(db_id))
    db_msg= "0"#Author.objects.get(id=1)
    #db_msg=str(db_msg)
    #msg.get(username=request.username)

  
    #template_name = '/home/admin1/Documents/Durganath/django/django projects/chatpr/chatReg/templates/chat/room.html'
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'cUsername': mark_safe(json.dumps(cUsername)),
        'db_msg': mark_safe(json.dumps(str(User))),



        'AuthorTextArea':AuthorTextArea
    })



def signup(request):


    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account '
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render (request,'signup_complete.html')
           
            #return HttpResponse('<h3>Please confirm your email address to complete the registration</h3> <br><a href="gmail.com"> Confirm </a><br><a href="{% url "login_url" %}">Login</a>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
