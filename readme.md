# Detalhes

Carrega o arquivo `.osm`, le as coordenadas gps dos pontos "way", referenciando o "node" via "nd", buscando valores com tag "highway", e gera posicoes GPS para preencher locais onde teoricamente seriam posicoes de Postes.

## Postes

Ainda nao esta 100%, pois os pontos estao "clusterizados" nas intersessoes. A intensao eh que estes pontos fiquem espalhados paralelamente a via, a certas distancia da via, a certa distancia entre um ponto e outro.

## TODO:

Fazer que os pontos sejam distribuidos a cada 30M um do outro, paralelo a via, a 10M da via, sendo esta distancia variando de acordo com o tipo da via (primaria, secundaria, tercearia, ...).