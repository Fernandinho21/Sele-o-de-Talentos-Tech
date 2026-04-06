from lanchonete.cardapio import Cardapio

CUPONS = {
    "LANCHE10": 0.10,   # 10% de desconto
    "LANCHE20": 0.20,   # 20% de desconto
    "FRETE0":   0.00,   # cupom só de frete (sem desconto no subtotal)
}


class Carrinho:
    def __init__(self, cardapio: Cardapio):
        self._cardapio = cardapio
        self._itens = {}  # nome -> {preco, quantidade}

    def adicionar_item(self, nome: str, quantidade: int = 1):
        """
        Regra: quantidade deve ser >= 1.
        Item deve existir no cardápio.
        """
        if quantidade < 1:
            raise ValueError("Quantidade deve ser pelo menos 1.")
        item = self._cardapio.obter_item(nome)  # lança KeyError se não existir
        nome = nome.strip().lower()
        if nome in self._itens:
            self._itens[nome]["quantidade"] += quantidade
        else:
            self._itens[nome] = {"preco": item["preco"], "quantidade": quantidade}

    def remover_item(self, nome: str, quantidade: int = 1):
        """
        Regra: não é possível remover mais do que a quantidade existente.
        Se chegar a 0, o item é removido do carrinho.
        """
        nome = nome.strip().lower()
        if nome not in self._itens:
            raise KeyError(f"Item '{nome}' não está no carrinho.")
        if quantidade < 1:
            raise ValueError("Quantidade a remover deve ser pelo menos 1.")
        atual = self._itens[nome]["quantidade"]
        if quantidade > atual:
            raise ValueError(
                f"Não é possível remover {quantidade} unidades; há apenas {atual} no carrinho."
            )
        self._itens[nome]["quantidade"] -= quantidade
        if self._itens[nome]["quantidade"] == 0:
            del self._itens[nome]

    def calcular_subtotal(self) -> float:
        """Soma de (preço × quantidade) de todos os itens."""
        return round(
            sum(v["preco"] * v["quantidade"] for v in self._itens.values()), 2
        )

    def aplicar_cupom(self, codigo: str) -> float:
        """
        Regra: cupom deve ser válido (estar em CUPONS).
        Retorna o valor do desconto aplicado sobre o subtotal.
        FRETE0 não gera desconto no subtotal.
        """
        codigo = codigo.strip().upper()
        if codigo not in CUPONS:
            raise ValueError(f"Cupom '{codigo}' inválido ou expirado.")
        desconto = round(self.calcular_subtotal() * CUPONS[codigo], 2)
        return desconto

    def total_com_desconto(self, codigo_cupom: str = None, taxa_entrega: float = 0.0) -> float:
        """
        Regra: total = subtotal - desconto_cupom + taxa_entrega.
        Total nunca pode ser negativo.
        """
        subtotal = self.calcular_subtotal()
        desconto = self.aplicar_cupom(codigo_cupom) if codigo_cupom else 0.0
        total = round(subtotal - desconto + taxa_entrega, 2)
        return max(total, 0.0)

    def listar_itens(self) -> dict:
        return dict(self._itens)

    def esvaziar(self):
        self._itens = {}
