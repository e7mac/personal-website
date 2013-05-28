# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import *
import os
import inspect
from django.utils.safestring import mark_safe
from models import *

def home(request):
    method = inspect.stack()[0][3]
    return render_to_response(method+'.html', {'title': method,})

def projects(request):
    method = inspect.stack()[0][3]
    projects = Project.objects.all().order_by('-date')
    return render_to_response('grid.html',
                              {'title': method, 'items': projects,},
                              context_instance=RequestContext(request),
                              )

def project_details(request,title):
    method = inspect.stack()[0][3]
    project = Project.objects.get(title=title)
    return render_to_response(method+'.html',
                              {'title': method, 'item': project,},
                              context_instance=RequestContext(request),
                              )

def experiments(request):
    method = inspect.stack()[0][3]
    experiments = Experiment.objects.all().order_by('-date')
    return render_to_response('grid.html', {'title': method, 'items': experiments,})

def experiment_details(request,title):
    method = inspect.stack()[0][3]
    experiment = Experiment.objects.get(title=title)
    return render_to_response(method+'.html',
                              {'title': method, 'item': experiment,},
                              context_instance=RequestContext(request),
                              )

def performances(request):
    method = inspect.stack()[0][3]
    performances = Performance.objects.all().order_by('-date')
    return render_to_response('grid.html', {'title': method,'items':performances,})

def performance_details(request,title):
    method = inspect.stack()[0][3]
    performance = Performance.objects.get(title=title)
    return render_to_response(method+'.html',
                              {'title': method, 'item': performance,},
                              context_instance=RequestContext(request),
                              )


def compositions(request):
    method = inspect.stack()[0][3]
    compositions = Composition.objects.all().order_by('-date')
    return render_to_response('grid.html', {'title': method, 'items': compositions,})

def composition_details(request,title):
    method = inspect.stack()[0][3]
    composition = Composition.objects.get(title=title)
    return render_to_response(method+'.html',
                              {'title': method, 'item': composition,},
                              context_instance=RequestContext(request),
                              )


def installations(request):
    method = inspect.stack()[0][3]
    installations = Installation.objects.all().order_by('-date')
    return render_to_response('grid.html', {'title': method,'items':installations,})

def installation_details(request,title):
    method = inspect.stack()[0][3]
    installation = Installation.objects.get(title=title)
    return render_to_response(method+'.html',
                              {'title': method, 'item': installation,},
                              context_instance=RequestContext(request),
                              )

def publications(request):
    method = inspect.stack()[0][3]
    publications = Publication.objects.all().order_by('-date')
    return render_to_response('grid.html', {'title': method,'items':publications,})

def publication_details(request,title):
    method = inspect.stack()[0][3]
    publication = Publication.objects.get(title=title)
    return render_to_response(method+'.html',
                              {'title': method, 'item': publication,},
                              context_instance=RequestContext(request),
                              )

def classes(request):
    method = inspect.stack()[0][3]
    return render_to_response('grid.html', {'title': method,})

def about(request):
    method = inspect.stack()[0][3]
    return render_to_response(method+'.html', {'title': method,})

def resume(request):
    method = inspect.stack()[0][3]
    return render_to_response(method+'.html', {'title': method,})

def contact(request):
    method = inspect.stack()[0][3]
    return render_to_response(method+'.html', {'title': method})

def links(request):
    method = inspect.stack()[0][3]    
    return render_to_response(method+'.html', {'title': method,})

def music(request):
    method = inspect.stack()[0][3]
    path = os.path.dirname(__file__) + '/../static/music/'
    dirList=os.listdir(path)
    playlist = []
    for file in dirList:
        if file.find('.mp3')!=-1:
            dict = {
                'title':file.rpartition('.mp3')[0],
                'mp3':"http://e7mac.com/static/music/"+file,
                }
            playlist.append(dict)
    return render_to_response(method+'.html', {'title': method,'playlist':mark_safe(playlist),})