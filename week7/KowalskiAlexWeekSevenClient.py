import socket as sk;

def handle_client(sock: sk.socket):
    sock.send(b"Hello, World!");
    print("Sent data to server");
    sock.close()
    print("Disconnected from server...");

HOST = "127.0.0.1";
PORT = 8080;

def main():
    with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT));
        print(f"Connected to {HOST}:{PORT}");
        handle_client(sock);

if __name__ == "__main__":
    main();
