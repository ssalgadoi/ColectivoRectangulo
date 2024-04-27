from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            # Tengo que avisar si esta todo esta bien
            return redirect(reverse('contacto')+'?ok')
        else:
        # Tengo que generar un error
            return redirect(reverse('contacto'))
    return render(request, 'contact/contacto.html', { 'form': contact_form })