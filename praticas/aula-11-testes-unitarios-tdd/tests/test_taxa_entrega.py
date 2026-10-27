import pytest

from src.pedido import calcular_taxa_entrega


def test_taxa_inicial_ate_tres_km():
    taxa = calcular_taxa_entrega(2, 50)
    assert taxa == 5


def test_acrescenta_taxa_por_km_excedente():
    taxa = calcular_taxa_entrega(4, 50)
    assert taxa == 7


def test_entrega_gratuita_a_partir_de_cem_reais():
    taxa = calcular_taxa_entrega(5, 100)
    assert taxa == 0


def test_rejeita_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-1, 50)
