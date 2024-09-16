from typing import Dict


class Estoque:
    produtos: Dict[str, int]

    def __init__(self, produtos: Dict[str, int]) -> None:
        self.produtos = produtos

    def adicionar_produto_no_estoque(self, nome: str, quantidade: int) -> None:
        if nome in self.produtos:
            self.produtos[nome] += quantidade
            return

        self.produtos[nome] = quantidade

    def remover_produto_do_estoque(self, nome: str, quantidade: int) -> None:
        if quantidade > self.produtos[nome]:
            raise ValueError(
                "Quantidade a ser removida maior que a quantidade em estoque."
            )

        self.produtos[nome] -= quantidade

    def atualizar_produto_no_estoque(
        self,
        nome: str,
        nova_quantidade: int,
    ) -> None:
        if nome not in self.produtos:
            raise ValueError("Produto não encontrado no estoque.")

        self.produtos[nome] = nova_quantidade

    def visualizar_estoque(self) -> None:
        for produto in self.produtos:
            print(f"{produto}: {self.produtos[produto]}")
