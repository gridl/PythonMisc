import queue
import threading
import requests

# called by each thread
def get_url(q,url):
    q.put(requests.get(url).text)

theurls = ["http://google.com", "https://yahoo.com"]

q = queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args=(q,u))
    t.daemon = True
    t.start()

s = q.get()
print(s)

""" Case where theading is used as a simple optimization. Each subthread is waiting for a URL to resolve an d respond in order to put its contents on the queue. Each thread is a daemon. The main thread
starts all subthreads, does a get on the queue to wait until one of them has done a put, then emits the results and terminates. Cpython doesnt use multiple cores to run CPU bound tasks, the only reason for thread is to
not blocking the process while there is a wait for I/O"""