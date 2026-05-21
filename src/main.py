from pathlib import Path

from PIL import Image


THRESHOLD = 128

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_IMAGE = BASE_DIR / "images" / "input" / "imagem.jpg"
OUTPUT_DIR = BASE_DIR / "images" / "output"
GRAYSCALE_IMAGE = OUTPUT_DIR / "grayscale.png"
BINARY_IMAGE = OUTPUT_DIR / "binary.png"


def rgb_to_grayscale(red: int, green: int, blue: int) -> int:
    """Converte um pixel RGB para um valor de cinza entre 0 e 255."""
    return int(0.299 * red + 0.587 * green + 0.114 * blue)


def create_grayscale_image(image: Image.Image) -> Image.Image:
    """Gera uma imagem em escala de cinza calculando cada pixel manualmente."""
    rgb_image = image.convert("RGB")
    grayscale_image = Image.new("L", rgb_image.size)

    width, height = rgb_image.size

    for y in range(height):
        for x in range(width):
            red, green, blue = rgb_image.getpixel((x, y))
            gray_value = rgb_to_grayscale(red, green, blue)
            grayscale_image.putpixel((x, y), gray_value)

    return grayscale_image


def create_binary_image(grayscale_image: Image.Image, threshold: int = THRESHOLD) -> Image.Image:
    """Aplica threshold manual: acima do limite vira 255, caso contrario vira 0."""
    binary_image = Image.new("L", grayscale_image.size)

    width, height = grayscale_image.size

    for y in range(height):
        for x in range(width):
            pixel_value = grayscale_image.getpixel((x, y))
            binary_value = 255 if pixel_value > threshold else 0
            binary_image.putpixel((x, y), binary_value)

    return binary_image


def main() -> None:
    print("iniciando processamento da imagem")

    if not INPUT_IMAGE.exists():
        print(f"erro: imagem de entrada nao encontrada em {INPUT_IMAGE}")
        print("adicione uma imagem chamada imagem.jpg dentro de images/input e tente novamente")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"carregando imagem: {INPUT_IMAGE}")

    with Image.open(INPUT_IMAGE) as image:
        grayscale_image = create_grayscale_image(image)
        binary_image = create_binary_image(grayscale_image)

    grayscale_image.save(GRAYSCALE_IMAGE)
    binary_image.save(BINARY_IMAGE)

    print(f"imagem em escala de cinza salva em: {GRAYSCALE_IMAGE}")
    print(f"imagem binarizada salva em: {BINARY_IMAGE}")
    print("processamento finalizado com sucesso")


if __name__ == "__main__":
    main()
