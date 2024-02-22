import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)

def store_index(request):
    result = 'Index page "Online Store Start" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def client(request):
    result = 'Index page "Client" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def product(request):
    result = 'Index page "Product" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def order(request):
    result = 'Index page "Order" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)