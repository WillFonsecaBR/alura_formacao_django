from django.shortcuts import render

def index(request):
    receitas = {
        1: 'Bolo de laranja',
        2: 'Bolo de cenoura',
        3: 'Guizado de frango', 
        4: 'Browne de chocolate'
    }
    
    dados = { 
        'nome_das_receitas' : receitas
    }
    return render(request,'index.html',dados)

def receita(request):
    return render(request,'receita.html')


