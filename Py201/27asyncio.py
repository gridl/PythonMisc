import asyncio

# asyncio removes around event loop which waits for something to happen and then acts on the event
# responsible for handling such things as I/O and system events
#Once event handlers are done , they need to give control back to event loop, to do this asyncio uses coroutines
# coroutine special function and is a consumer and extension of a generator

# coroutine example

import asyncio
import os
import urllib.request

async def download_coroutine(url):
    """ A coroutine to download the specified URL"""
    request = urllib.request.urlopen(url)
    filename = os.path.basename(url)

    with open(filename, 'wb') as file_handle:
        while True:
            chunk = request.read(1024)
            if not chunk:
                break

            file_handle.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg

async def main(urls):
    """ Creates a group of coroutines and waits for them to finish"""
    # queues up the list of URLs
    coroutines = [download_coroutine(url) for url in urls]
    # wait function to wait for the coroutines to finish
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())

if __name__ == '__main__':
    urls = ['http://www.irs.gov/pub/irs-pdf/f1040.pdf']

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))
    finally:
        event_loop.close()




