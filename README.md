# image binarization python dio

projeto simples em python para converter uma imagem colorida em escala de cinza e depois em uma imagem binarizada, usando apenas valores 0 e 255.

o projeto foi criado para um desafio da dio e também como material de portfólio no github.

## objetivo

implementar um fluxo básico de processamento de imagens:

1. carregar uma imagem colorida;
2. gerar uma versão em níveis de cinza, com valores de 0 a 255;
3. aplicar uma regra de threshold para transformar a imagem em preto e branco;
4. salvar os resultados em arquivos separados.

## tecnologias usadas

- python
- pillow
- matplotlib

o pillow é usado para carregar, manipular e salvar as imagens. o matplotlib fica disponível como apoio para visualização, caso seja necessário evoluir o projeto depois.

## o que é escala de cinza

uma imagem em escala de cinza representa cada pixel com apenas um valor de intensidade.

esse valor vai de 0 a 255:

- 0 representa preto;
- 255 representa branco;
- valores intermediários representam tons de cinza.

para gerar esse valor a partir de uma imagem colorida, o projeto usa uma combinação dos canais vermelho, verde e azul. essa combinação aproxima a percepção humana de luminosidade:

```text
cinza = 0.299 * vermelho + 0.587 * verde + 0.114 * azul
```

## o que é binarização

binarização é o processo de transformar uma imagem em apenas duas cores: preto e branco.

nesse projeto, cada pixel da imagem em escala de cinza passa por uma regra simples:

- se o valor for maior que 128, o pixel vira 255;
- se o valor for menor ou igual a 128, o pixel vira 0.

isso cria uma imagem com contraste forte, útil para separar regiões claras e escuras.

## estrutura do projeto

```text
image-binarization-python-dio/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── main.py
├── images/
│   ├── input/
│   │   └── .gitkeep
│   └── output/
│       └── .gitkeep
└── examples/
    └── README.md
```

## como executar

antes de rodar o projeto, coloque uma imagem chamada `imagem.jpg` dentro da pasta `images/input`.

depois execute:

```bash
cd image-binarization-python-dio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

## exemplo de entrada e saída

entrada esperada:

```text
images/input/imagem.jpg
```

arquivos gerados:

```text
images/output/grayscale.png
images/output/binary.png
```

a imagem `grayscale.png` contém os tons de cinza de 0 a 255. a imagem `binary.png` contém apenas pixels pretos e brancos, com valores 0 e 255.

## explicação do threshold

o threshold usado no projeto é 128.

ele funciona como um ponto de corte:

- pixels com intensidade acima de 128 são considerados claros e viram branco;
- pixels com intensidade menor ou igual a 128 são considerados escuros e viram preto.

esse valor pode ser alterado no código, mas 128 é um bom ponto inicial porque fica próximo ao meio da escala entre 0 e 255.

## resultados esperados

ao executar o script, o terminal deve mostrar mensagens indicando:

- se a imagem de entrada foi encontrada;
- onde a imagem em cinza foi salva;
- onde a imagem binarizada foi salva;
- se o processamento terminou com sucesso.

se a imagem `images/input/imagem.jpg` não existir, o programa exibe uma mensagem de erro clara e encerra sem quebrar a execução.

## aprendizados do projeto

este projeto ajuda a praticar:

- leitura e gravação de imagens com python;
- manipulação de pixels;
- conversão de rgb para escala de cinza;
- aplicação manual de threshold;
- organização de um projeto simples para github;
- escrita de documentação técnica clara.

## melhorias futuras

algumas melhorias possíveis:

- permitir informar o caminho da imagem por argumento de linha de comando;
- permitir escolher o valor do threshold ao executar o script;
- adicionar visualização com matplotlib;
- criar testes automatizados para validar os pixels gerados;
- comparar diferentes métodos de conversão para escala de cinza.

## comandos git

para versionar e publicar o projeto:

```bash
git init
git add .
git commit -m "feat: add image binarization project"
git branch -M main
git remote add origin https://github.com/fezleep/image-binarization-python-dio.git
git push -u origin main
```

se quiser criar o repositório pelo github cli, use algo como:

```bash
gh repo create fezleep/image-binarization-python-dio --public --source=. --remote=origin
```

não execute o `git push` antes de conferir se o repositório remoto está correto.

## conclusão

o projeto implementa uma base direta e didática de processamento de imagens com python. a lógica principal fica visível no código, sem depender de funções prontas de binarização, o que facilita entender cada etapa do processo.
