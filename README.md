
# Extração de Texto com Tesseract OCR em Python

Este projeto utiliza o Tesseract OCR com a biblioteca `pytesseract` para extrair texto de uma imagem, com suporte à língua portuguesa (acentuação, "ç", etc).

## 🧠 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://github.com/madmaze/pytesseract)

---

## 🛠️ Requisitos

- Python 3 instalado
- Tesseract OCR instalado
- Biblioteca OpenCV (`cv2`)
- Biblioteca `pytesseract`

### Instalação do Tesseract no Windows

1. Baixe o instalador:  
   👉 https://github.com/UB-Mannheim/tesseract/wiki

2. Instale e anote o caminho de instalação (ex: `C:\Program Files\Tesseract-OCR`)

3. Baixe o arquivo de linguagem portuguesa (por.traineddata) em:  
   👉 https://github.com/tesseract-ocr/tessdata

4. Coloque esse arquivo na pasta `tessdata` do Tesseract, geralmente em:  
   `C:\Program Files\Tesseract-OCR\tessdata`

---

## 📦 Instalação das dependências Python

```bash
pip install pytesseract opencv-python
```

---

## 🧪 Como usar

1. Coloque sua imagem (ex: `teste.png`) no mesmo diretório do script.
2. Altere a variável `nomePrint` com o nome da sua imagem, se necessário.
3. Execute o script Python:

```python
import pytesseract
import cv2

nomePrint = "teste.png"

# Lendo a imagem
imagem = cv2.imread(nomePrint)

# Caminho para o executável do Tesseract
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

# Extração do texto com linguagem em português
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)
```

---

## 📷 Exemplo de saída

Para uma imagem com o texto:

```
Olá, mundo! Isso é um teste com acentuação: á, é, í, ó, ú, ç.
```

A saída será:

```
Olá, mundo! Isso é um teste com acentuação: á, é, í, ó, ú, ç.
```

---

## ❗ Observações

- Certifique-se de que o caminho do Tesseract esteja correto.
- Para melhores resultados, utilize imagens nítidas e com boa iluminação.
- Pode-se aplicar pré-processamento na imagem (como escala de cinza, binarização, etc) para melhorar a leitura, se necessário.

---

## 📄 Licença

Este projeto está sob a licença MIT.
