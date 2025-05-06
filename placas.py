"""
Este script fue ejecutado en Google Colab, por lo que ha cambiado un poco la forma de mostrar las imágenes.
Para ejecutarlo de forma local, cambia 'cv2_imshow' por 'cv2.imshow' y agrega 'cv2.waitKey(0)' y 'cv2.destroyAllWindows()'.
"""

import cv2
import numpy as np
import easyocr
from google.colab.patches import cv2_imshow


def filtrar_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Filtro negro
    mascara_negra = np.zeros(imagen_gris.shape, dtype=np.uint8)
    for y in range(imagen_gris.shape[0]):
        for x in range(imagen_gris.shape[1]):
            if imagen_gris[y, x] < 50:
                mascara_negra[y, x] = 255

    # Desenfoque gaussiano
    desenfoque = cv2.GaussianBlur(mascara_negra, (21, 21), sigmaX=9)

    # Filtro blanco
    mascara_blanca = np.zeros(desenfoque.shape, dtype=np.uint8)
    for y in range(desenfoque.shape[0]):
        for x in range(desenfoque.shape[1]):
            if desenfoque[y, x] > 120:
                mascara_blanca[y, x] = 255

    return mascara_blanca


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
        cv2.putText(imagen_original, texto, tl,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print(f"Detectado: '{texto}' (confianza: {confianza:.2f})")

    cv2_imshow(imagen_original)


if __name__ == "__main__":
    detectar_texto("./images/placa_q.jpg")
    detectar_texto("./images/placa_4.jpg")