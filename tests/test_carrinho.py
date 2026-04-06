import pytest

from lanchonete.carrinho import Carrinho


class TestCarrinho:

    def test_adicionar_item_valido(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 2)
        itens = carrinho.listar_itens()
        assert itens["x-burguer"]["quantidade"] == 2

    def test_adicionar_item_inexistente_levanta_erro(self, carrinho):
        with pytest.raises(KeyError):
            carrinho.adicionar_item("Tapioca")

    def test_adicionar_quantidade_zero_levanta_erro(self, carrinho):
        with pytest.raises(ValueError, match="Quantidade deve ser pelo menos 1"):
            carrinho.adicionar_item("X-Burguer", 0)

    def test_adicionar_mesmo_item_duas_vezes_acumula(self, carrinho):
        carrinho.adicionar_item("Coca-Cola", 1)
        carrinho.adicionar_item("Coca-Cola", 2)
        assert carrinho.listar_itens()["coca-cola"]["quantidade"] == 3

    def test_remover_item_do_carrinho(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 3)
        carrinho.remover_item("X-Burguer", 1)
        assert carrinho.listar_itens()["x-burguer"]["quantidade"] == 2

    def test_remover_quantidade_exata_remove_item(self, carrinho):
        carrinho.adicionar_item("Sorvete", 1)
        carrinho.remover_item("Sorvete", 1)
        assert "sorvete" not in carrinho.listar_itens()

    def test_remover_mais_do_que_tem_levanta_erro(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 1)
        with pytest.raises(ValueError, match="Não é possível remover"):
            carrinho.remover_item("X-Burguer", 5)

    def test_remover_item_nao_presente_levanta_erro(self, carrinho):
        with pytest.raises(KeyError):
            carrinho.remover_item("Sorvete")

    def test_calcular_subtotal_correto(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 2)
        carrinho.adicionar_item("Coca-Cola", 1)
        assert carrinho.calcular_subtotal() == 37.00

    def test_subtotal_carrinho_vazio(self, carrinho):
        assert carrinho.calcular_subtotal() == 0.00

    def test_cupom_10_porcento(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 2)
        desconto = carrinho.aplicar_cupom("LANCHE10")
        assert desconto == 3.00

    def test_cupom_20_porcento(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 2)
        desconto = carrinho.aplicar_cupom("LANCHE20")
        assert desconto == 6.00

    def test_cupom_invalido_levanta_erro(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 1)
        with pytest.raises(ValueError, match="inválido ou expirado"):
            carrinho.aplicar_cupom("DESCONTO99")

    def test_total_com_desconto_e_entrega(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 2)
        total = carrinho.total_com_desconto("LANCHE10", taxa_entrega=5.00)
        assert total == 32.00

    def test_total_sem_cupom(self, carrinho):
        carrinho.adicionar_item("Coca-Cola", 2)
        total = carrinho.total_com_desconto(taxa_entrega=5.00)
        assert total == 19.00

    def test_esvaziar_carrinho(self, carrinho):
        carrinho.adicionar_item("X-Burguer", 1)
        carrinho.esvaziar()
        assert carrinho.listar_itens() == {}
