from django.shortcuts import render
import random

# Create your views here.

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz') # initial list of characters
    if request.GET.get('uppercase'): 
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) # extend initial list with CAPITAL letters if uppercase is selected by user
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()')) # extend initial list with special characters is special is selected by user
    if request.GET.get('numbers'):
        characters.extend(list('0123456789')) # extend initial list with numbers if numbers is selected
    length = int(request.GET.get('length',12)) # determine the length of the password, default is 12
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters) # randomise characters in the characters list and store the result in thepassword variable
    return render(request, 'generator/password.html', {'password':thepassword}) # password key is passed into the templates and will return the value stored in the password