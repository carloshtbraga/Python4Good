def minha_funcao(c):
    print(f"Olá, {c}!")


def test_minha_funcao(capsys):
    minha_funcao("oi")
    capturador = capsys.readouterr()
    assert capturador.out.strip() == "Olá, oi!"
    minha_funcao("tchau")
    capturador = capsys.readouterr()
    assert capturador.out.strip() == "Olá, tchau!"


# Se quiser usar parametros
# import pytest


# def minha_funcao(valor):
#     print("O valor é:", valor)


# @pytest.mark.parametrize("valor", [5, 10])
# def test_minha_funcao(capsys, valor):
#     minha_funcao(valor)
#     capturador = capsys.readouterr()
#     assert capturador.out.strip() == f"O valor é: {valor}"
