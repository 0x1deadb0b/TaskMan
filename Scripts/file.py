import os
import zipfile
import tarfile
import urllib.request
import shutil

def download(url: str, output_path: str, working_dir: str = ".") -> bool:
    full_path = os.path.join(working_dir, output_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    print(f"[INFO] Downloading {url}")
    try:
        urllib.request.urlretrieve(url, full_path)
        return True
    except Exception as e:
        print(f"[ERROR] Download failed: {e}")
        return False

def extract(archive_path: str, dest_dir: str, working_dir: str = ".") -> bool:
    full_archive = os.path.join(working_dir, archive_path)
    full_dest = os.path.join(working_dir, dest_dir)

    if not os.path.exists(full_archive):
        print(f"[ERROR] Archive does not exist: {archive_path}")
        return False

    os.makedirs(full_dest, exist_ok=True)
    print(f"[INFO] Extracting {archive_path} -> {dest_dir}")

    try:
        if full_archive.endswith('.zip'):
            with zipfile.ZipFile(full_archive, 'r') as zip_ref:
                zip_ref.extractall(full_dest)
        elif full_archive.endswith(('.tar.gz', '.tgz', '.tar.xz', '.tar.bz2')):
            with tarfile.open(full_archive, 'r:*') as tar_ref:
                tar_ref.extractall(full_dest)
        else:
            print(f"[WARNING] Unknown archive format for {archive_path}. Moving file directly to {dest_dir}.")
            file_name = os.path.basename(full_archive)
            os.rename(full_archive, os.path.join(full_dest, file_name))
            
        return True
    except Exception as e:
        print(f"[ERROR] Extraction failed: {e}")
        return False

def delete_folder(folder_path:str, working_dir:str) -> bool:
    full_path = os.path.join(working_dir, folder_path)
    if os.path.exists(full_path):
        print(f"[INFO] Deleting {full_path}")
        shutil.rmtree(full_path)
        print(f"[INFO] {full_path} deleted successfully.")
    else:
        print(f"[INFO] {full_path} directory not found.")
    return True
