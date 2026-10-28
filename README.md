# Equipes Equilibradas

Programa para dividir participantes de uma oficina ou grupo de estudo em equipes com tamanhos que diferem no máximo em uma pessoa. Exemplo: sete participantes em três equipes resultam em grupos de 3, 2 e 2 pessoas. Funciona apenas no terminal.

## Executar
Python 3.10+, sem dependências externas:

```sh
python equipes.py exemplo.json --equipes 3
python equipes.py exemplo.json --equipes 3 --semente 42
python -m unittest -v
```

A entrada é uma lista JSON de nomes. A saída JSON contém as equipes. Nenhum arquivo é alterado. Nomes repetidos, desconsiderando maiúsculas, espaços extras e normalização Unicode NFC, são rejeitados; diferencie homônimos com identificadores. A lista original não é modificada.

## Limites
Demonstração de portfólio com participantes fictícios. Equilibra apenas quantidade, não habilidades, disponibilidade ou preferências. Não tem interface gráfica, contas ou histórico. Usa o gerador pseudoaleatório padrão do Python: não serve para sorteios com prêmios, seleção de candidatos ou decisões que exijam auditoria. A semente permite repetir o resultado com a mesma ordem de entrada e o mesmo ambiente; não promete resultados idênticos entre versões diferentes do Python.
