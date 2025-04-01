# Detector de Carros

Este projeto implementa um pipeline para detecção de carros em imagens utilizando técnicas de processamento de imagens e operações morfológicas. Ele é composto por scripts em Python e um Jupyter Notebook que detalha as etapas do processamento.

## Estrutura do Projeto

- **`salvar_coordenadas.py`**: Script para selecionar manualmente regiões de interesse em imagens e salvar as coordenadas em arquivos JSON e TXT.
- **`detector.ipynb`**: Notebook que implementa o pipeline completo de processamento de imagens, incluindo equalização, operações morfológicas e detecção de carros.

## Bibliotecas Utilizadas

As principais bibliotecas utilizadas no projeto são:

- `numpy`: Manipulação de arrays e cálculos numéricos.
- `matplotlib`: Visualização de imagens e gráficos.
- `scikit-image`: Processamento de imagens.
- `json`: Manipulação de arquivos JSON.
- `os`: Operações de sistema de arquivos.

## Como Executar

### 1. Selecionar Coordenadas com `salvar_coordenadas.py`

Este script permite selecionar manualmente regiões de interesse em uma imagem e salvar as coordenadas.

#### Passos:

1. Certifique-se de que a imagem está no diretório `imagens/`.
2. Execute o script:
   ```bash
   python salvar_coordenadas.py
   ```
3. Use o mouse para selecionar regiões retangulares na imagem exibida.
4. Pressione `Q` ou `q` para fechar a janela.
5. As coordenadas serão salvas no diretório `coordenadas/` em arquivos `.json` e `.txt`.

### 2. Executar o Pipeline no Jupyter Notebook

O notebook `detector.ipynb` implementa o pipeline completo de detecção de carros.

#### Etapas Implementadas:

1. **Carregamento e Equalização de Imagem**:

   - A imagem é carregada e convertida para escala de cinza.
   - Um histograma é gerado e a equalização é realizada manualmente.

2. **Processamento Morfológico**:

   - Operações como abertura e fechamento são aplicadas para remover ruídos e destacar regiões de interesse.

3. **Detecção de Regiões**:

   - Regiões conectadas são identificadas e analisadas para encontrar possíveis carros.

4. **Cálculo de IoU**:

   - A métrica Intersection over Union (IoU) é usada para comparar as regiões detectadas com as coordenadas reais.

5. **Marcação de Regiões**:
   - As regiões detectadas são marcadas na imagem original com retângulos.

#### Passos:

1. Abra o notebook no Jupyter:
   ```bash
   jupyter notebook detector.ipynb
   ```
2. Siga as células do notebook para executar o pipeline.
3. Visualize os resultados intermediários e finais, incluindo as imagens processadas e as regiões detectadas.

## Funções Principais

### `salvar_coordenadas.py`

- **`ao_selecionar_retangulo`**: Callback para capturar as coordenadas do retângulo selecionado.
- **`main`**: Função principal que exibe a imagem, permite a seleção de regiões e salva as coordenadas.

### `detector.ipynb`

- **`carregar_exibir_e_equalizar_imagem`**: Carrega a imagem, converte para escala de cinza e realiza a equalização.
- **`abertura_imagem` e `fechamento_imagem`**: Aplicam operações morfológicas para remover ruídos e destacar estruturas.
- **`detectar_e_marcar_carros`**: Detecta regiões retangulares e marca as áreas correspondentes na imagem original.
- **`calcular_iou`**: Calcula a métrica IoU para avaliar a precisão da detecção.

## Resultados

O pipeline detecta regiões que correspondem a carros em imagens, marcando-as com retângulos. Ele também compara as detecções com coordenadas reais para avaliar a precisão.

## Contribuição

Sinta-se à vontade para contribuir com melhorias no código ou na documentação. Abra uma issue ou envie um pull request!
