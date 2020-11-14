from threading import Thread
import seldiscord
import itertools

workers = 10
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
output_file = open("tokens.txt", "a")

with open("proxies.txt", encoding="UTF-8", errors="ignore") as f:
    proxy_iter = itertools.cycle(f.read().splitlines())

def save_token(token):
    print(token)
    output_file.write("%s\n" % token)
    output_file.flush()

class Worker(Thread):
    def do_task(self):
        proxy_url = "http://%s" % next(proxy_iter)
        with seldiscord.Session(user_agent, proxy_url) as dsc:
            dsc.setup()
            dsc.register(
                username="h0nda")
            dsc.gateway()
            save_token(dsc.token)
        
    def run(self):
        while 1:
            try:
                self.do_task()
            except Exception as err:
                print("Worker error:", err, type(err))

for _ in range(workers):
    Worker().start()
