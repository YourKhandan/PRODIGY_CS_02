import os
import zipfile

def create_zip(processed_folder):
    zip_path = os.path.join(processed_folder, 'encrypted_files.zip')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for f in os.listdir(processed_folder):
            if f != 'encrypted_files.zip':
                zipf.write(os.path.join(processed_folder, f), arcname=f)
