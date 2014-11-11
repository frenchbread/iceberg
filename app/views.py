from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response


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
