import socket
import threading
import pyperclip
from termcolor import colored

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(colored(f"[+] {port}/tcp: Open", "green"))
            pyperclip.copy(f"{port}/tcp")
            with open("PORTS.txt", "a") as file:
                file.write(f"{port}/tcp\n")
        sock.close()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
    except:
        pass

def main():
    print(colored("""
------------------------------------------------------------
Welcome to the Python Interactive Port Scanner.
------------------------------------------------------------""", "cyan"))

    ip = input(colored("Enter the IP address you want to scan: ", "blue"))

    print(colored(f"\nScanning all ports on {ip}...\n", "yellow"))

    threads = []
    for port in range(1, 65536):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(colored("\nPort scan complete.", "cyan"))
    print(colored("Open ports copied to clipboard.", "green"))

    help_message = """
------------------------------------------------------------
To view the open ports on your system, open a text editor
(such as Notepad), paste the contents of your clipboard, 
and save the file with the name 'open_ports.txt' in the 
current directory.
------------------------------------------------------------"""
    print(colored(help_message, "cyan"))

if __name__ == "__main__":
    main()