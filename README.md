# Projeto Final do Módulo de Analytics Engineering da ADA

> Engenharia de Dados e Garantia de Qualidade no Conjunto de Dados do Airbnb no Rio de Janeiro

## Descrição do Projeto

O projeto consiste no tratamento do conjunto de dados da [Inside Airbnb](http://insideairbnb.com/), que apresenta informações sobre listagens de hospedagem, avaliações de hóspedes e disponibilidade de calendário em várias cidades ao redor do mundo. No nosso trabalho, a cidade de estudo foi o Rio de Janeiro.

## Sumário

- [Arquivos](#arquivos)
- [Pré-requisitos](#Prérequisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Teste](#teste)
- [Grupo](#grupo)

## Arquivos

Os arquivos CSV são:

- Listing (Listagem): Este conjunto de dados contém informações detalhadas sobre as propriedades listadas no Airbnb. Cada registro representa uma listagem individual e inclui informações como o tipo de propriedade, preço, localização, número de quartos, comodidades oferecidas e muito mais.

- Reviews (Avaliações): O conjunto de dados de avaliações contém informações sobre as avaliações feitas por hóspedes que ficaram nas propriedades listadas. Ele inclui dados como a data da avaliação, o identificador da propriedade, os comentários escritos pelos hóspedes, e outras informações.

- Calendar (Calendário): Este conjunto de dados contém informações sobre a disponibilidade das propriedades ao longo do tempo. Ele lista as datas em que as propriedades estão disponíveis para reserva, bem como os preços para cada data.

## Pré-requisitos

- Instalar PostgreSQL (versão 16 ou mais atualizada)
- Python3
- Pandas
- dbt

## Instalação

1. Fazer download dos arquivos CSV no [Drive](https://drive.google.com/drive/folders/1VksUbxJR7XVp0sqagbtR8WF8cmbpk5oj)
2. Clonar projeto: `git clone git@github.com:CaioBrainer/Analytics_Engineering_ADA.git`
3. Trocar senha da conexão com BD nos arquivos profiles.yml e script_db.py
4. Acessar a pasta source:

```
cd project/source
```

5. Instalar os packages dbt-core e dbt-postgres

```
pip install dbt-core
pip install dbt-postgres
```

6. Mover os arquivos CSV para a pasta data

## Uso

Para fazer a conexão com o banco:

```
python script_db.py
```

Para dar carga no BD:

```
python script_carga.py
```

Acessar a pasta analytics_engineer:

```
cd ..
cd analytics_engineer
```

Rodar dbt

```
dbt run
```

## Teste

```
dbt test
```

## Grupo

O Grupo 3 é composto por:

- Caio Brainer
- Thaísa Elvas
- Guilherme Oliveira
- Carlos Caldeira
- Thascilla Rosa
- Sormanny Junior
- João Victor
- Natalia Loeblein
