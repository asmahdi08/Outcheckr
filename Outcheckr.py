import colorama
import sys
import argparse
import outbound

colorama.init()

is_windows=sys.platform.startswith('win')

Green = colorama.Fore.GREEN
Magenta = colorama.Fore.MAGENTA
Red = colorama.Fore.RED
Reset = colorama.Fore.RESET

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
parser.add_argument('-n', '--no-color', help = "output without colors", nargs='?',required=False)
parser.add_argument('-v', '--verbose', help = "Display results real-time",nargs='?', required=False)
parser.add_argument('-o', '--output', help = "file to save the results", required=False)

args = parser.parse_args()

checkingurl = args.url

ols= outbound.outbound.get_outbound_links(checkingurl)

for link in ols:
    print(link)
