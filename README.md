# 🎨 Pixel Manipulator

A web-based image manipulation tool that allows users to upload image or PDF files, apply a variety of transformations, and download the results—right from your browser.

🌐 **Live Website**: [https://pixel-manipulator.onrender.com](https://pixel-manipulator.onrender.com)


## 🔧 Features

- 🎞 Upload image files (`.jpg`, `.jpeg`, `.png`) — PDF support limited to local use
- ⚙️ Choose from a range of manipulations:
  - **Grayscale** (with brightness control)
  - **Invert Colors**
  - **Blur**
  - **Brightness Adjustment** (darken/lighten)
  - **Contrast Adjustment**
  - **XOR Filter**
- 📦 Download all manipulated files in a single `.zip`
- ✨ Live intensity slider with numeric and hover value preview
- 💡 Visual feedback: processing indicators, hover descriptions for manipulations


---

## 🚀 Deployment Notes

> 🛡️ The app is built with certain system-level libraries like **OpenCV** and **pdf2image**, which require:
>
> - **Admin privileges** to run locally
> - **Poppler** installed (for PDF manipulation)(but i havent embedded this into the web app)
> - **Render.com** hosting (PDF features may be partially disabled)


## 🛠️ Tech Stack

- **Frontend**: HTML5, Bootstrap5, JS
- **Backend**: Python, Flask
- **Libraries**: OpenCV, Pillow, FPDF, pdf2image
- **Deployment**: Render with Docker

## 💡 Running Locally

1. Clone the repository  
   git clone https://github.com/YourKhandan/PRODIGY_CS_02.git
   cd PRODIGY_CS_02
2. Install dependencies
  pip install -r requirements.txt
3. Run the ap
  python run.py
4. Visit: http://localhost:5000
## 📌Notes
PDF manipulations (e.g., grayscale, brightness, etc.) are fully supported in local runs with Poppler installed.

Render deployments may restrict PDF handling due to lack of system-level tools.

Manipulation range: -100 to +100 — visible via slider with live hover feedback.
## Acknowledgement
Thank you for visiting my repository
