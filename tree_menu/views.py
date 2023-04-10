from django.shortcuts import render


def index_view(request):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='index.html',
                  context=context)


def category_view(request, category):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='index.html',
                  context=context)


def category_object_view(request, category, pk):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='index.html',
                  context=context)

def sc_1(request):
    context={'url_cursor': request.path}
    return render(request=request, template_name='index.html',
                  context=context)