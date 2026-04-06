class Cardapio:
    def __init__(self):
        self._itens = {}

    def adicionar_item(self, nome: str, preco: float, categoria: str) -> dict:
        """
        Regra: nome não pode ser vazio, preço deve ser > 0,
        categoria deve ser: 'lanche', 'bebida' ou 'sobremesa'.
        """
        if not nome or not nome.strip():
            raise ValueError("Nome do item não pode ser vazio.")
        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero.")
        categorias_validas = {"lanche", "bebida", "sobremesa"}
        if categoria not in categorias_validas:
            raise ValueError(f"Categoria inválida. Use: {categorias_validas}")
        nome = nome.strip().lower()
        if nome in self._itens:
            raise ValueError(f"Item '{nome}' já existe no cardápio.")
        self._itens[nome] = {"preco": preco, "categoria": categoria}
        return self._itens[nome]

    def obter_item(self, nome: str) -> dict:
        nome = nome.strip().lower()
        if nome not in self._itens:
            raise KeyError(f"Item '{nome}' não encontrado no cardápio.")
        return self._itens[nome]

    def listar_itens(self) -> dict:
        return dict(self._itens)

    def remover_item(self, nome: str) -> bool:
        nome = nome.strip().lower()
        if nome not in self._itens:
            raise KeyError(f"Item '{nome}' não encontrado no cardápio.")
        del self._itens[nome]
        return True
