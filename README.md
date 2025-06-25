# PRODIGY_CS_02
🎯 PIXL Manipulator
A full-fledged image & PDF manipulation web tool
Built with ❤️ using Flask + OpenCV + PDF2Image + Docker

🌟 Features
✅ Upload multiple images and PDFs

✅ Manipulate images with:

Grayscale (with adjustable brightness)

Brightness Adjustment (both increase & decrease)

Invert Colors

Contrast Adjustment

Pixel Shuffle (color shuffling for cool effects)

XOR Encryption-like pixel modification

✅ Full PDF support with all manipulation effects applied

✅ Clean UI with live slider + progress handling

✅ Download all processed files in a single ZIP

⚙️ Deployment Details
This app is designed to run inside a Dockerized container.

Note: This app requires some libraries which are not easily available on serverless cloud platforms (like opencv, pdf2image, poppler). Hence, it uses Docker for portability and stability.

That’s also why it can't be directly deployed on platforms like Render without Docker support.
🔑 Security Notes
This app runs file operations and image processing.

Do NOT expose publicly without proper security if handling real user data.

All file uploads are temporary and processed locally.

💡 Tech Stack
Flask (Python)

OpenCV

PDF2Image

FPDF2

Docker
