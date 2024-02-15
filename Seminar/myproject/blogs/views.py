import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

def blogs_index(request):
    result = 'Index page "Blogs Start" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def blogs(request):
    result = 'Index page "Blogs" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def author(request):
    result = 'Index page "Author" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)