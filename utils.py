"""Funções utilitárias personalizadas e com validações defensivas."""

from __future__ import annotations

from typing import Any


def meu_somar_itens(valores: list[float | int]) -> float:
    """Soma uma lista de números de forma segura.

    Corrige bugs comuns:
    - lista vazia retorna 0.0
    - ignora valores booleanos (True/False)
    - falha com mensagem clara para valores não numéricos
    """
    total = 0.0
    for valor in valores:
        if isinstance(valor, bool):
            continue
        if not isinstance(valor, (int, float)):
            raise TypeError(f"Valor inválido para soma: {valor!r}")
        total += float(valor)
    return total


def meu_dividir(a: float | int, b: float | int) -> float:
    """Divide dois números com validação de divisão por zero."""
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return float(a) / float(b)


def meu_normalizar_nome(nome: str) -> str:
    """Normaliza nomes removendo espaços extras e padronizando capitalização."""
    if not isinstance(nome, str):
        raise TypeError("Nome deve ser uma string.")

    partes = [p for p in nome.strip().split(" ") if p]
    return " ".join(parte.capitalize() for parte in partes)


def meu_buscar_chave(dados: dict[str, Any], chave: str, padrao: Any = None) -> Any:
    """Busca uma chave em um dicionário com fallback seguro."""
    if not isinstance(dados, dict):
        raise TypeError("Dados deve ser um dicionário.")
    if not isinstance(chave, str) or not chave:
        raise ValueError("Chave deve ser uma string não vazia.")
    return dados.get(chave, padrao)
