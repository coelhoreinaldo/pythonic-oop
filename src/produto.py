class Produto:
    _nome: str
    _codigo: str
    _preco: float
    _quantidade: int

    def __init__(
        self, nome: str, codigo: str, preco: float, quantidade: int
    ) -> None:
        self._nome = nome
        self._codigo = codigo
        self._preco = preco
        self._quantidade = quantidade

    def get_preco(self) -> float:
        pass

    def get_quantidade(self) -> int:
        pass

    def atualizar_preco_do_produto(self, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("Preço não pode ser negativo")

        self._preco = novo_preco

    def adicionar_estoque_do_produto(self, quantidade: int) -> None:
        self._quantidade += quantidade

    def remover_estoque_do_produto(self, quantidade: int) -> None:
        if quantidade > self._quantidade:
            raise ValueError(
                "Quantidade a ser removida é maior que a quantidade em estoque"
            )

        self._quantidade -= quantidade
