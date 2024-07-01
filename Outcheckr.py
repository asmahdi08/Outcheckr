import colorama
import sys
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os
import re

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

def banner():

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
parser.add_argument('-n', '--no-color', help = "output without colors",required=False, action="store_true")
parser.add_argument('-v', '--verbose', help = "Display results real-time", required=False, action="store_true")
parser.add_argument('-o', '--output', help = "file to save the results", required=True)

args = parser.parse_args()

if args.no_color:
    Green=""
    Magenta = ""
    Red = ""
    Reset = ""
    white = ""

banner()

if args.no_color:
    print(f"{white}[-]{Green}no-color is on. colors are not displayed{Reset}\n")

if args.verbose:
    print(f"{white}[-]{Green}verbosity is on. Output will be displayed{Reset}\n")

checkingurl = args.url

def get_outbound_links(domain):
        try:
            response = requests.get(domain)
            response.raise_for_status()

        except requests.RequestException as e:
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
        
def sanitize(text):
    sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', text)
    return sanitized

def parse_input_file(filen):
    with open(f"./input/{filen}", "r") as file:
        urls = [line.strip() for line in file]

    return urls

def file_write(filename, intype):
    if ".txt" in filename:
        pass
    else:
        filename = filename + ".txt"
    if intype == "single":
        ols = get_outbound_links(args.url)
        file = open(f"./output/{filename}", "w")
        for link in ols:
            file.write(link+"\n")
    elif intype == "multiple":
        inputlinks = parse_input_file(filen=args.url)
        outall = open(f"./output/{filename}", "w")
        for inlink in inputlinks:
            ll = get_outbound_links(inlink)
            for files in inputlinks:
                os.makedirs(f"./output/(folder){filename}", exist_ok=True)
                foldername = sanitize(files)
                out = open(f"./output/(folder){filename}/{foldername}.txt", "w")
                for link in ll:
                    out.write(link+"\n")
                    outall.write(link+"\n")

if args.output:
    if ".txt" in args.url:
        file_write(filename=args.output,intype="multiple")
    else:
        file_write(filename=args.output,intype="single")

if args.verbose:
    fn = args.output
    if ".txt" in fn :
        pass
    else:
        fn = fn+".txt"
    outfile = open(f"./output/{fn}", "r")
    outs = outfile.readlines()
    for link in outs:
        print(link+"\n")