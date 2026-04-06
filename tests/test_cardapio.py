import pytest

from lanchonete.cardapio import Cardapio


class TestCardapio:

    def test_adicionar_item_valido(self, cardapio):
        item = cardapio.obter_item("X-Burguer")
        assert item["preco"] == 15.00
        assert item["categoria"] == "lanche"

    def test_adicionar_item_preco_zero_levanta_erro(self):
        c = Cardapio()
        with pytest.raises(ValueError, match="Preço deve ser maior que zero"):
            c.adicionar_item("Frango", 0, "lanche")

    def test_adicionar_item_preco_negativo_levanta_erro(self):
        c = Cardapio()
        with pytest.raises(ValueError):
            c.adicionar_item("Frango", -5, "lanche")

    def test_adicionar_item_nome_vazio_levanta_erro(self):
        c = Cardapio()
        with pytest.raises(ValueError, match="Nome do item não pode ser vazio"):
            c.adicionar_item("   ", 10.00, "lanche")

    def test_adicionar_item_categoria_invalida_levanta_erro(self):
        c = Cardapio()
        with pytest.raises(ValueError, match="Categoria inválida"):
            c.adicionar_item("Frango", 10.00, "prato")

    def test_adicionar_item_duplicado_levanta_erro(self, cardapio):
        with pytest.raises(ValueError):
            cardapio.adicionar_item("X-Burguer", 20.00, "lanche")

    def test_remover_item_existente(self, cardapio):
        cardapio.remover_item("Sorvete")
        with pytest.raises(KeyError):
            cardapio.obter_item("Sorvete")

    def test_remover_item_inexistente_levanta_erro(self, cardapio):
        with pytest.raises(KeyError):
            cardapio.remover_item("Pizza")

    def test_listar_itens_retorna_todos(self, cardapio):
        itens = cardapio.listar_itens()
        assert len(itens) == 3
        assert "x-burguer" in itens

    def test_obter_item_inexistente_levanta_erro(self, cardapio):
        with pytest.raises(KeyError):
            cardapio.obter_item("Hot Dog")
