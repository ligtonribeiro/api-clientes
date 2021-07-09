import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    return nome.replace(" ", "").isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    """Verifica se o celular é válido (11 91234-1234) """
    regex_celular = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    match_celular = re.findall(regex_celular, celular)
    return match_celular
