import random
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'generator/home.html')

def information(request):
    return render(request,'generator/information.html')



def password(request):
    characters = list('abcdefghklmnopqrstuvxyzwj')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHKLMNOPQRSTUVYZJW'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^'))




    length = int(request.GET.get('length',12))
    thepassword  = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
