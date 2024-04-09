import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import arxiv
import os


URL = 'https://arxiv.org/list/cs.AI/recent'

def fetch_recent_paper_ids(url, max_query=3):
    """Fetches recent paper IDs from arXiv."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', title='Abstract')

        # Limiting the number of queries to the actual number of IDs found, if necessary
        num_links = len(links)
        if max_query > num_links:
            print(f"Requested number of papers exceeds available. Fetching {num_links} papers instead.")
            max_query = num_links

        arxiv_ids = [link.text[6:] for link in links[:max_query]]

        return arxiv_ids
    except requests.HTTPError as e:
        print(f'Failed to retrieve content: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
    return []

def download_papers(paper_ids, download_path='./PDF'):

    os.makedirs(download_path, exist_ok=True)
    """Downloads papers given a list of arXiv IDs."""
    client = arxiv.Client()
    search = arxiv.Search(id_list=paper_ids)

    for result in tqdm(client.results(search), total=len(paper_ids), desc="Downloading"):
        result.download_pdf(dirpath=download_path)

if __name__ == "__main__":
    paper_ids = fetch_recent_paper_ids(URL)
    if paper_ids:
        download_papers(paper_ids)
        print("Papers downloaded!")
    else:
        print("No papers fetched.")
