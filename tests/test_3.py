from src.exercises_3.fish import fish
from src.exercises_3.wage import wage
from src.exercises_3.ink import ink


def test_fish(capsys):
    fish(40)
    cap = capsys.readouterr()
    assert cap.out.strip() == "Se você pescou 40 kg, isento de multa"

    fish(60)
    cap = capsys.readouterr()
    assert cap.out.strip() == "Excedeu o limite em 10 kg. Multa de 40.0"


def test_wage(capsys):
    valorHora = 10.0
    horasTrabalhadas = 40
    salarioLiquido = 304.0
    wage(valorHora, horasTrabalhadas)
    cap = capsys.readouterr()
    assert (
        cap.out.strip() == f"Seu salário líquido é de {salarioLiquido} reais."
    )

    valorHora = 15.5
    horasTrabalhadas = 35
    salarioLiquido = 412.3
    wage(valorHora, horasTrabalhadas)
    cap = capsys.readouterr()
    assert (
        cap.out.strip() == f"Seu salário líquido é de {salarioLiquido} reais."
    )


def test_ink(capsys):
    area_m = 50
    ink(area_m)
    cap = capsys.readouterr()
    assert cap.out.strip() == "Você usará 1 lata(s) e isso custará 80.0."

    area_m = 2000
    ink(area_m)
    cap = capsys.readouterr()
    assert cap.out.strip() == "Você usará 38 lata(s) e isso custará 3040.0."
