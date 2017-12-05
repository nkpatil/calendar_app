import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Record

@csrf_exempt
def signin(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/cal/')
        else:
            return render(request, 'login.html', {'error': 'Username or password not correct!'})
    else:
         return render(request, 'login.html', {'error':''})

def index(request):
    if request.user.is_authenticated():
        template_name = request.user.last_name
        return render(request, template_name, {'user': request.user})
    else:
        return render(request, 'login.html', {'error': ''})


@csrf_exempt
@login_required(login_url="/cal/login/")
def save_record(request):
    if request.POST:
        try:
            teacher_name = request.POST['teacher_name']
            grade_no = request.POST['grade_no']
            dt = request.POST['date']
            dt = datetime.datetime.strptime(dt, '%m-%d-%Y')
            tm = request.POST['time']
            tm = datetime.datetime.strptime(tm, "%I:%M%p")
            timestamp = str(dt.date()) +" "+ str(tm.time())
            comments = request.POST['comments']
            user = request.user
            record = Record()
            record.user = user
            record.teacher_name = teacher_name
            record.grade = grade_no
            record.timestamp = timestamp
            record.district = user.first_name
            record.comments = comments
            record.save()
            messages.success( request, 'Data saved successfully!' )
            return HttpResponseRedirect("/cal/save_record/")
        except Exception as err:
            messages.error( request, 'Error saving data ({0})'.format(str(err)) )
            return HttpResponseRedirect("/cal/save_record/")
    else:
          query = Record.objects.filter(user=request.user).values()
          data = []
          for i in query:
              obj = {}
              obj['teacher_name'] = i['teacher_name']
              obj['grade'] = i['grade']
              obj['timestamp'] = str(i['timestamp']).split('+')[0]
              data.append(obj)
          return render(request, "calendar.html", {'message':' ', 'data':data})

