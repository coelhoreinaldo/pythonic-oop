class Produto:
    _Produto__nome: str
    _Produto__codigo: str
    _Produto__preco: float
    _Produto__quantidade: int

    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        self._Produto__nome = nome
        self._Produto__codigo = codigo
        self._Produto__preco = preco
        self._Produto__quantidade = quantidade

    def get_preco(self) -> float:
        return self._Produto__preco

    def get_quantidade(self) -> int:
        return self._Produto__quantidade

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("Preço não pode ser negativo")

        self._Produto__preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        self._Produto__quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        if quantidade > self._Produto__quantidade:
            raise ValueError(
                "Quantidade a ser removida é maior que a quantidade em estoque"
            )

        self._Produto__quantidade -= quantidade
