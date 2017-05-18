import subprocess

completed = subprocess.run(['ls','-l'], stdout = subprocess.PIPE,)

print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))

#output error
# run a series of commands in a subshell, send messages to standard output and standard error before commands exit with an error code

try:
    completed = subprocess.run('echo to stdout; echo to stderr 1>&2; exit 1', check=True,shell=True,stdout=subprocess.PIPE,)

except subprocess.CalledProcessError as err:
    print('Error:', err)
else:
    print('returncode:', completed.returncode)
    print('have {} bytes in stdout: {!r}'.format(len(completed.stdout), completed.stdout.decode('utf-8')))

