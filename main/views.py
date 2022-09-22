from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Task
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
# Create your views here.
class TaskView(APIView):
    @api_view(['POST'])
    def get(self,request):
        data=Task.objects.all()
        serializer=TaskSerializer(data, many=True)
        return Response({"Data":serializer.data})
    @api_view(['POST'])
    def post(self,request):
        data=request.data.get('task')
        serializer=TaskSerializer(data=Task)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success":"Task '{}' created succesfuly".format(data)})
def index(request):
    data=Task.objects.all()
    serializer=TaskSerializer(data, many=True)
    if request.method=="POST":
        fullnames=request.POST['fullnames']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        if fullnames=="":
            messages.info(request,"Fullnames cannot be blank")
            return redirect('index')
        elif Task.objects.filter(fullnames=fullnames).exists():
            messages.info(request,'Fullnames Already taken')
            return redirect('index')
        elif email=="":
            messages.info(request,'email cannot be blank')
            return redirect('index')
        elif Task.objects.filter(email=email).exists():
            messages.info(request,'Email Already Exists')
            return redirect('index')

        else:
            user=Task.objects.create(fullnames=fullnames,email=email,phone=phone,address=address)
            user.save()
            return redirect('content')


        
    else:
     return render(request,'main/index.html')
def content(request):
    data=Task.objects.all()
    return render(request,'main/content.html' ,{"data":data})