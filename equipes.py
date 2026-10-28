"""Distribui participantes em equipes com tamanhos equilibrados."""
import argparse
import json
import random
import unicodedata
from pathlib import Path


def distribuir(nomes, quantidade, semente=None):
    if not isinstance(nomes, list) or not nomes:
        raise ValueError('Informe uma lista não vazia de participantes.')
    if type(quantidade) is not int or not 1 <= quantidade <= len(nomes):
        raise ValueError('Quantidade de equipes deve estar entre 1 e o total de participantes.')
    limpos = []
    vistos = set()
    for nome in nomes:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError('Cada participante deve ter um nome não vazio.')
        nome = unicodedata.normalize('NFC', ' '.join(nome.split()))
        chave = nome.casefold()
        if chave in vistos:
            raise ValueError(f'Participante repetido: {nome}. Use identificadores distintos para homônimos.')
        vistos.add(chave)
        limpos.append(nome)
    random.Random(semente).shuffle(limpos)
    return [limpos[i::quantidade] for i in range(quantidade)]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('arquivo', type=Path, help='JSON com lista de nomes')
    p.add_argument('--equipes', type=int, required=True)
    p.add_argument('--semente', type=int, help='Reproduz o resultado com a mesma lista e ambiente Python')
    a = p.parse_args()
    try:
        nomes = json.loads(a.arquivo.read_text(encoding='utf-8-sig'))
        equipes = distribuir(nomes, a.equipes, a.semente)
    except (ValueError, OSError) as e:
        p.error(str(e))
    print(json.dumps({'equipes': equipes}, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
