import socket
import yaml
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DEVICES_FILE = BASE_DIR / "config" / "devices.yaml"


def load_devices():
    with open(DEVICES_FILE, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data.get("devices", [])


def test_telnet_connection(host, port, timeout=5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True, None
    except socket.timeout:
        return False, "Timeout"
    except ConnectionRefusedError:
        return False, "Connexion refusée"
    except OSError as error:
        return False, str(error)


def main():
    devices = load_devices()

    print("=== Test des connexions Telnet GNS3 ===\n")

    for device in devices:
        name = device.get("name", "UNKNOWN")
        host = device.get("host")
        port = int(device.get("port", 23))

        print(f"[+] Test {name} — {host}:{port}")

        success, error = test_telnet_connection(host, port)

        if success:
            print(f"    OK : connexion possible\n")
        else:
            print(f"    ERREUR : {error}\n")


if __name__ == "__main__":
    main()