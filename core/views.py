from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos </h1>'.format(nome,idade))

def somar(request, valor1, valor2):
    valor3 = ( valor1 + valor2 )
    return HttpResponse('<h1>Soma de  {} e {} é igual à {} </h1>'.format(valor1,valor2,valor3))


