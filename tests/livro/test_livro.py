from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("Sul da fronteira, oeste do sol", "Haruki Murakami", 224)
    assert livro.titulo == "Sul da fronteira, oeste do sol"
    assert livro.autor == "Haruki Murakami"
    assert livro.paginas == 224


def test_livro_repr():
    livro = Livro("Crônica do pássaro de corda", "Haruki Murakami", 608)
    assert (
        repr(livro)
        == "O livro Crônica do pássaro de corda de Haruki Murakami possui 608 páginas."
    )
