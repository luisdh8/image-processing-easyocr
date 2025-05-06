"""
Este script fue ejecutado en Google Colab, por lo que ha cambiado un poco la forma de mostrar las imágenes.
Por tanto, para ejecutar de manera local, se debe cambiar la función cv2_imshow por cv2.imshow y agregar cv2.waitKey(0) y cv2.destroyAllWindows al final de la función detectar_texto.
"""

import cv2
import numpy as np
import easyocr
from google.colab.patches import cv2_imshow

def filtrar_imagen(ruta_imagen):
    img = cv2.imread(ruta_imagen)
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Filtro negro
    negro = np.zeros(img_gris.shape, dtype=np.uint8)
    for y in range(img_gris.shape[0]):
        for x in range(img_gris.shape[1]):
            if img_gris[y, x] < 50:
                negro[y, x] = 255

    # Desenfoque gaussiano
    desenfoque = cv2.GaussianBlur(negro, (21, 21), sigmaX=9)

    # Filtro blanco
    blanco = np.zeros(desenfoque.shape, dtype=np.uint8)
    for y in range(desenfoque.shape[0]):
        for x in range(desenfoque.shape[1]):
            if desenfoque[y, x] > 120:
                blanco[y, x] = 255

    return blanco

def detectar_texto(ruta_imagen):
    imagen_filtrada = filtrar_imagen(ruta_imagen)
    lector = easyocr.Reader(['es', 'en'])
    resultados = lector.readtext(imagen_filtrada)

    imagen_original = cv2.imread(ruta_imagen)

    print(f"\nResultados para {ruta_imagen}:")
    for (caja, texto, confianza) in resultados:
        (tl, tr, br, bl) = caja
        tl = tuple(map(int, tl))
        br = tuple(map(int, br))

        cv2.rectangle(imagen_original, tl, br, (0, 255, 0), 2)
        cv2.putText(imagen_original, texto, tl, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print(f"Detectado: '{texto}' (confianza: {confianza:.2f})")

    cv2_imshow(imagen_original)

if __name__ == "__main__":
    detectar_texto("./images/placa_q.jpg")
    detectar_texto("./images/placa_4.jpg")