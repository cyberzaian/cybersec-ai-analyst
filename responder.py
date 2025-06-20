import subprocess

def block_ip(ip):
    if ip:
        try:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
            return f"Blocked IP: {ip}"
        except Exception as e:
            return f"Error blocking IP: {e}"
    return "No IP to block."
