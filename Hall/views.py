from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import hallPresenceSerializer
from Login.models import Profile
from Hall.models import hallPresence
from .form import EntryForm
from .form import ExitForm
from django.contrib.auth.decorators import login_required
import pytz 
# Create your views here.
import datetime
from django.contrib.auth.models import User
from Login.models import Profile
# 
@login_required
def entry_view(request,id):
    if(request.user.profile.is_student==False):
        return HttpResponse("<h1>Page not found</h1>")
    for x in hallPresence.objects.all():
        if (str(x.user) == str(request.user.username) and x.in_hall == True):
            context={"hall_number":x.hall_numnber}
            return render(request,"exit.html",context)
    if request.method == "POST":
        MyLoginForm = EntryForm(request.POST or None)
        if MyLoginForm.is_valid():
            hall_number = id
            user_visiting = int(MyLoginForm.cleaned_data['user_visiting'])
            room_number = MyLoginForm.cleaned_data['room_number']
            laptop=MyLoginForm.cleaned_data['laptop']
            time = datetime.datetime.now()+datetime.timedelta(minutes=330)
            #time = time + datetime.datetime(2000,1,1,5,30) - datetime.datetime(2000,1,1)
            print(time)
            f="False"
            l=False
            if(laptop=='Yes'):
                l=True
            for students in Profile.objects.all():
               if user_visiting == students.roll_no and  room_number == students.room_no and id==students.hall_no:
                    z=hallPresence(hall_numnber=hall_number, user=request.user,user_visiting=user_visiting,in_hall=True,laptop=l,timeEntered=time,first_name = request.user.profile.first_name, last_name = request.user.profile.last_name, roll_no = request.user.profile.roll_no, mobile_no = request.user.profile.mobile_no,room_visiting=room_number)
                    z.save()
                    f="True"
                    break
            context={'hall_number' : id,'credential': f}
            return render(request,"welcome.html",context)
    else:
        MyLoginForm = EntryForm(request.POST or None)
        context = {"form": MyLoginForm,
        "hall_number":id
        }
        return render(request, "entry.html", context)

def security_view(request):
    if(request.user.profile.is_security==False):
        return   HttpResponse("<h1>Page not found</h1>")
    return render(request,"manage_guests.html")

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/'
    }
    return Response(api_urls)

@api_view(['GET'])
def studentlist(request):
    orders = hallPresence.objects.all()
    serializer = hallPresenceSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentdetail(request,pk):
    orders = hallPresence.objects.get(id=pk)
    serializer = hallPresenceSerializer(orders, many=False)
    return Response(serializer.data) 

@api_view(['POST'])
def studentcreate(request):
    serializer = hallPresenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")

@api_view(['POST'])
def studentupdate(request,pk):
    student = hallPresence.objects.get(id=pk)
    serializer = hallPresenceSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    else:
        return Response("ankurs mom")


@api_view(['DELETE'])
def studentdelete(request,pk):
    order = hallPresence.objects.get(id=pk)
    order.delete()
    return Response('mom')