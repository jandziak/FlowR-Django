from django.shortcuts import render
from django.http import HttpResponse
from .models import Box, Specification
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from .Algorithms.Helps import *


def index(request):
    box_list = Box.objects.order_by('name')[:5]
    template = loader.get_template('RBlocks/index.html')
    context = {
        'box_list': box_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, type_id):
    try:
        box = Box.objects.get(pk=type_id)
    except Box.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'RBlocks/detail.html', {'name': box})


def start_page_2(request):
    print(request.method)
    if request.method == "POST":
        data_load(request)
        return render(request, 'RBlocks/index.html')
    return render(request, 'RBlocks/index2.html', {"xa": "xaxa"})


def results(request, type_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % type_id)


def vote(request, type_id):
    return HttpResponse("You're voting on question %s." % type_id)


def data_load(request):
    print(os.getcwd())
    path = 'C:\\Users\\iWindows\\Desktop\\Python Prudential\\input\\'
    print([request.POST['train_data'], request.POST['test_data']])
    if request.POST['train_data'] and request.POST['test_data']:
        # from .Algorithms.Helps import load_data, transform_data, fit_xgb_model,
        train, test = load_data(path + request.POST['train_data'], path + request.POST['test_data'])
        train, test = transform_data(train, test)
        model, xgtrain = fit_xgb_model(train, test, [0.5*200])
        offsets = train_offset(model, xgtrain, train)
        make_submission(test, model, offsets, test)


