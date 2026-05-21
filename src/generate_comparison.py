import os
import tempfile
from pathlib import Path

# Define um cache temporario para o matplotlib.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "matplotlib"))

import matplotlib
from PIL import Image

# Usa um backend sem janela para salvar a imagem comparativa.
matplotlib.use("Agg")

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent.parent
ORIGINAL_IMAGE = BASE_DIR / "images" / "input" / "imagem.jpg"
GRAYSCALE_IMAGE = BASE_DIR / "images" / "output" / "grayscale.png"
BINARY_IMAGE = BASE_DIR / "images" / "output" / "binary.png"
RESULT_IMAGE = BASE_DIR / "images" / "result_example.png"


def load_image(path):
    # Carrega a imagem a partir do caminho informado.
    return Image.open(path)


def main():
    # Define as imagens e os titulos que serao exibidos.
    images = [
        ("original", load_image(ORIGINAL_IMAGE)),
        ("grayscale", load_image(GRAYSCALE_IMAGE)),
        ("binary", load_image(BINARY_IMAGE)),
    ]

    # Cria uma figura com tres imagens lado a lado.
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=150)
    fig.patch.set_facecolor("white")

    for axis, (title, image) in zip(axes, images):
        axis.imshow(image, cmap="gray" if image.mode == "L" else None)
        axis.set_title(title, fontsize=9, pad=8)
        axis.axis("off")

    # Ajusta os espacamentos para manter um layout limpo.
    plt.tight_layout(pad=1.5)
    fig.savefig(RESULT_IMAGE, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    print(f"Imagem comparativa salva em: {RESULT_IMAGE}")


if __name__ == "__main__":
    main()
