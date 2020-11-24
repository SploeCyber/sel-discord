from threading import Thread
import seldiscord
import secrets
import itertools

workers = 10
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
output_file = open("tokens.txt", "a")

with open("proxies.txt", encoding="UTF-8", errors="ignore") as f:
    proxy_iter = itertools.cycle(f.read().splitlines())

def save_token(token):
    print(token)
    output_file.write("%s\n" % token)
    output_file.flush()

def generate_name():
    return secrets.token_hex(4)

class Worker(Thread):
    def do_task(self):
        proxy_url = "http://%s" % next(proxy_iter)
        with seldiscord.Session(user_agent, proxy_url) as dsc:
            dsc.register(username=generate_name())
            dsc.gateway()
            save_token(dsc.token)
        
    def run(self):
        while 1:
            try:
                self.do_task()
            except Exception:
                pass

for _ in range(workers):
    Worker().start()
