from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306231422',
        'name': 'Muhammad Farhan Ramadhan',
        'class': 'PBP A'
    }
    

    return render(request, "main.html", context)