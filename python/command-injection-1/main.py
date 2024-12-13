from pingutil import PingRemote

# Showcasing blind command injection
# Vulnerable code -> pingutil.py
# Vulnerable function -> PingRemote
def main():
    host = input("> Enter the host to ping: ")
    PingRemote(host)



if __name__ == '__main__':
    main()
