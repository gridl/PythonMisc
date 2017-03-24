# fabfile.py

from fabric.api import cd, env, prefix, run, task

env.hosts = ['10.184.195.47']  # where to ssh

@task
def memory_usage():
    run('free -m')

@task
def deploy():
    with cd('/'):
        run('ls')

