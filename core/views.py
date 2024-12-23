from django.shortcuts import render, redirect
from .models import Cliente, Produto, Venda
from .forms import ClienteForm, ProdutoForm, VendaForm


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def cliente_form(request, id=None):
    cliente = Cliente.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})


def produto_list(request):
    produto = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produto})


def produto_form(request, id=None):
    produto = Produto.objects.get(Produto, id=id) if id else None
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})

def vendas(request):
    vendas = Venda.objects.all()

    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendas')
    else:
        form = VendaForm()

    return render(request, 'vendas.html', {'vendas': vendas, 'form': form})


from django.shortcuts import render

# Create your views here.
