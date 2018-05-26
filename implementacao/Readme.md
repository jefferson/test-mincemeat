# Paradigmas de Computação distribuída e bancos de dados

Responda quais são as duas palavras que mais acontecem para os seguintes autores:

- Grzegorz Rozenberg
- Philip S. Y

Inicialmente criamos um programa para verificar quantos artigos existem para cada autor, chegando ao seguinte resultado:

- Grzegorz Rozenberg, 28
- Philip S. Yu, 36

O código que executou a contagem acima pode ser verificado em: quantos_artigos_para_cada_autor.py

Posteriomente verificamos as palavras que mais ocorrem para cada autor, no títulos dos seus respectivos artigos, obtendo os seguintes resultados:

- Para o autor Grzegorz Rozenberg foram encontradas duas palavras com a mesma quantidade de ocorrência que são: "Systems" e "Grammars" com o total de 9 incidências.
- Para o autor Philip S. Yu a palavra com o maior número de incidências foi "Data" com 7 ocorrências.

Para realizar a pesquisa acima foram realizados os seguintes filtros durante a etapa de mapeamento:

- Remoção das stopwords
- Remoção dos caracteres "." e ",".

O código que executou a contagem acima pode ser verificado em: amostragem_de_palavras.py

o resultado completo da contagem das palavras pode ser verificado no arquivo Ocorrencias.csv