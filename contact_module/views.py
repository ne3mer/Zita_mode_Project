from django.shortcuts import render


# Create your views here.


def contact_us(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contact_module/contact_page.html', {})
