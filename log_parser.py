import re

def parse_logs(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    log_entries = []
    for line in lines:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
        ip = match.group(1) if match else None
        log_entries.append({
            "line": line.strip(),
            "ip": ip,
        })
    return log_entries
