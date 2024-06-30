import colorama
import sys
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

colorama.init()

is_windows=sys.platform.startswith('win')

Green = colorama.Fore.GREEN
Magenta = colorama.Fore.MAGENTA
Red = colorama.Fore.RED
Reset = colorama.Fore.RESET
white = colorama.Fore.WHITE

if is_windows:
    import win_unicode_console

    win_unicode_console.enable()

prompt = '>>'

banner = f"""{Green}
 ██████╗ ██╗   ██╗████████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██████╗ 
██╔═══██╗██║   ██║╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔══██╗
██║   ██║██║   ██║   ██║   ██║     ███████║█████╗  ██║     █████╔╝ ██████╔╝
██║   ██║██║   ██║   ██║   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══██╗
╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║  ██║
 ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                           
{Reset}"""

print(banner)
print("Welcome to Outcheckr, an advanced tool for checking outbound links from a domain\n")
print("#Coded by Ashfaq Sadat\n\n")

parser = argparse.ArgumentParser("Argparser")

parser.add_argument('-u', '--url', help = "url to check for", required=True)
parser.add_argument('-n', '--no-color', help = "output without colors", nargs='?',required=False, default=False)
parser.add_argument('-v', '--verbose', help = "Display results real-time", required=False, action="store_true")
parser.add_argument('-o', '--output', help = "file to save the results", required=False)

args = parser.parse_args()

if args.verbose:
    print(f"{white}[-]{Green}verbosity is on. Output will be displayed{Reset}\n")

checkingurl = args.url

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
        
ols= get_outbound_links(checkingurl)

def file_write(filename):
    if ".txt" in filename:
        pass
    else:
        filename = filename + ".txt"
    file = open(filename, "w")
    for link in ols:
        file.write(link+"\n")

if args.output:
    file_write(args.output)
    print(f"{Green}successfully written in file!{Reset}\n\n")

if args.verbose:
    for link in ols:
        print(link+"\n")





