import os
import argparse
import logging
from scrapers import get_vogue_pages, get_ad_pages, get_vf_pages, get_esquire_pages
from downloader import download_images, reorganize_and_rename_images
import shutil

def main(url: str):
    # Set up main Library and subdirectories
    base_dir = "Library"
    os.makedirs(base_dir, exist_ok=True)
    for sub_dir in ["Vogue", "Esquire", "VF", "AD"]:
        os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)

    magazine_name = None  # Placeholder for magazine name
    if "vogue" in url:
        pages = get_vogue_pages(url)
        magazine_name = "Vogue"
    elif "architecturaldigest" in url:
        pages = get_ad_pages(url)
        magazine_name = "AD"
    elif "vanityfair" in url:
        pages = get_vf_pages(url)
        magazine_name = "VF"
    elif "esquire" in url:
        pages = get_esquire_pages(url)
        magazine_name = "Esquire"
    else:
        logging.error("Website not recognized")
        exit()

    date = url.split('/')[-2]
    temp_dir = os.path.join("Library", magazine_name, f"{date}_temp")
    
    # Download images to the temp directory
    download_images(pages, temp_dir, magazine_name, date)
    
    # Reorganize and rename images
    reorganize_and_rename_images(temp_dir, magazine_name, date)

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Argument parser
    parser = argparse.ArgumentParser(description="Download magazine issues from Conde Nast's archives.")
    parser.add_argument('url', type=str, help='URL of the magazine issue.')
    args = parser.parse_args()

    main(args.url)
