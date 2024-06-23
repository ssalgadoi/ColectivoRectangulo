from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from history.models import Post as HistoryPost
from .forms import ContactForm

def home(request):
    history_posts = HistoryPost.objects.all()
    posts = HistoryPost.objects.all()
    contact_form = ContactForm()  # Instancia del formulario de contacto
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, '¡El mensaje se ha enviado correctamente!')
            # Redirige a la sección de contacto dentro de la vista home
            return redirect(reverse('home') + '#contacto')
        else:
            messages.error(request, '¡El mensaje no ha podido ser enviado. Por favor, intente más tarde.')
            # Renderiza nuevamente la página con el formulario y los mensajes de error
            return render(request, 'core/home.html', {'history_posts': history_posts, 'posts': posts, 'contact_form': contact_form})
    
    # Renderiza la página por primera vez con el formulario inicializado
    context = {
        'history_posts': history_posts,
        'posts': posts,
        'contact_form': contact_form,
    }
    return render(request, "core/home.html", context)
