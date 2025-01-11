# Intalação do tesseract
# https://stackoverflow.com/questions/46140485/tesseract-installation-in-windows

# Por padrao o tesseract ele vem com o tessdata em ingles ou seja se voce usar uma imageme brasileira que tenha acento e "ç" ele nao vai colocar toda a acentuação
# Para corrigir isso tem que entrar no link do github (https://github.com/tesseract-ocr/tessdata) e baixar o arquivo da linguagem correspondente
# https://github.com/tesseract-ocr/tessdata

import pytesseract;
import cv2;

nomePrint = "teste.png"

# Lendo a imagem
imagem = cv2.imread(nomePrint)

caminho = r"C:\Program Files\Tesseract-OCR"
# Fazendo o pytesseract extrair os dados da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

# O segundo parametro "lang=""por" define a linguagem para portugues 
# Antes de colocar esse parametro deve ser feito o passo no começo do arquivo que e baixar o arquivo e coloca na pasta r"\tessdata" 
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)