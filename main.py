import socket

host = "192.168.1.1"

print("""
====================================
    🔍Simple TCP Fingerprinter🐍
====================================""")
print(f"""\n    OPEN TCP PORTS ({host}):
""")

def tcp_scan(host:str):
    fp = {
        b"SSH": "SSH Server",
        b"HTTP": "HTTP Server",
        b"220": "FTP/SMTP Banner"
        # more soon :)
    }

    for port in range(1, 8100):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

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
    tcp_scan(host)