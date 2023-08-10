# Condé Cracker
## Unlock Condé Nast's vault with the premier ripper for Vogue, Esquire, Vanity Fair, and Architectural Digest.

### Overview
Condé Cracker is a powerful tool for accessing a vast collection of iconic journalism from Condé Nast's prestigious archives. The app is built in Python and uses advanced web-scraping technology to seamlessly downloads full issues from publications including Vogue, Esquire, Vanity Fair, and Architectural Digest spanning over a century. 

After fetching the content, Condé Cracker efficiently processes and organizes the high-quality scans into coherent directories, systematically renaming images and archiving full-length issues. If you enjoy Esquire's in-depth articles, Vogue's trend-setting fashion pieces, Architectural Digest's stunning home designs, or Vanity Fair's insightful cultural critiques, CondeCracker offers you effortless access to these historical archives on the grandest of scales.

## Features
- **Automated Downloading:** Given a list of image URLs, the application downloads all images efficiently.
- **Organized File Management:** Images are saved in a structured directory based on the magazine name and publication date.
- **Sequential Renaming:** Images are renamed in a sequential manner to maintain order, ensuring covers and other important pages are properly placed.
- **Error Handling:** The application handles potential download errors, ensuring all images are accounted for and retrieved if any issues arise.

## Installation and Setup
- Ensure you have Python installed on your machine.
- Clone the repository: `‌git clone github.com/saldigioia/conde-cracker`
- Navigate to the repository: `c‌d conde-cracker`
- Install the necessary libraries: `pip install -r requirements.txt`

## How to Use
1. Navigate to one of the following archives to choose an issue:
- **Esquire:** https://classic.esquire.com/
- **Vogue:** https://archive.vogue.com/
- **Vanity Fair:** https://archive.vanityfair.com
- **Architectural Digest:** https://archive.architecturaldigest.com/
2. Once you've picked an issue, alter its URL by appending "/print" to bypass any subscription barriers. This is essential for the application's functionality.
3. Run the application: `‌python3 main.py [URL]`
4. As the application whirs, it curates a temporary .TXT file housing each page's URL. This file is safely tucked away in a temporary directory. Following this, the application embarks on a mission, sifting through this directory to refurbish and retitle each page.
5. After the makeover, you'll find your fresh, high-resolution magazine issues neatly stacked in the Library directory.

Enjoy unfettered access to a world of classic journalism with CondeCracker!
