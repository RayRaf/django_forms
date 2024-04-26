from django.shortcuts import render
from .forms import MyForm

# Create your views here.
def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        return render(request, 'result.html', {'name': name, 'email': email, 'message': message})
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})