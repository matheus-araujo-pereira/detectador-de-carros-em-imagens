import os
import json
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from matplotlib.widgets import RectangleSelector

coordenadas_selecionadas = []


def ao_selecionar_retangulo(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    coordenadas_selecionadas.append((x1, y1))
    coordenadas_selecionadas.append((x1, y2))
    coordenadas_selecionadas.append((x2, y1))
    coordenadas_selecionadas.append((x2, y2))


def main():
    caminho_imagem = "imagens/image_0010.jpg"  # Ajuste conforme necessário
    imagem = io.imread(caminho_imagem)

    fig, ax = plt.subplots()
    ax.imshow(imagem)

    seletor_retangulo = RectangleSelector(
        ax,
        ao_selecionar_retangulo,
        interactive=True,
        useblit=True,
        button=[1],
        minspanx=5,
        minspany=5,
        spancoords="pixels",
    )

    plt.connect(
        "key_press_event", lambda e: plt.close(fig) if e.key in ["Q", "q"] else None
    )
    plt.show()

    if not os.path.exists("coordenadas"):
        os.makedirs("coordenadas")

    # Extrai apenas o nome do arquivo
    nome_arquivo = os.path.basename(caminho_imagem)

    # Para salvar em TXT
    nome_txt = nome_arquivo.replace(".jpg", ".txt")
    caminho_txt = os.path.join("coordenadas", nome_txt)
    with open(caminho_txt, "w") as arquivo_txt:
        for x, y in coordenadas_selecionadas:
            arquivo_txt.write(f"{x},{y}\n")

    # Para salvar em JSON
    nome_json = nome_arquivo.replace(".jpg", ".json")
    caminho_json = os.path.join("coordenadas", nome_json)
    with open(caminho_json, "w") as arquivo_json:
        json.dump(coordenadas_selecionadas, arquivo_json, indent=2)


if __name__ == "__main__":
    main()
