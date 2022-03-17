import os, random, time,subprocess, string
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()

class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    blueaccounts = f"{WHITE}[ {BLUE}ACCOUNTS {WHITE}]"
    redaccounts = f"{WHITE}[ {RED}ACCOUNTS {WHITE}]"
    blueone = f"{WHITE}[ {BLUE}1 {WHITE}]"
    bluetwo = f"{WHITE}[ {BLUE}2 {WHITE}]"
    xrblue = f"\n{blueplus} Follow Grabber {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
accounts = []
class FILES():
    def __init__(self):
        self.select_file(f"\n{DESIGN.blueaccounts} Enter To Select File: ")
        self.open_file(accounts, DESIGN.blueaccounts, DESIGN.redaccounts)
    def select_file(self, text):
        print(text, end="")
        input()
        root = Tk()
        root.title(".txt")
        self.path = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=(("txt document","*.txt"),("All Files", "*.*")))
        root.destroy()
        root.mainloop()
    def open_file(self, my_list, bluefile, redfile):
        filename = self.path.split("/")[-1]
        if self.path[-4:]!=".txt":
            print(f"\n{redfile} Please Select (.txt) File ", end="")
            input()
            exit()
        try:
            for x in open(self.path, "r").read().split("\n"):
                if x!="":
                    my_list.append(x)
            print(f"\n{bluefile} Successfully Load {DESIGN.BLUE}{filename}")
            time.sleep(2)
        except Exception as err:
            print(f"\n{redfile} {err} ", end="")
            input()
            exit()
class FILES2():
    def __init__(self):
        self.open_file("accounts", accounts)
    def open_file(self, filename, my_list):
        try:
            for x in open(f"{filename}.txt", "r").read().split("\n"):
                if x!="" and ":" in x:
                    my_list.append(x)
            print(f"\n{DESIGN.blueplus} Successfully Load {DESIGN.BLUE}{filename}.txt")
            time.sleep(2)
        except:
            print(f"\n{DESIGN.redminus} {DESIGN.RED}{filename}.txt {DESIGN.WHITE}is missing ", end="")
            input()
            exit()
class Xnce():
    def __init__(self):
        self.done, self.error, self.turn, self.run = 0, 0, 0, True
        print(f"\n{DESIGN.blueplus} Target: ", end="")
        self.target = input()
        self.id()
    def inex(self, text):
        print(f"\n{DESIGN.redminus} {DESIGN.WHITE}run = {DESIGN.RED}False {DESIGN.WHITE}, {text}")
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        exit()
    def remove_session(self, sessionid):
        accounts.remove(sessionid)
        if len(accounts) < 1:
            self.inex("No Accounts")
    def id(self):
        self.my_id = False
        while not self.my_id:
            try:
                sessionid = accounts[self.turn]
            except:
                self.inex("No Accounts")
            head = {
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                "cookie": f"sessionid={sessionid}"
            }
            req = requests.get(f"https://www.instagram.com/{self.target}/?__a=1", headers=head)
            #print(req.text, req.status_code)
            if "graphql" in req.text and req.status_code==200:
                try:
                    self.user_id = req.json()["graphql"]["user"]["id"]
                    self.my_id = True
                except Exception as err:
                    print(f"\n{DESIGN.redminus} {err}")
                    self.inex("Error")
            elif "no-js not-logged-in" in req.text:
                self.turn += 1
            else:
                print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
                self.inex("Error")
    def followers_ing(self):
        print(f"\n{DESIGN.blueone} Followers {DESIGN.bluetwo} Following: ", end="")
        mode = input()
        if mode == "1":
            self.follow = "followers"
        elif mode == "2":
            self.follow = "following"
        else:
            exit()
        print(f"\n{DESIGN.blueplus} Enter To Start: ", end="")
        input()
        self.follow_url = f"https://i.instagram.com/api/v1/friendships/{self.user_id}/{self.follow}/?count=10000&search_surface=follow_list_page"
        while self.run:
            for sessionid in accounts:
                head = {
                    "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)",
                    "cookie": f"sessionid={sessionid}",
                    }
                req = requests.get(self.follow_url, headers=head)
                #print(req.text, req.status_code)
                if "users" in req.text:
                    usernames = req.json()
                    for user in usernames["users"]:
                        self.done += 1
                        with open(f"{self.target}-{self.follow}.txt", "a") as file:
                                file.write(f'\n{user["username"]}')
                                file.close()
                        self.counter()
                    try:
                        self.max_id = usernames["next_max_id"]
                        self.follow_url = f"https://i.instagram.com/api/v1/friendships/{self.user_id}/{self.follow}/?count=10000&max_id={self.max_id}&search_surface=follow_list_page"
                    except:
                        self.inex("Finshed")
                elif "challenge_required" in req.text and req.status_code==400:
                    self.remove_session(sessionid)
                elif "unable to fetch" in req.text and req.status_code==400:
                    self.inex("Target is Private Account")
                elif '"users":[]' in req.text:
                    self.inex("Finshed")
                elif req.status_code == 403:
                    self.remove_session(sessionid)
                elif req.status_code==429:
                    self.error += 1
                else:
                    print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
                self.counter()
    def counter(self):
        os.system(f"title Done : {self.done} / Error: {self.error}")
try:
    from tkinter import *
    from tkinter import filedialog
    FILES()
except:
    FILES2()
clear()
print(DESIGN.xrblue)
x = Xnce()
try:
    x.followers_ing()
except:
    pass
