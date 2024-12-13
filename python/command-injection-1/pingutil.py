import subprocess

def PingRemote(host):
    cmd = f'ping -c 1 {host}'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = proc.communicate()
    
    if proc.returncode != 0:
        raise RuntimeError('PingHost failed! Maybe ping is not installed?')


