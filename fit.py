import ftplib

def check_anon(host):
    try:
        ftplib.FTP(host).login()
        print(f"[+] {host} allows anonymous FTP login.")
    except:
        print(f"[-] {host} does NOT allow anonymous FTP.")

check_anon("ftp.be.debian.org")