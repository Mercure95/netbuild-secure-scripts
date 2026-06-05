import time
import socket
from pathlib import Path

import yaml
from netmiko import ConnectHandler


BASE_DIR = Path(__file__).resolve().parent.parent
DEVICES_FILE = BASE_DIR / "config" / "devices.yaml"
HARDENING_FILE = BASE_DIR / "config" / "hardening_profile.yaml"


def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


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


def check_compliance(running_config, compliance_checks):
    passed = []
    failed = []

    for check in compliance_checks:
        if check in running_config:
            passed.append(check)
        else:
            failed.append(check)

    return passed, failed


def apply_hardening(device, hardening_commands, compliance_checks):
    name = device.get("name", "UNKNOWN")
    host = device.get("host")
    port = int(device.get("port", 23))

    print(f"\n=== {name} — {host}:{port} ===")

    success, error = test_telnet_connection(host, port)

    if not success:
        print(f"[ERREUR] Connexion Telnet impossible : {error}")
        return

    print("[OK] Port Telnet joignable")

    connection_params = {
        "device_type": device.get("device_type", "cisco_ios_telnet"),
        "host": host,
        "port": port,
        "username": device.get("username", ""),
        "password": device.get("password", ""),
        "secret": device.get("secret", ""),
        "timeout": 10,
        "global_delay_factor": 2,
    }

    try:
        print("[+] Connexion Netmiko en Telnet...")
        connection = ConnectHandler(**connection_params)

        # Passage en enable si un secret est fourni
        if device.get("secret"):
            connection.enable()

        print("[+] Application des commandes de hardening...")
        output = connection.send_config_set(hardening_commands)
        print(output)

        print("[+] Sauvegarde de la configuration...")
        save_output = connection.send_command_timing("write memory")
        print(save_output)

        time.sleep(1)

        print("[+] Vérification de conformité...")
        running_config = connection.send_command("show running-config")

        passed, failed = check_compliance(running_config, compliance_checks)

        print("\n[CONFORME]")
        for item in passed:
            print(f"  - {item}")

        if failed:
            print("\n[NON CONFORME]")
            for item in failed:
                print(f"  - {item}")
        else:
            print("\n[OK] Tous les contrôles sont conformes")

        connection.disconnect()

    except Exception as error:
        print(f"[ERREUR] Problème avec {name} : {error}")


def main():
    devices_data = load_yaml(DEVICES_FILE)
    hardening_data = load_yaml(HARDENING_FILE)

    devices = devices_data.get("devices", [])
    hardening_commands = hardening_data.get("hardening_commands", [])
    compliance_checks = hardening_data.get("compliance_checks", [])

    print("=== Hardening Telnet des switchs GNS3 ===")

    for device in devices:
        apply_hardening(device, hardening_commands, compliance_checks)


if __name__ == "__main__":
    main()