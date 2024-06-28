import colorama
import sys

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
print("Welcome to Outcheckr, an advanced tool for checking outbound links from a domain")
print("#Coded by Ashfaq Sadat")


