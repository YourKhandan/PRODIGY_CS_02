import os
import cv2
import numpy as np
import tempfile
from pdf2image import convert_from_path
from fpdf import FPDF

def process_pdf(file_path, manipulation, intensity, processed_folder):
    with tempfile.TemporaryDirectory() as temp_dir:
        pages = convert_from_path(file_path, output_folder=temp_dir)
        processed_images = []

        for i, page in enumerate(pages):
            img = np.array(page)

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

            processed_images.append(img)

        # Save processed images into new PDF
        output_pdf_path = os.path.join(
            processed_folder,
            f"{os.path.splitext(os.path.basename(file_path))[0]}_encrypted_{manipulation}.pdf"
        )
        save_images_to_pdf(processed_images, output_pdf_path)

def save_images_to_pdf(images, output_pdf_path):
    pdf = FPDF(unit='pt', format=[images[0].shape[1], images[0].shape[0]])
    for img in images:
        temp_img_path = output_pdf_path + ".jpg"
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        cv2.imwrite(temp_img_path, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        pdf.add_page()
        pdf.image(temp_img_path, 0, 0)
        os.remove(temp_img_path)
    pdf.output(output_pdf_path)

def pixel_shuffle(image, intensity):
    h, w = image.shape[:2]
    for _ in range(intensity * 10):
        x1, y1 = np.random.randint(0, w), np.random.randint(0, h)
        x2, y2 = np.random.randint(0, w), np.random.randint(0, h)
        image[y1, x1], image[y2, x2] = image[y2, x2], image[y1, x1]
    return image
