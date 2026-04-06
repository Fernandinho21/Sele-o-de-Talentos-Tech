import pytest

from lanchonete.entrega import calcular_taxa_entrega


class TestEntrega:

    def test_entrega_gratis_ate_2km(self):
        assert calcular_taxa_entrega(1.0) == 0.00

    def test_entrega_gratis_exatamente_2km(self):
        assert calcular_taxa_entrega(2.0) == 0.00

    def test_entrega_5_reais_entre_2_e_5km(self):
        assert calcular_taxa_entrega(3.5) == 5.00

    def test_entrega_5_reais_exatamente_5km(self):
        assert calcular_taxa_entrega(5.0) == 5.00

    def test_entrega_10_reais_entre_5_e_10km(self):
        assert calcular_taxa_entrega(8.0) == 10.00

    def test_entrega_10_reais_exatamente_10km(self):
        assert calcular_taxa_entrega(10.0) == 10.00

    def test_acima_de_10km_levanta_erro(self):
        with pytest.raises(ValueError, match="não disponível"):
            calcular_taxa_entrega(11.0)

    def test_distancia_zero_levanta_erro(self):
        with pytest.raises(ValueError, match="maior que zero"):
            calcular_taxa_entrega(0)

    def test_distancia_negativa_levanta_erro(self):
        with pytest.raises(ValueError):
            calcular_taxa_entrega(-3)
