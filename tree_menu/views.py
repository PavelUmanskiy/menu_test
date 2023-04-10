from django.shortcuts import render


def index_view(request):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='index.html',
                  context=context)


def profile_view(request):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='profile.html',
                  context=context)

def contacts_view(request):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='contacts.html',
                  context=context)

def all_categories_view(request):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='all_categories.html',
                  context=context)

def category_view(request, category):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='category.html',
                  context=context)

def category_object_view(request, category, pk):
    context = {'url_cursor': request.path}
    return render(request=request, template_name='category_object.html',
                  context=context)