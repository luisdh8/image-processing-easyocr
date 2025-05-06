# License Plate Recognition with EasyOCR

This project performs **license plate detection and text recognition** from images using Python, OpenCV, NumPy, and EasyOCR.  
It includes preprocessing techniques to improve recognition and can run both locally and in Google Colab.

---

## 📁 Project Structure

actividad1/
├── images/
│   ├── placa\_q.jpg
│   └── placa\_4.jpg
├── placas.py
└── README.md


---

## 🚀 Features

- License plate detection using image filtering.
- Text extraction using `EasyOCR` in Spanish and English.
- Compatible with **Google Colab** and **local environments**.
- Draws bounding boxes and displays recognized text with confidence scores.

---

## 🧠 How It Works

1. The image is converted to grayscale.
2. A **black mask** is created to isolate dark regions.
3. Gaussian blur is applied to smooth the mask.
4. A **white mask** highlights bright regions of interest.
5. EasyOCR extracts text from the filtered image.
6. The original image is annotated with recognized text.

---

## 🖼️ Results

## Result 1
![image](https://github.com/user-attachments/assets/c642af48-4479-49b6-bbf0-e46d1d7018b9)

## Result 2
![image](https://github.com/user-attachments/assets/be58b4ee-8bfa-4bcc-9c1e-dad1070ca766)

---

## 💻 Usage

### 🔹 Google Colab

To run in Colab, use:

```python
detectar_texto("./images/placa_q.jpg", colab=True)
detectar_texto("./images/placa_4.jpg", colab=True)
```

### 🔹 Local Execution

To run locally (outside Colab), use:

```python
detectar_texto("./images/placa_q.jpg", colab=False)
```

This will open a window using `cv2.imshow`. Press any key to close it.

---

## 🔧 Requirements

Install the required libraries using pip:

```bash
pip install opencv-python numpy easyocr
```

If you're using Google Colab, also run:

```python
from google.colab.patches import cv2_imshow
```

---

## 📚 Technologies Used

* Python 3
* OpenCV
* NumPy
* EasyOCR
* Google Colab (optional)

---

## 📸 Sample Images

The sample images used are:

* `placa_q.jpg`
* `placa_4.jpg`

They are located inside the `images/` folder.

---

## 📝 Author

Developed by \[Your Name].
For educational and research purposes.

---

```

¿Quieres que agregue una sección de "Posibles mejoras" o "Errores comunes y cómo resolverlos"?
```
