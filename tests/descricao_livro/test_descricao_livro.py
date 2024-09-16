from src.livro.livro import Livro


def test_descricao_livro(capsys):
    livro = Livro("Sul da fronteira, oeste do sol", "Haruki Murakami", 224)
    assert livro.titulo == "Sul da fronteira, oeste do sol"
    assert livro.autor == "Haruki Murakami"
    assert livro.paginas == 224

    print(livro)

    out, _ = capsys.readouterr()

    assert (
        out.strip()
        == "O livro Sul da fronteira, oeste do sol de Haruki Murakami possui 224 páginas."
    )
