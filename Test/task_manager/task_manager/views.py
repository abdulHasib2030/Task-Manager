from django.shortcuts import render

def MainHome(request):
  return render(request, 'index.html')