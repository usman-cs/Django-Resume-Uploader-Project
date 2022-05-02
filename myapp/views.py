from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
# Create your views here.
'''
I can use django-unused-media to delete media file which are deleted from database
'''
def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ResumeForm()
        candidates = Resume.objects.all()
    return render(request,'myapp/home.html',{'form':form,'candidates':candidates})

def candidates(request,pk):
    data = Resume.objects.get(pk=pk)
    return render(request,'myapp/candidate.html',{'data':data})