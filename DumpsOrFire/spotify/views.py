from django.shortcuts import render
from . import generate_rating as gr

# Create your views here.

def index(request):
    return render(request, 'spotify/index.html')

def home(request):
    context = {}
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if gr.get_track_popularity(user_input) is not None:
            context['rating'] = gr.get_track_popularity(user_input)
            context['image'] = gr.get_track_image(user_input)
        else:
            context['error'] = f"No result with name {user_input} found."

    return render(request, 'spotify/home.html', context)
