from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from forms import EventForm
from models import Event
from django.contrib.auth.models import User


def home(request):

    context_vars={}
    context_vars.update(csrf(request))
    username = password = state = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                state = "Your account is not active, please contact the support."
        else:
            state = "Your username or password were incorrect."

    template = 'index.html'
    context = RequestContext(request)
    context_vars.update({'state': state})
    return render_to_response(template, context_vars, context_instance=context)


def cal(request):

    args={}
    args.update(csrf(request))

    e = Event.objects.filter(user=request.user)

    args.update({'e': e})

    return render_to_response('cal.html', args, context_instance=RequestContext(request))


def addEvent(request):

    args = {}
    args.update(csrf(request))

    u = get_object_or_404(User, username=request.user)
    status = 0

    #making some fun stuff-----------------------------------------------
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = u
            form.save()
            status = 1

            return HttpResponseRedirect(reverse('cal', ))
    else:
        form = EventForm()
        status = 0

    #packing bags and fly--------------------------------------------------
    args.update({'status': status, 'form': form})
    template = 'addevent.html'
    context = RequestContext(request)
    return render_to_response(template, args, context_instance=context)

