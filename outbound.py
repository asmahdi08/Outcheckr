import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class outbound:
    def get_outbound_links(domain):
        try:
            response = requests.get(domain)

        except requests.RequestException:
            print(f"Error fetching {domain}: {e}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        tags = soup.find_all(href=True)

        o_links = []

        for link in tags :
            url = link['href']

            full_url = urljoin(domain, url)

            domain_name = urlparse(domain).netloc
            url_name = urlparse(full_url).netloc

            if url_name and url_name != domain_name :
                o_links.append(full_url)
        
        if o_links :
            return o_links
        else:
            return None

