from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from user_agents import parse
from redirect.models import Page

def redirector(request, num):
    userAgent = request.META['HTTP_USER_AGENT']
    url = Page.objects.get(number=num)
    urlDict = {}
    urlDict['number'] = url.number
    urlDict['short_url'] = url.short_url
    urlDict['android'] = url.android
    urlDict['ios'] = url.ios
    urlDict['other'] = url.other
    user_agent = parse(userAgent)
    if user_agent.os.family == 'Android':
        return redirect(urlDict['android'])
    elif user_agent.os.family == 'iOS':
        return redirect(urlDict['ios'])
    else:
        return redirect(urlDict['other'])
