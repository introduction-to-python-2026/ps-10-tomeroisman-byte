from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    %%writefile image_utils.py
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=float)

def edge_detection(image):
    def edge_detection(image, threshold=50):
    img_array = np.array(image.convert('L'))
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    h, w = img_array.shape
    edge_data = np.zeros_like(img_array, dtype=float)
    padded = np.pad(img_array, 1, mode='edge')
    for i in range(h):
        for j in range(w):
            region = padded[i:i+3, j:j+3]
            gx = np.sum(region * kx)
            gy = np.sum(region * ky)
            edge_data[i, j] = np.sqrt(gx**2 + gy**2)
    white = np.where(edge_data > threshold, 255, 0).astype(np.uint8)
    return image, Image.fromarray(white)
