import pytest

from lanchonete.cardapio import Cardapio
from lanchonete.carrinho import Carrinho


@pytest.fixture
def cardapio():
    c = Cardapio()
    c.adicionar_item("X-Burguer", 15.00, "lanche")
    c.adicionar_item("Coca-Cola", 7.00, "bebida")
    c.adicionar_item("Sorvete", 8.00, "sobremesa")
    return c


@pytest.fixture
def carrinho(cardapio):
    return Carrinho(cardapio)
