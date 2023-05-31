import json
from colorama import Fore, Style

def make_account():
    username = input("Enter a new username > ")
    password = input("Enter a new password > ")

    try:
        with open('save.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    if username in data:
        print("Username already exists in the database.")
    else:
        data[username] = {"username": username, "password": password}

        with open('save.json', 'w') as file:
            json.dump(data, file, indent=4)


def sign_in():
    with open('save.json', 'r') as file:
        data = json.load(file)
    username = input("enter username > ")
    password = input("enter password > ")
    account_make = input("need to make a account [yes or no] > ")
    if username and password in data:
        print("logging into your acc")
        main()
    else:
        print("wrong password or username")

    if account_make == "no" or account_make is None:
        pass
    else:
        make_account()

def main():
    menu = f"""{Fore.MAGENTA}
    ██████╗  █████╗ ██████╗  █████╗ ██████╗  ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝
    ██████╔╝███████║██████╔╝███████║██║  ██║██║   ██║ ╚███╔╝ 
    ██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║  ██║██║   ██║ ██╔██╗ 
    ██║     ██║  ██║██║  ██║██║  ██║██████╔╝╚██████╔╝██╔╝ ██╗
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝v1 skids edition
    ---------------------------------------------------------
    
    
    
    [1] - put some here                 [4] put some here
    [2] - put some here                 [5] put some here  
    [3] - put some here                 [6] put some here  
    
    

    """
    print(menu)

sign_in()