from django.shortcuts import render

# Create your views here.
def post_list(request):
    context = {
        'abc': 123,
        'def': 456,

    }
    return render(request, 'blog/post_list.html', context)