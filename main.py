import socket
import ipaddress

host = "IP_TARGET" #example: 192.168.1.1

def check_ip(host_to_check:str):
    if host_to_check == "IP_TARGET":
        print(f" [!] Remember change IP_TARGET! 🐍❗")
        print(f" [X] Closing script...")
        exit()

    try:
        ipaddress.ip_address(host_to_check)
        return host_to_check
    except ValueError as e:
        print(f" [!] Check IP format {host_to_check}! 🐍❗")
        print(f" [X] Closing script...")
        exit()


def tcp_scan(host:str):
    fp = {
        b"SSH": "SSH Server",
        b"HTTP": "HTTP Server",
        b"220": "FTP/SMTP Banner"
        # more soon :)
    }
    print(f"    OPEN TCP PORTS ({host}):\n")

    for port in range(1, 1024):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        try:
            r = s.connect_ex((host,port))
            if r != 0:
                continue
            
            try:
                d = s.recv(32)
            except:
                d = b""

            if d == b"" and port in (80,8080,8000):
                s.sendall(b"GET / HTTP/1.1\r\nHost: x\r\n\r\n")
                try:
                    d = s.recv(64)
                except socket.timeout:
                    d = b""
        
            det = "desconocido"
            for k, v in fp.items():
                if d.startswith(k):
                    det = v
                    break

            print(f" [!] {port:5d}  {det:12s}  hex={d[:16].hex()}  raw={d!r}\n")

        except KeyboardInterrupt as e:
            print(f"[X] Keyboard Interrupt! stopping the scan... 🐍")
            exit()
        except Exception as e:
            print(f" [X] ERROR: {e} \n🐍❔")
            exit()

        finally:
            s.close()

if __name__ == "__main__":
    print("======================================")
    print("    🔍 Simple TCP Fingerprinter 🐍    ")
    print("======================================")
    print("")

    validated_ip = check_ip(host)
    tcp_scan(validated_ip)
