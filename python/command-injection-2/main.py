from configparser import ConfigParser
import subprocess

def main():
    conf = ConfigParser()
    config = conf.read("api.config")


    key = conf.get('secret', 'api')
    url = conf.get('URL', 'url')
    
    print(f"Grabbing {url} using {key}...")
    subprocess.run(f"curl {url}", shell=True)


if __name__ == "__main__":
    main()
