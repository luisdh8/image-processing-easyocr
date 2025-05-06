"""
Este script fue ejecutado en Google Colab, por lo que ha cambiado un poco la forma de mostrar las imágenes.
Para ejecutarlo de forma local, cambia 'cv2_imshow' por 'cv2.imshow' y agrega 'cv2.waitKey(0)' y 'cv2.destroyAllWindows()'.
"""

import cv2
import numpy as np
import easyocr
from google.colab.patches import cv2_imshow


def crear_mascara_negra(imagen_gris):
    return np.where(imagen_gris < 50, 255, 0).astype(np.uint8)


def crear_mascara_blanca(imagen_desenfocada):
    return np.where(imagen_desenfocada > 120, 255, 0).astype(np.uint8)


def filtrar_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    mascara_negra = crear_mascara_negra(imagen_gris)
    desenfoque = cv2.GaussianBlur(mascara_negra, (21, 21), sigmaX=9)
    mascara_blanca = crear_mascara_blanca(desenfoque)

    return mascara_blanca


def mostrar_resultados(resultados):
    for (_, texto, confianza) in resultados:
        print(f"Detectado: '{texto}' (confianza: {confianza:.2f})")


def dibujar_resultados(imagen, resultados):
    for (caja, texto, _) in resultados:
        (tl, tr, br, bl) = caja
        tl = tuple(map(int, tl))
        br = tuple(map(int, br))
        cv2.rectangle(imagen, tl, br, (0, 255, 0), 2)
        cv2.putText(imagen, texto, tl,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    return imagen


def detectar_texto(ruta_imagen, colab=True):
    imagen_filtrada = filtrar_imagen(ruta_imagen)
    lector = easyocr.Reader(['es', 'en'])
    resultados = lector.readtext(imagen_filtrada)

    imagen_original = cv2.imread(ruta_imagen)

    print(f"\nResultados para {ruta_imagen}:")
    mostrar_resultados(resultados)

    imagen_con_resultados = dibujar_resultados(imagen_original, resultados)

    if colab:
        cv2_imshow(imagen_con_resultados)
    else:
        cv2.imshow("Resultado", imagen_con_resultados)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Para Google Colab
    detectar_texto("./images/placa_q.jpg", colab=True)
    detectar_texto("./images/placa_4.jpg", colab=True)

    # Para ejecución local, descomenta esta línea:
    # detectar_texto("./images/placa_q.jpg", colab=False)