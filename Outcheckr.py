import colorama
import sys
import argparse

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

args = parser.parse_args()

checkingurl = args.url

print(checkingurl)

