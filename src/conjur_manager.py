from conjur import Client

class ConjurManager:

    def __init__(self, username, api_key, url) -> None:
        self.username = username
        self.api_key = api_key
        self.url = url
        self.client = Client(account=self.username, api_key=self.api_key, url=self.url)
        
    def print_menu():
        print("--------------------------------")
        print("1. list")
        choose = input()
        return choose


    def get(self):
        print("input the id:")
        myid = input()
        
        

        