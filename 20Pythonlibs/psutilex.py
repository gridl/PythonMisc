import psutil
import os, sys, time

# CPU load sampled over time
# Produces one value for each logical CPU
cpu = psutil.cpu_percent(interval=5, percpu=True)
print(cpu)
# os module provides pid
pid = os.getpid()

# Psutil constructs a process object based on the PID
p = psutil.Process(pid)
print('process info')
print(' name :', p.name())
print(' exe :', p.exe())

data = []
while True:
    data += list(range(100000))
    info = p.memory_full_info()
    # COnvert to MB
    memory = info.uss /1024 / 1024
    print('Memory used: {:.2f} MB'.format(memory))
    if memory > 40:
        print('Memory is too big! Exiting')
        sys.exit()
    time.sleep(1)




