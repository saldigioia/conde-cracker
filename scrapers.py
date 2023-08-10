import requests
from bs4 import BeautifulSoup
import logging
from typing import List

# Functions to get page links

def get_vogue_pages(url: str) -> List[str]:
    date = url.split("/")[-2]
    source_url = 'https://archive.vogue.com//image/nCU7lza0PM150sIHOTteljBKCHAc7Y9a/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('script', type='text/javascript')
    pages = data[2].text
    result = pages.split('"PageName":"')
    page_links = []
    
    for x in result[1:]:
        clean = x.split('Key')
        final = clean[0].split('"')
        final_src = source_url + date + '/' + final[0]
        page_links.append(final_src)
    
    return page_links


def get_ad_pages(url: str) -> List[str]:
    date = url.split("/")[-2]
    source_url = 'https://architecturaldigest.azurewebsites.net/image/nCU7lza0PM150sIHOTteljBKCHAc7Y9a/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        return []

    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all('script', type='text/javascript')
    pages = data[1].text
    result = pages.split('"PageName":"')
    page_links = []
    
    for x in result[1:]:
        clean = x.split('"')
        final = clean[0]
        final_src = source_url + date + '/' + final
        page_links.append(final_src)

    return page_links


def get_vf_pages(url: str) -> List[str]:
    date = url.split("/")[-2]
    source_url = 'https://archive.vanityfair.com/image/nCU7lza0PM150sIHOTteljBKCHAc7Y9a/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        return []

    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all('script', type='text/javascript')
    pages = data[2].text
    result = pages.split('"PageName":"')
    page_links = []
    
    for x in result[1:]:
        clean = x.split('"')
        final = clean[0]
        final_src = source_url + date + '/' + final
        page_links.append(final_src)

    return page_links


def get_esquire_pages(url: str) -> List[str]:
    date = url.split("/")[-2]
    source_url = 'https://classic.esquire.com/image/nCU7lza0PM150sIHOTteljBKCHAc7Y9a/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        return []

    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all('script', type='text/javascript')
    pages = data[1].text
    result = pages.split('"PageName":"')
    page_links = []
    
    for x in result[1:]:
        clean = x.split('"')
        final = clean[0]
        final_src = source_url + date + '/' + final
        page_links.append(final_src)

    return page_links
