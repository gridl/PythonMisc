import asyncio
import functools

# use a coroutine to launch a process to run the unix command df to find the free space on local disks
# use subprocess() to launch the process and tie it to a protocol class that knows how to read the df command output and parse it
# methods of the protocol class are called automatically based on i/o events for the subprocess

async def run_df(loop):
    print('in run_df')

    cmd_done = asyncio.Future(loop=loop)
    factory = functools.partial(DFProtocol, cmd_done)
    proc = loop.subprocess_exec(
        factory, 'df', '-hl',
        stdin=None,stderr=None
    )
    try:
        print('launching process')
        transport, protocol = await proc
        print('waiting for process to complete')
        await cmd_done
    finally:
        transport.close()

    return cmd_done.result()

class DFProtocol(asyncio.SubprocessProtocol): # derived from subprocess protocol which defines the API for a class to communicate with another process through pipes
    FD_NAMES = ['stdin','stdout','stderr']

    def __init__(self,done_future):
        self.done = done_future
        self.buffer = bytearray()
        super().__init__()


    def connection_made(self, transport): # invoked when the input channels to the new process are set up
        print('process started {}'.format(transport.get_pid()))
        self.transport = transport


    def pipe_data_received(self, fd, data):# invoked with the file descriptor where the data was emitted and the actual data read from the pipe
        # protocol class saves the output from the standard output channel of the process in a buffer for later processing
        print('read {} bytes from {}'.format(len(data),self.FD_NAMES[fd]))

        if fd == 1:
            self.buffer.extend(data)


    def process_exited(self): # when the process terminates, process_exited() is called
        print('process exited')
        return_code = self.transport.get_returncode() # exit code of the process is available from the trnasport object by calling get_returncode()
        print('return code {}'.format(return_code))
        if not return_code:
            cmd_output = bytes(self.buffer).decode()
            results = self._parse_results(cmd_output)
        else:
            results = []
        self.done.set_result((return_code, results))


    def _parse_results(self,output):
        print('parsing results')
        # Output has one row of headers, all single words. THe remaining rows are one per filesystem, with columns matching the headers (assuming that none of the mountpoints ahve whitespace in the names
        if not output:
            return []
        lines = output.splitlines()
        headers = lines[0].split()
        devices = lines [1:]
        results = [
            dict(zip(headers,line.split()))
            for line in devices
        ]
        return results

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(run_df(event_loop))
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('\nFree space')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))