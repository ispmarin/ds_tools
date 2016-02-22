```
Ivan Marin
Vivo Data Labs
ivan.smarin@telefonica.com
2016-02-18
```
# Gerador de Hashes
O script Python gera hashes usando o algoritmo [SHA-256](https://en.wikipedia.org/wiki/SHA-2)
e faz a codificação destes hashes em [Base64](https://en.wikipedia.org/wiki/Base64).

## Algoritmo
O script executa as seguintes operações:

```
para linha em arquivo:
    hash = SHA-256(linha)
    hash_base = base64(hash)
```

## Execução
O script requer Python versão 2.7. Para executar, em um terminal utilize o comando

```
python generate_hash.py -i test.csv -o out.csv
```
os quais `test.csv` é o arquivo de entrada com o nome do tipo de dado e os dados a serem gerados hashes e `out.csv` é
o arquivo de saída com os valores originais de entrada e uma coluna adicional, chamada de `hash`.

O executável do Python deve estar no caminho do terminal.