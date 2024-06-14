import cmd

class Outcheckr:

    banner = """
 ██████╗ ██╗   ██╗████████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██████╗ 
██╔═══██╗██║   ██║╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔══██╗
██║   ██║██║   ██║   ██║   ██║     ███████║█████╗  ██║     █████╔╝ ██████╔╝
██║   ██║██║   ██║   ██║   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══██╗
╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║  ██║
 ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                           
"""

    print(banner)
    print("Welcome to Outcheckr, an advanced tool for checking outbound links from a domain")
    print("Please make sure to use the tool for educational or ethical purposes only.The owner is not responsible of any harm done using this tool.")
    print(">>")
    command = input()
    cmd_ = cmd.Cmd()

    cmd_.cmdloop()
