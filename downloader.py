import os
import subprocess
import logging
from typing import List
import re

def download_images(pages: List[str], dirname: str, magazine_name: str, date: str):
    os.makedirs(dirname, exist_ok=True)

    with open(f'{dirname}.txt', 'w') as f:
        for url in pages:
            f.write(url + '\n')  
    
    # Initial download
    aria2_command = f"aria2c -i {dirname}.txt -d {dirname}"
    subprocess.run(aria2_command, shell=True)
    logging.info('Initial download attempt complete!')

    # Verify if all files were downloaded
    expected_files = [url.split('/')[-1].strip().split('.')[0] for url in pages]
    downloaded_files = [f.split('.')[0] for f in os.listdir(dirname) if not f.endswith('.txt')]

    missing_files = set(expected_files) - set(downloaded_files)

    # Retry downloading missing files up to 3 times
    retries = 3
    while missing_files and retries:
        logging.info(f'Retrying download for missing files: {missing_files}')
        
        with open(f'{dirname}_retry.txt', 'w') as f:
            for missing in missing_files:
                f.write(pages[expected_files.index(missing)] + '\n')

        aria2_command_retry = f"aria2c -i {dirname}_retry.txt -d {dirname}"
        subprocess.run(aria2_command_retry, shell=True)
        logging.info(f"Retry {4 - retries} download attempt complete!")

        # Recheck missing files
        downloaded_files = [f.split('.')[0] for f in os.listdir(dirname) if not f.endswith('.txt')]
        missing_files = set(expected_files) - set(downloaded_files)
        retries -= 1

    if missing_files:
        logging.error(f"Failed to download the following files after retries: {missing_files}")


def reorganize_and_rename_images(dirname, magazine_name, date):
    # Base directory
    base_dir = "Library"
    
    # Magazine specific directory
    magazine_dir = os.path.join(base_dir, magazine_name)
    
    # Date specific directory for the magazine
    date_dir = os.path.join(magazine_dir, date)

    # Create directories if they don't exist
    os.makedirs(date_dir, exist_ok=True)

    # Counter for file naming
    counter = 1

    # Read URLs from txt file
    with open(f"{dirname}.txt", "r") as f:
        urls = [line.strip() for line in f.readlines()]

    for url in urls:
        # Extract the original filename from the URL without the extension
        original_filename = url.split('/')[-1].strip().split('.')[0]
        old_path = os.path.join(dirname, original_filename)
        
        # New filename with .jpg extension
        new_filename = f"{counter:03}.jpg"
        new_path = os.path.join(date_dir, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        counter += 1

    os.remove(f"{dirname}.txt")
    os.rmdir(dirname)
    logging.info(f"Images reorganized and renamed for {magazine_name} - {date}!")
