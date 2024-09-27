# Casos de Dengue no Estado de São Paulo em 2022
  Projeto de dashboard em **Power BI** para representar os dados epidemiológicos de Dengue da plataforma do [CVE - Centro de Vigilância Epidemiológica "Prof. Alexandre Vranjac"](https://www.saude.sp.gov.br/cve-centro-de-vigilancia-epidemiologica-prof.-alexandre-vranjac/areas-de-vigilancia/doencas-de-transmissao-por-vetores-e-zoonoses/agravos/) de maneira mais dinâmica e acrescentar insights. <br>
  <br>
  Assim com pensar na pensando na vistualização dos diferentes níveis hierárquicos do setor de epidemiologia:
- Gestor do Estado
- Subgestor das GVEs
- Subgestor das Regiões de Saúde
- Subgestor dos Município.
 <br>
 <br>
 
  ![Texto Alternativo](https://github.com/Edgard-Lopes/dengue/blob/main/Dashboard%20-%20Dados%20epidemiol%C3%B3gicos.jpg)

## Origem
  A ideia do projeto surgiu com a aplicação do Itinerário **"Zoonoses Tropicais"** que apliquei enquanto era professor do Ensino Público do Estado de São Paulo. Durante a disciplina, me deparei com a dificuldade de encontrar informações epidemiológicas, visualizar as informações e tranformar os dados disponíveis em dados trabalháveis para o nível exigido pelos alunos do Ensino Médio.

## Refinamento
Necessitei criar um programa em Python para realizar a transformação da planilha original do CVE em algo trabalhável pelo Power BI, ajustando informações e removendo cabeçalhos. <br>
+ Disponível na pasta :file_folder: [Conversor de tabelas](https://github.com/Edgard-Lopes/Casos-de-Dengue-no-Estado-de-Sao-Paulo-em-2022/tree/main/Conversor%20de%20tabelas), no documento :page_facing_up: [arquivo Automatizador planilha dengue.py](https://github.com/Edgard-Lopes/Casos-de-Dengue-no-Estado-de-Sao-Paulo-em-2022/blob/main/Conversor%20de%20tabelas/Automatizador%20planilha%20dengue.py)

## Insights
  Uma das informações interessantes foi ver que alguns municipios apresentaram uma menor proporção de casos confirmado de Dengue em relação a Casos Notificados. Isso leva a perguntas como: Por que? Podemos pensar em compreender a adesão da população aos exames, se há informação da população, se há autocuidado da população, buscar encontrar outras variáveis que podem se correlacionar com os dados e explicar o padrão observado e a partir disso pensar em ações para mudar o quadro.

## Ferramentas
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

> [!NOTE]   
> Note: I've excluded "casos inforrmado importados", 'cause it represented no significant information for the analisis. <br>
> Nota: Excluí as informções de "casos confirmados importados" pois apresentavam pouca relevância na análise.
