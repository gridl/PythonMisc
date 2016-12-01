# Download the landing page of sites and print out the size

from concurrent.futures import ThreadPoolExecutor as Executor

urls = """google twitter facebook """.split()


def fetch(url):
    from urllib import request, error
    try:
        data = request.urlopen(url).read()
        return '{}: length {}'.format(url, len(data))
    except error.HTTPError as e:
        return '{}:{}'.format(url, e)

# create threadpool executor instance to specify how many workers are required
with Executor(max_workers=4) as exe:
    template = 'http://www.{}.com'
    # jobs are created one for every URL
    # executor manages delivery of jobs to the four threads
    jobs = [exe.submit(fetch, template.format(u)) for u in urls]
    results = [job.result() for job in jobs]
print('\n'.join(results))
# Even though one job is created for every URL, we limit the number of active threads to 4

""""
if you want to use processes in stead of threads change to

from concurrent.futures import ProcessPoolExecutor as Executor

In CPU bound tasks, better to use processs based pool
Primary problem while using processes for parallelism is that each process is confined to its own memory space which makes it difficult for multuiple workers to chew on the same large chunk of data. Ther are way to get around this but in such situations threads proovide a much simpler model


"""