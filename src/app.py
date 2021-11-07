from os import path
import json
from conjur import Client
from conjur.api import api

def get_api_key_from_file(path) -> str:
    with open(path) as file:
        for line in file:
            if line.startswith('API key for admin: '):
                return line[19:].rstrip()

def print_menu():
    print("---------Main Menu---------")
    print("(1) Policy")
    print("(2) Replace policy file")
    print("(q) exit")
    print(">>", end="")
    return input()

def do_policy(client: Client):
    exit_do_policy = False
    while exit_do_policy == False:
        print("----------Policy-----------")
        print("(1) Load policy")
        print("(2) Replace policy")
        print("(3) Replace policy (delete/revoke/deny)")
        print("(4) Back to main menu")
        print(">>", end="")
        p_choose = input()
        if p_choose in ["1", "2", "3"]:
            print("Enter policy file>>", end="")
            policy_file = input()
            if path.exists(policy_file):
                print(1)
            else:
                print(f"File {policy_file} not found")
                exit_do_policy = True
        elif p_choose == "4":
            exit_do_policy = True
        else:
            print(f"Invalid command {p_choose}")
            exit_do_policy = True


def do_list(client: Client):
    print(json.dumps(client.list(), indent=4))


dispatch = {
    '1': do_policy,
    '2': do_list,
}

def process_command(command: str, client:Client):
    if command in dispatch:
        dispatch[command](client)
        return False
    else:
        if command.lower() == 'q':
            return True
        else:
            print(f"command {command} is not found")
            return False

def main():
    conjur_server_url = "http://localhost:8080"
    api_key = get_api_key_from_file("myorg_data")   
    client = Client(url=conjur_server_url,
        account="myorg",
        login_id="admin",
        password=api_key)

    #map(lambda x: True if x % 2 == 0 else False, range(1, 11))

    stop = False
    while stop == False:
        choice = print_menu()
        stop = process_command(choice, client)


if __name__ == '__main__':
    main()
