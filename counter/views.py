from django.shortcuts import render

def count(request, form_id):
    
    return render(request, 'count/count.html')