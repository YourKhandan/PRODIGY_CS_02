import cv2
import numpy as np
import os

def process_image(file_path, manipulation, intensity, processed_folder):
    img = cv2.imread(file_path)

    if manipulation == 'pixel_shuffle':
        img = pixel_shuffle(img, intensity)
    elif manipulation == 'grayscale':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.clip(img.astype(int) + intensity, 0, 255).astype(np.uint8)
    elif manipulation == 'brightness':
        img = cv2.convertScaleAbs(img, alpha=1, beta=intensity)
    elif manipulation == 'contrast':
        factor = (259 * (intensity + 255)) / (255 * (259 - intensity)) if intensity != 0 else 1
        img = cv2.convertScaleAbs(img, alpha=factor, beta=0)
    elif manipulation == 'invert':
        img = cv2.bitwise_not(img)
    elif manipulation == 'xor':
        img = cv2.bitwise_xor(img, np.full_like(img, 127))
    elif manipulation == 'blur':
        ksize = max(1, int(abs(intensity) / 5) * 2 + 1)
        img = cv2.GaussianBlur(img, (ksize, ksize), 0)

    filename = os.path.basename(file_path)
    new_filename = f"{os.path.splitext(filename)[0]}_encrypted_{manipulation}.png"
    save_path = os.path.join(processed_folder, new_filename)

    cv2.imwrite(save_path, img)
    return new_filename

def pixel_shuffle(image, intensity):
    h, w = image.shape[:2]
    for _ in range(intensity * 10):
        x1, y1 = np.random.randint(0, w), np.random.randint(0, h)
        x2, y2 = np.random.randint(0, w), np.random.randint(0, h)
        image[y1, x1], image[y2, x2] = image[y2, x2], image[y1, x1]
    return image
