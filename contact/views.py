from django.shortcuts import render, HttpResponse
from .forms import ContactForm
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
  
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
          
        if form.is_valid():
            return HttpResponse("Yay! you are human.")
        else:
            print(form.is_valid())
            return HttpResponse("OOPS! Bot suspected.")
            
    else:
        form = ContactForm()
          
    return render(request, 'contact.html', {'form':form})