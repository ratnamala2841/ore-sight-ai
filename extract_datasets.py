"""
Auto-extractor for Google Drive zip downloads in Ore-Sight AI.
Looks for any .zip files in the project or datasets folder and unpacks them cleanly.
"""

import os
import zipfile
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

def extract_all_zips():
    DATA_DIR = os.path.join(BASE_DIR, "data")
    search_dirs = [DATASETS_DIR, DATA_DIR, BASE_DIR]
    zip_files = []
    
    for d in search_dirs:
        if os.path.exists(d):
            zip_files.extend(glob.glob(os.path.join(d, "*.zip")))
        
    if not zip_files:
        print("[!] No .zip files found in:")
        print(f"    - {DATASETS_DIR}")
        print(f"    - {DATA_DIR}")
        print(f"    - {BASE_DIR}")
        return
        
    for zf in zip_files:
        print(f"[*] Found zip archive: {os.path.basename(zf)}")
        print(f"    Extracting to {DATASETS_DIR}...")
        try:
            with zipfile.ZipFile(zf, 'r') as zip_ref:
                zip_ref.extractall(DATASETS_DIR)
            print(f"    [SUCCESS] Extracted all files from {os.path.basename(zf)}")
        except Exception as e:
            print(f"    [ERROR] Failed to extract {zf}: {e}")
            
    print("\n[DONE] All datasets extracted and ready!")

if __name__ == "__main__":
    extract_all_zips()
