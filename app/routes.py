import os
import shutil
from flask import Blueprint, render_template, request, redirect, url_for, current_app, send_file
from werkzeug.utils import secure_filename
from .encryptor.image_processor import process_image
from .encryptor.pdf_processor import process_pdf


main = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def initial():
    return render_template('initial.html')

@main.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
    return redirect(url_for('main.manipulation'))

@main.route('/manipulation')
def manipulation():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    files = os.listdir(upload_folder)
    return render_template('manipulation.html', files=files)

@main.route('/process', methods=['POST'])
def process_manipulation():
    manipulation = request.form.get('manipulation')
    intensity = int(request.form.get('intensity', 0))
    upload_folder = current_app.config['UPLOAD_FOLDER']
    processed_folder = current_app.config['PROCESSED_FOLDER']

    # Clean processed folder first
    if os.path.exists(processed_folder):
        shutil.rmtree(processed_folder)
    os.makedirs(processed_folder, exist_ok=True)

    processed_count = 0

    for filename in os.listdir(upload_folder):
        file_path = os.path.join(upload_folder, filename)
        ext = filename.rsplit('.', 1)[1].lower()

        if ext in ['jpg', 'jpeg', 'png']:
            process_image(file_path, manipulation, intensity, processed_folder)
            processed_count += 1
        '''elif ext == 'pdf':
            process_pdf(file_path, manipulation, intensity, processed_folder)
            processed_count += 1'''

    # After processing, clear upload folder
    shutil.rmtree(upload_folder)
    os.makedirs(upload_folder, exist_ok=True)

    # Store count in session to show on result page
    from flask import session
    session['processed_count'] = processed_count
    return redirect(url_for('main.result', manipulation=manipulation))


@main.route('/result')
def result():
    processed_folder = current_app.config['PROCESSED_FOLDER']
    files = os.listdir(processed_folder)
    manipulation = request.args.get('manipulation', 'Encryption')
    return render_template('result.html', files=files, manipulation=manipulation)

@main.route('/download')
def download_zip():
    processed_folder = current_app.config['PROCESSED_FOLDER']
    zip_path = os.path.join(processed_folder, 'encrypted_files_temp.zip')

    if os.path.exists(zip_path):
        os.remove(zip_path)

    files_to_zip = [f for f in os.listdir(processed_folder) if not f.endswith('.zip')]

    import zipfile
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files_to_zip:
            file_path = os.path.join(processed_folder, file)
            zipf.write(file_path, arcname=file)

    return send_file(zip_path, as_attachment=True, download_name="encrypted_files.zip")
@main.route('/about')
def about():
    return render_template('about.html')

